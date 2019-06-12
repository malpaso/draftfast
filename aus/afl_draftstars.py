from os import environ
from draftfast.rules import DRAFT_KINGS, DRAFT_STARS, RuleSet
from draftfast.optimize import run
from draftfast.optimize import run_multi
from draftfast.orm import Player, Roster
from draftfast.csv_parse import salary_download, uploaders
from draftfast.lineup_constraints import LineupConstraints
from draftfast.settings import Stack
from draftfast.settings import OptimizerSettings

DRAFT_STARS_POS = [
  ['FWD', 2, 2],
  ['MID', 4, 4],
  ['DEF', 2, 2],
  ['RK', 1, 1],
]

DS_AFL_RULE_SET = RuleSet(
    site=DRAFT_KINGS,
    league='AFL',
    roster_size=9,
    salary_max=100_000,
    position_limits=DRAFT_STARS_POS,
    general_position_limits=[],
)


class AFLRoster(Roster):
    POSITION_ORDER = {
        'FWD': 0,
        'MID': 1,
        'DEF': 2,
        'RK': 3,
    }


#downloads = environ.get('downloads')
downloads = 'D:/Projects/dfs_research/draftstars/players'
#downloads = 'D:/repos/draft-kings-fun/examples'
players = salary_download.generate_players_from_csvs(
    salary_file_location='{}/AFL_SALS.csv'.format(downloads),
    projection_file_location='{}/AFL_PROJECTIONS.csv'.format(downloads),
    game=DRAFT_STARS,
    ruleset=DS_AFL_RULE_SET,
)


rosters, _ = run_multi(
    iterations=4,
    rule_set=DS_AFL_RULE_SET,
    player_pool=players,
    verbose=True,
    exposure_bounds=[],
    constraints=LineupConstraints(
        locked=[],
        banned=['T. Cotchin','S. Edwards','D. Martin'],
        groups=[],
    ),
)

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
