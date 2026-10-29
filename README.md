# ⚡ Discord Glass Dashboard
![HTML5](https://img.shields.io/badge/HTML5-orange)
![CSS3](https://img.shields.io/badge/CSS3-blueviolet)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

A sleek, modern user analytics and profile dashboard built for Discord users, featuring a custom **glassmorphism** UI powered by Tailwind CSS.

## 🚀 Tech Stack
- **Backend:** FastAPI, Python, `httpx`, OAuth2
- **Frontend:** Jinja2, Tailwind CSS, JavaScript (Polling API)
- **Integrations:** Discord API, Lanyard API (Real-time Rich Presence)

## ✨ Features
- 🔒 **Discord OAuth2 Authorization** with secure session handling.
- 🟢 **Real-time Status Tracking** via Lanyard API with animated indicators.
- 🎨 **Glassmorphic Design** crafted with custom Tailwind utility classes.
- 🔗 **Connected Accounts Showcase** (Spotify, GitHub, Steam, Twitch, YouTube, etc.).
- 📂 **Joined Guilds Grid** displaying user servers and roles.

## ⚡ Quick Start
### 1. Clone the repository
```bash
git clone [https://github.com/owiga/DiscordDashboard.git](https://github.com/owiga/DiscordDashboard.git)
cd DiscordDashboard
```
### 2. Install dependencies
```bash
pip install fastapi uvicorn httpx python-dotenv jinja2
```
### 3. Environment configuration
Create a .env file in the root directory of your project and add your credentials from the Discord Developer Portal:
```bash
DISCORD_CLIENT_ID=your_client_id_here
DISCORD_CLIENT_SECRET=your_client_secret_here
DISCORD_ACCESS_TOKEN=your_client_access_token_here
```
### 4. Run the application
Start the local server using Uvicorn:
```bash
uvicorn main:app --reload
```
Open http://127.0.0.1:8000 in your browser to view the dashboard! 🚀
