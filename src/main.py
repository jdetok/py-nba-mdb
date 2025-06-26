from datetime import datetime, timedelta
import clean
import run
import logs
import gmail

# db = 'prod'

def main():
    game_date = (datetime.today() - timedelta(1)).strftime('%m/%d/%Y')
    logmsg = f'Fetching and inserting NBA/WNBA/G-League game logs: {game_date}\n' 
    logs.log_print(logmsg)
    
    # fetch and insert current players into player_temp table
    logs.append_log(f'Fetching current players first...')
    run.fetch_insert_players()
        
    tm_df = run.check_all_lgs(game_date, pl_tm='T')
    if tm_df.empty:
        logs.log_print(f'No logs found for {game_date}, exiting...', brk=True)
        return # no logs, exit
    
    # get player logs if team logs weren't empty
    pl_df = run.check_all_lgs(game_date, pl_tm='P')
    
    # clean data
    team_data = clean.TeamData(tm_df)
    player_data = clean.PlayerData(pl_df, team_data.tgame_df)
    
    # combine player and team tables to one list
    table_dfs = (list(team_data.table_dfs) + list(player_data.table_dfs))
    
    logs.append_log('logs fetched and cleaned, starting DB insert...')
    
    # insert list of all dfs into db
    run.inserts(table_dfs)
    
    # finish and close the log, attach to summary email 
    logs.log_print('Script complete!', brk=True)
    gmail.send_summary()
    
if __name__=='__main__':
    main()
    
