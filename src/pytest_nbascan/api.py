from fastapi import FastAPI
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd

app = FastAPI

@app.get(("/"))
def read_root():
    return {"message": "Bem-vindo à API NBA Scan!"}

@app.get("/teams") #RETORNA A LISTA DE TIMES DA NBA
def get_teams():
    nba_teams = teams.get_teams()
    return nba_teams

@app.get("/games/{team_name}")
def get_team_games(team_name: str): # RETORNA OS ULTIMOS JOGOS DE UM TIME ESPECIFICO#
    nba_teams = teams.get_teams()
    team = next((t for t in nba_teams if t['full_name'].lower() == team_name.lower()), None)

    if not team:
        return {"error": "Time não encontrado!"}

    team_id = team["id"]
    gamefinder = leaguegamefinder.LeagueGameFinder(vs_team_id_nullable=team_id)
    games = gamefinder.get_data_frames()[0]

    return games.to_dict(orient="records")