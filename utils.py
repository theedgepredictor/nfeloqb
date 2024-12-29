import pandas as pd


def get_schedules():
    '''
    Manually clean scores that are incorrect in the
    game file
    '''
    manual_clean_dict = {
    "2009_17_IND_BUF": {
        "home_score": 30,
        "away_score": 7
    },
    "2013_07_CIN_DET": {
        "home_score": 24,
        "away_score": 27
    },
    "2015_06_ARI_PIT": {
        "home_score": 25,
        "away_score": 13
    },
    "2015_09_PHI_DAL": {
        "home_score": 27,
        "away_score": 33
    },
    "2015_15_KC_BAL": {
        "home_score": 14,
        "away_score": 34
    },
    "2016_01_MIN_TEN": {
        "home_score": 16,
        "away_score": 25
    },
    "2016_05_NE_CLE": {
        "home_score": 13,
        "away_score": 33
    }
    }
    ## create a home and away map ##
    home_map = {k:manual_clean_dict[k]['home_score'] for k in manual_clean_dict.keys()}
    away_map = {k:manual_clean_dict[k]['away_score'] for k in manual_clean_dict.keys()}
    ## apply ##

    scheds = pd.read_csv('http://www.habitatring.com/games.csv')
    scheds['home_score'] = scheds['game_id'].map(home_map).combine_first(scheds['home_score'])
    scheds['away_score'] = scheds['game_id'].map(away_map).combine_first(scheds['away_score'])
    #scheds['away_team'] = scheds['away_team'].str.replace("SD", "LAC").str.replace("OAK", "LV").str.replace("STL", "LA")
    #scheds['home_team'] = scheds['home_team'].str.replace("SD", "LAC").str.replace("OAK", "LV").str.replace("STL", "LA")
    return scheds

def collect_player_stats():
    data = pd.read_parquet(f'https://github.com/nflverse/nflverse-data/releases/download/player_stats/player_stats.parquet')
    return data
def load_players():
    df = pd.read_parquet('https://github.com/nflverse/nflverse-data/releases/download/players/players.parquet')
    return df

def load_win_total_ratings():
    df = pd.read_csv("https://raw.githubusercontent.com/greerreNFL/nfelosrs/main/wt_ratings.csv")
    return df

def load_missing_draft_data():
    df = pd.read_csv("https://github.com/greerreNFL/nfeloqb/raw/refs/heads/main/nfeloqb/Manual%20Data/missing_draft_data.csv",index_col=0)
    return df

def load_original_elo_file():
    df = pd.read_csv("https://github.com/greerreNFL/nfeloqb/raw/refs/heads/main/nfeloqb/Manual%20Data/original_elo_file.csv")
    return df