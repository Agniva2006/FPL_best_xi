import pandas as pd

def build_features(df):
    # create same rolling/lag features as Step 2
    rolling_features = ['total_points', 'minutes', 'goals_scored', 'assists', 'clean_sheets']
    window_sizes = [3, 5, 10]

    df = df.sort_values(['name', 'season', 'gameweek'])
    for feat in rolling_features:
        for w in window_sizes:
            df[f'{feat}_roll{w}'] = (
                df.groupby('name')[feat]
                  .transform(lambda x: x.shift(1).rolling(window=w, min_periods=1).mean())
            )
    df['last_points'] = df.groupby('name')['total_points'].shift(1).fillna(0)
    df['form_points'] = 0.5*df['total_points_roll3'] + 0.3*df['total_points_roll5'] + 0.2*df['total_points_roll10']
    return df
