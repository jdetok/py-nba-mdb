from time import sleep
from nba_api.stats.endpoints import leaguegamefinder, commonallplayers, playbyplayv3
import pandas as pd
from datetime import datetime as dt
import logs
import nba_api.stats.library.http as nba

# TODO - play by play data with playbyplayv3

def get_players(league='all', current=1, szn=None): # pass 0 to get all players
    lgs = ['NBA', 'WNBA', 'GNBA']
    if league != 'all':
        lgs = [league]

    pls = []
    for lg in lgs:
        try:
            raw = commonallplayers.CommonAllPlayers(is_only_current_season=current, 
                                                    league_id='10' if lg == 'WNBA' \
                                                        else ('20' if lg == 'GNBA' else '00'),
                                                        season=szn if current == 0 else None
                                                        ).get_data_frames()[0]    
            
            raw['lg'] = lg
            pl = raw.copy()
            pl = pl.rename(columns={'PERSON_ID': 'player_id', 'DISPLAY_FIRST_LAST': 'player',
                                    'TEAM_ID': 'team_id', 'ROSTERSTATUS': 'active'})
            pl = pl[['player_id', 'player', 'team_id', 'lg', 'active']]
            pls.append(pl.copy())
        except Exception as e:
            logs.append_log(f'ERROR fetching current players:\n********** {e}')
    return pd.concat(pls)

def game_logs(game_date, game_date_to=None, player_team = 'P', lg = 'NBA'):
    attempt = 0
    while attempt < 5:
        try:
            df = leaguegamefinder.LeagueGameFinder(
                player_or_team_abbreviation=player_team,
                league_id_nullable= '10' if lg == 'WNBA' else ('20' if lg == 'GNBA' else '00'), 
                date_from_nullable=game_date,
                date_to_nullable=game_date_to if game_date_to else game_date
            ).get_data_frames()[0]
            
            # CRUCIAL -- ADD LG TO THIS DF
            df['lg'] = lg
            
            logs.append_log(f" "
                f"{df.shape[0]} {lg} {'team' if player_team == 'T' else 'player'} rows fetched for {game_date} - {game_date_to}")
            return df
        
        except Exception as e:
            print(e)
            logs.log_print(f'ERROR fetching {lg} game logs for {game_date} after {attempt + 1} attempts...:\n*********** {e}\nIntentionally delaying for 5 minutes...')
            sleep(300) # timeout for 5 minutes just to be safe
            attempt+=1
    
# convert start and end date in 01/01/2025 format to list of dates

def main():
    print(get_players('WNBA', 0, '2024-25'))
    
if __name__=='__main__':
        main()