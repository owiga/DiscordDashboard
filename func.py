import httpx


async def get_discord_profile(access_token: str):
    headers = {"Authorization": f"Bearer {access_token}"}

    async with httpx.AsyncClient() as client:
        # 1. Базовый профиль + почта
        user_resp = await client.get("https://discord.com/api/users/@me", headers=headers)
        user_data = user_resp.json()

        # 2. Привязанные аккаунты (Steam, GitHub и т.д.)
        conn_resp = await client.get("https://discord.com/api/users/@me/connections", headers=headers)
        connections = conn_resp.json() if conn_resp.status_code == 200 else []

        # 3. Серверы
        guilds_resp = await client.get("https://discord.com/api/users/@me/guilds", headers=headers)
        guilds = guilds_resp.json() if guilds_resp.status_code == 200 else []

    # Собираем всё в один большой JSON для твоей базы или сайта
    return {
        "profile": user_data,
        "connections": connections,
        "guilds_count": len(guilds),
        "guilds": guilds
    }

async def get_user_presence(discord_id: str):
    url = f"https://api.lanyard.rest/v1/users/{discord_id}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            if response.status_code == 200:
                data = response.json()
                # Lanyard возвращает объект 'data', внутри которого есть список 'activities'
                return data.get("data", {}).get("activities", [])
        except Exception:
            pass
        return []