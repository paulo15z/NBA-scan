from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd

def get_team_games(team_name="Golden State Warriors"):
    """Retorna os últimos jogos do time especificado."""
    nba_teams = teams.get_teams()
    team = next((t for t in nba_teams if t['full_name'] == team_name), None)

    if not team:
        raise ValueError("Time não encontrado!")
    
    team_id = team["id"]
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id)
    games = gamefinder.get_data_frames()[0]

    return games

if __name__ == "__main__":
    df = get_team_games()
    print(df.head()) #mostra os primeiros jogos do time
    