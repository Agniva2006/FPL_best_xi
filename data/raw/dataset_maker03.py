from soccerdata import Understat
u = Understat(leagues="ENG-Premier League", seasons=range(2020,2025))
xg_data = u.read_team_match_stats()
xg_data.head()
