import requests
import pandas as pd
import json
from pathlib import Path
# Step 1.1 — latest season snapshot (players, teams, positions)

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