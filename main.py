import httpx
import os

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

from func import get_discord_profile, get_user_presence
from settings import REDIRECT_URI, jinja2_templates
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


load_dotenv()
CLIENT_ID = os.getenv("DISCORD_CLIENT_ID")
CLIENT_SECRET = os.getenv("DISCORD_CLIENT_SECRET")
ACCESS_TOKEN=os.getenv("DISCORD_ACCESS_TOKEN")

@app.get("/login")
def login():
    scopes = "identify email guilds connections rpc rpc.activities.write"
    discord_login_url = (
        f"https://discord.com/api/oauth2/authorize"
        f"?client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&response_type=code"
        f"&scope={scopes.replace(' ', '%20')}"
    )
    return RedirectResponse(discord_login_url)


@app.get("/")
async def index():
    return RedirectResponse("/main")

@app.get("/main")
async def main(request: Request):
    data = await get_discord_profile(ACCESS_TOKEN)
    precence = await get_user_presence(data["profile"]["id"])
    return jinja2_templates.TemplateResponse(request,
        "index.html",
    {
        "profile": data.get("profile", {}),
        "connections": data.get("connections", []),
        "guilds": data.get("guilds", []),
        "guilds_count": data.get("guilds_count", 0),
        "precense": precence,
    })

@app.get("/api/presence")
async def api_presence():
    data = await get_discord_profile(ACCESS_TOKEN)
    activities = await get_user_presence(data["profile"]["id"])
    return {"activities": activities}

@app.get("/auth/callback")
async def auth_callback(code: str):
    token_url = "https://discord.com/api/oauth2/token"
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(token_url, data=data)
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Failed to fetch token from Discord")

        token_data = response.json()
        access_token = token_data.get("access_token")

        user_response = await client.get(
            "https://discord.com/api/users/@me",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        user_info = user_response.json()

    return {
        "message": "Successfully authorized!",
        "username": user_info.get("username"),
        "id": user_info.get("id"),
        "token": access_token,
        "avatar": f"https://cdn.discordapp.com/avatars/{user_info.get('id')}/{user_info.get('avatar')}.png"
    }


