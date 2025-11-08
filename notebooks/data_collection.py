import requests
import pandas as pd
import json
from pathlib import Path
# latest season snapshot (players, teams, positions)

url = "https://fantasy.premierleague.com/api/bootstrap-static/"
data = requests.get(url).json()

# save raw JSON
root = Path(__file__).resolve().parents[2]
raw_dir = root / "data" / "raw"
raw_dir.mkdir(parents=True, exist_ok=True)

with open(raw_dir / "bootstrap_static_current.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

# convert to DataFrames
elements       = pd.DataFrame(data["elements"])        # all player stats
teams          = pd.DataFrame(data["teams"])           # team info
element_types  = pd.DataFrame(data["element_types"])   # GK/DEF/MID/FWD

# save csvs
elements.to_csv(raw_dir / "players_current.csv", index=False)
teams.to_csv(raw_dir / "teams.csv", index=False)
element_types.to_csv(raw_dir / "positions.csv", index=False)

print("Current-season FPL data saved in data/raw/")
print("Players:", elements.shape, "Teams:", teams.shape)

import glob
import requests
import pandas as pd


import pandas as pd
import glob
import os

# Define source + target paths
src_path = "C:\\Users\\User\\Desktop\\end-to-end_ml_project\\data\\fpl_history\\data"
output_path = "C:\\Users\\User\\Desktop\\end-to-end_ml_project\\FPL_best_xi\\data\\raw\\all_seasons_fpl.csv"

# Collect all gameweek CSVs across seasons (e.g., 2016–17 … 2024–25)
all_files = sorted(glob.glob(os.path.join(src_path, "20*/gws/gw*.csv")))
print(f" Found {len(all_files)} gameweek files across seasons.")

# Initialize an empty list for DataFrames
dataframes = []

for file_path in all_files:
    try:
        # Extract season and gameweek info from path
        parts = file_path.split(os.sep)
        season = parts[-3] if len(parts) > 3 else "unknown"
        gw = os.path.basename(file_path).replace("gw", "").replace(".csv", "")
        
        df = pd.read_csv(file_path)
        df["season"] = season
        df["gameweek"] = int(gw)
        
        dataframes.append(df)
    except Exception as e:
        print(f" Skipped {file_path} due to error: {e}")

# Concatenate everything
all_seasons_df = pd.concat(dataframes, ignore_index=True)

# Sort chronologically (important for later time-series modeling)
all_seasons_df = all_seasons_df.sort_values(by=["season", "gameweek"]).reset_index(drop=True)

# Drop duplicates and clean small inconsistencies
all_seasons_df.drop_duplicates(inplace=True)

# Save final master dataset
os.makedirs(os.path.dirname(output_path), exist_ok=True)
all_seasons_df.to_csv(output_path, index=False)

print(f" Combined FPL data saved to: {output_path}")
print(f" Shape: {all_seasons_df.shape}")
print(" Columns:", list(all_seasons_df.columns)[:10], "...")

from soccerdata import Understat
u = Understat(leagues="ENG-Premier League", seasons=range(2020,2025))
xg_data = u.read_team_match_stats()
xg_data.head()
