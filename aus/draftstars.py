from draftfast import rules
from draftfast.optimize import run
from draftfast.csv_parse import salary_download
from draftfast.rules import DRAFT_KINGS, RuleSet
from draftfast.lineup_constraints import LineupConstraints
from draftfast.orm import Player, Roster

player_pool = [
    Player(name='A1', team='Q', cost=5500, proj=55, pos='FWD'),
    Player(name='A2', team='A', cost=5500, proj=55, pos='FWD'),
    Player(name='A3', team='AA', cost=5500, proj=55, pos='MID'),
    Player(name='A4', team='A', cost=5500, proj=55, pos='MID'),
    Player(name='A5', team='A', cost=5500, proj=55, pos='MID'),
    Player(name='A6', team='A', cost=5500, proj=55, pos='MID'),
    Player(name='A7', team='A', cost=5500, proj=55, pos='DEF'),
    Player(name='A8', team='A', cost=5500, proj=55, pos='DEF'),
    Player(name='A9', team='A', cost=5500, proj=55, pos='RK'),
    Player(name='A10', team='A', cost=5500, proj=55, pos='RK'),
    Player(name='B1', team='R', cost=5500, proj=55, pos='FWD'),
    Player(name='B2', team='F', cost=5500, proj=55, pos='FWD'),
    Player(name='B3', team='B', cost=5500, proj=55, pos='MID'),
    Player(name='B4', team='B', cost=5500, proj=55, pos='MID'),
    Player(name='B5', team='B', cost=5500, proj=55, pos='MID'),
    Player(name='B6', team='G', cost=5500, proj=55, pos='MID'),
    Player(name='B7', team='B', cost=5500, proj=55, pos='DEF'),
    Player(name='B8', team='E', cost=5500, proj=55, pos='DEF'),
    Player(name='B9', team='D', cost=5500, proj=55, pos='RK'),
    Player(name='B10', team='C', cost=5500, proj=55, pos='RK'),
]

DRAFT_STARS_POS = [
  ['FWD', 2, 2],
  ['MID', 4, 4],
  ['DEF', 2, 2],
  ['RK', 1, 1],
]

DS_AFL_RULE_SET = RuleSet(
    site=rules.DRAFT_KINGS,
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


roster = run(
  rule_set=DS_AFL_RULE_SET,
  player_pool=player_pool,
  verbose=True,
  roster_gen=AFLRoster,
)