# main.py - FastAPI Backend for FotMob Mini App

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from data import PLAYERS, LEAGUES, STANDINGS, MATCHES, NEWS, TRANSLATIONS

app = FastAPI(title="FotMob Mini App API")

# CORS sozlamalari
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =============================
# API ENDPOINTS
# =============================

@app.get("/api/matches")
async def get_matches(league_id: str = None, date: str = None):
    """Barcha o'yinlar yoki filtr bo'yicha"""
    result = MATCHES
    
    if league_id:
        result = [m for m in result if m["league_id"] == league_id]
    
    if date:
        result = [m for m in result if m["date"] == date]
    
    return {"matches": result}


@app.get("/api/match/{match_id}")
async def get_match(match_id: int):
    """Bitta o'yin tafsilotlari"""
    for match in MATCHES:
        if match["id"] == match_id:
            return match
    raise HTTPException(status_code=404, detail="O'yin topilmadi")


@app.get("/api/news")
async def get_news():
    """Barcha yangiliklar"""
    return {"news": NEWS}


@app.get("/api/news/{news_id}")
async def get_news_detail(news_id: int):
    """Bitta yangilik tafsilotlari"""
    for news in NEWS:
        if news["id"] == news_id:
            return news
    raise HTTPException(status_code=404, detail="Yangilik topilmadi")


@app.get("/api/player/{player_id}")
async def get_player(player_id: int):
    """O'yinchi profili"""
    if player_id in PLAYERS:
        return PLAYERS[player_id]
    raise HTTPException(status_code=404, detail="O'yinchi topilmadi")


@app.get("/api/leagues")
async def get_leagues():
    """Barcha ligalar"""
    return {"leagues": list(LEAGUES.values())}


@app.get("/api/standings/{league_id}")
async def get_standings(league_id: str):
    """Liga jadvali"""
    if league_id in STANDINGS:
        return {"standings": STANDINGS[league_id], "league": LEAGUES.get(league_id)}
    raise HTTPException(status_code=404, detail="Liga jadvali topilmadi")


@app.get("/api/translations/{lang}")
async def get_translations(lang: str):
    """Tarjimalar"""
    if lang in TRANSLATIONS:
        return TRANSLATIONS[lang]
    return TRANSLATIONS.get("uz", {})


# =============================
# STATIC FILES & FRONTEND
# =============================

# Static fayllarni ulash
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.get("/", response_class=HTMLResponse)
async def root():
    """Asosiy sahifa"""
    return FileResponse(os.path.join(BASE_DIR, "index.html"))


@app.get("/style.css")
async def get_css():
    """CSS fayli"""
    return FileResponse(os.path.join(BASE_DIR, "style.css"), media_type="text/css")


@app.get("/script.js")
async def get_js():
    """JavaScript fayli"""
    return FileResponse(os.path.join(BASE_DIR, "script.js"), media_type="application/javascript")


# =============================
# RUN SERVER
# =============================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
