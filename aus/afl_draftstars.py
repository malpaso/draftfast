from os import environ
from draftfast import rules
from draftfast.optimize import run
from draftfast.optimize import run_multi
from draftfast.orm import Player
from draftfast.csv_parse import salary_download, uploaders
from draftfast.lineup_constraints import LineupConstraints
from draftfast.settings import Stack
from draftfast.settings import OptimizerSettings

"""
Script to create 10 AFL lineups for DraftStars.

Assumptions:
- Environment variable called "downloads" has path to downloads
- In downloads, salary, projection and player ID files exist with
  the filenames listed in the script.
- SALARY FILE: Name, Position, Salary, Team, Opponent, FPPG
- PROJECTION FILE: playername, points
"""
#downloads = environ.get('downloads')
#downloads = 'D:/Projects/dfs_research/moneyball/players'
#downloads = 'D:/repos/draft-kings-fun/examples'
#players = salary_download.generate_players_from_csvs(
    #salary_file_location='./examples/AFL_SALS.csv',
    #projection_file_location='./examples/AFL_PROJECTIONS.csv',
    #game=rules.DRAFT_STARS,
    #ruleset=rules.DS_AFL_RULE_SET,
#)

player_pool = [
    Player(name='A1', team='A', cost=5500, proj=55, pos='FWD'),
    Player(name='A2', team='A', cost=5500, proj=55, pos='FWD'),
    Player(name='A3', team='A', cost=5500, proj=55, pos='MID'),
    Player(name='A4', team='A', cost=5500, proj=55, pos='MID'),
    Player(name='A5', team='A', cost=5500, proj=55, pos='MID'),
    Player(name='A6', team='A', cost=5500, proj=55, pos='MID'),
    Player(name='A7', team='A', cost=5500, proj=55, pos='DEF'),
    Player(name='A8', team='A', cost=5500, proj=55, pos='DEF'),
    Player(name='A9', team='A', cost=5500, proj=55, pos='RK'),
    Player(name='A10', team='A', cost=5500, proj=55, pos='RK'),
    Player(name='B1', team='B', cost=5500, proj=55, pos='FWD'),
    Player(name='B2', team='B', cost=5500, proj=55, pos='FWD'),
    Player(name='B3', team='B', cost=5500, proj=55, pos='MID'),
    Player(name='B4', team='B', cost=5500, proj=55, pos='MID'),
    Player(name='B5', team='B', cost=5500, proj=55, pos='MID'),
    Player(name='B6', team='B', cost=5500, proj=55, pos='MID'),
    Player(name='B7', team='B', cost=5500, proj=55, pos='DEF'),
    Player(name='B8', team='B', cost=5500, proj=55, pos='DEF'),
    Player(name='B9', team='B', cost=5500, proj=55, pos='RK'),
    Player(name='B10', team='B', cost=5500, proj=55, pos='RK'),
]


roster = run(
  rule_set=rules.DS_AFL_RULE_SET,
  player_pool=player_pool,
  verbose=True,
)


#rosters, _ = run_multi(
    #iterations=4,
    #rule_set=rules.DS_AFL_RULE_SET,
    #player_pool=players,
    #verbose=True,
    #exposure_bounds=[],
    #constraints=LineupConstraints(
        #locked=[],
        #banned=[],
        #groups=[]
    #),
#)

#constraints=LineupConstraints(
      #locked=[],
      #banned=[], 
      #groups=[],
    #),

#,
    #optimizer_settings=OptimizerSettings(
        #stacks=[
            #Stack(team='HOU', count=2),
            #Stack(team='MIL', count=3),
            #Stack(team='PHI', count=3),
        #]
    #),

#uploader = uploaders.DraftStarsAFLUploader(
    #pid_file='{}/NBA_PIDS.csv'.format(downloads),
#)
#uploader.write_rosters(rosters)
