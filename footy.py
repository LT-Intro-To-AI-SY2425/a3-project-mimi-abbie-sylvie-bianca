from footy_data import footy_db
from match import match
from typing import List, Tuple, Callable, Any

def get_player(footy: Tuple[str, str, int, int, int]) -> str:
    return footy[0] 


def get_team(footy: Tuple[str, str, int, int, int]) -> str:
    return footy[1]


def get_mins(footy: Tuple[str, str, int, int, int]) -> int:
    return footy[2] 


def get_goals(footy: Tuple[str, str, int, int, int]) -> int:
    return footy[3] 

def get_assists(footy: Tuple[str, str, int, int, int]) -> int:
    return footy[4]



# def players_by_team(matches: List[str]) -> List[str]:
#     team = str(matches[0])
#     result = []
#     for footy in footy_db:
#         print(footy)
#         if get_team(footy) == team:
#             print("match")
#             # result.append(get_team(footy))
#     return results

def players_by_team(matches: List[str]) -> List[str]:
    team = str(matches[0])
    result = []
    # print(f"Searching for players on team: {team}")  # Debug: print the team being searched
    for footy in footy_db:
        if get_team(footy) == team:
            # print(f"Found player: {get_player(footy)}")
            result.append(get_player(footy))
    return result

def team_by_player(matches: List[str]) -> List[str]:
    player = str(matches[0])
    result = []
    for footy in footy_db:
        players = get_player(footy)
        if player in players:
            result.append(get_team(footy))
            break
    return result

# def player_by_goal(matches: List[str]) -> List[str]:
#     goal_start = int(matches[0])
#     result = []
#     for footy in footy_db:
#         if(get_goals(footy) >= goal_start):
#             result.append(get_player(footy))
#     return result

def assists_by_player(matches: List[str]) -> List[str]:
    player = str(matches[0])
    result = []
    for footy in footy_db:
        players = get_player(footy)
        if(player in players):
            result.append(get_assists(footy))
    return result  


def player_by_goal(matches: List[str]) -> List[str]:
    goal_given = int(matches[0])
    result = []
    for footy in footy_db:
        if get_goals(footy) == goal_given:
            result.append(get_player(footy))
            break
    return result

def player_by_assists(matches: List[str]) -> List[str]:
    assists_given = int(matches[0])
    result = []
    for footy in footy_db:
        if get_assists(footy) == assists_given:
            result.append(get_player(footy))
            break
    return result

# dummy argument is ignored and doesn't matter
def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt
def player_by_min(matches: List[str])-> List[str]:
    mins_given = int(matches[0])
    result = []
    for footy in footy_db:
        if get_mins(footy) == mins_given:
            result.append(get_player(footy))
            break
    return result


def mins_by_player(matches: List[int])-> List[int]:
    player_given = str(matches[0])
    result = []
    for footy in footy_db:
        if get_player(footy) == player_given:
            result.append(get_mins(footy))
            break
    return result

def player_by_assists(matches: List[str])-> List[str]:
    assists_given = int(matches[0])
    result = []
    for footy in footy_db:
        if get_assists(footy) == assists_given:
            result.append(get_player(footy))
            break
    return result
def player_by_min_range(matches: List[str])-> List[str]:
    mins_given = int(matches[0])
    result = []
    for footy in footy_db:
        if get_mins(footy) >= mins_given:
            result.append(get_player(footy))
    return result

def player_by_goal_range(matches: List[str]) -> List[str]:
    goal_range_given = int(matches[0])
    result = []
    for footy in footy_db:
        if get_goals(footy) >= goal_range_given:
            result.append(get_player(footy))
    return result
def mins_by_player(matches: List[int])-> List[int]:
    player_given = str(matches[0])
    result = []
    for footy in footy_db:
        if get_player(footy) == player_given:
            result.append(get_mins(footy))
            break
    return result

def player_by_assists(matches: List[str])-> List[str]:
    assists_given = int(matches[0])
    result = []
    for footy in footy_db:
        if get_assists(footy) == assists_given:
            result.append(get_player(footy))
            break
    return result

# The pattern-action list for the natural language query system A list of tuples of
# pattern and action It must be declared here, after all of the function definitions
pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what players play on % "), players_by_team),
    (str.split("what player scored _ goals"), player_by_goal),
    (str.split("how many assists does %  have"), assists_by_player),
    (str.split("what player had _ assists"), player_by_assists),
    (str.split("what team does % play for"), team_by_player),
    (str.split("what player played for over _ minutes"), player_by_min_range),
    (str.split("how many minutes did % play"), mins_by_player),
    (str.split("what players scored over _ goals"), player_by_goal_range),
    (["bye"], bye_action)
]


def search_pa_list(src: List[str]) -> List[str]:
    for pat, act in pa_list:
        val = match(pat, src)
        # print(f"Pattern: {pat}, Matched: {val}")  # Debug: print the pattern and matched values
        if val is not None:
            team = " ".join(val)  # Ensure correct extraction of the team name
            # print(f"Extracted team: {team}")  # Debug: print extracted team
            result = act(val)
            if result:
                return result
            else:
                return ["No answers"]
    return ["I don't understand"]


def query_loop() -> None:
    print("Welcome to the EPL database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for answer in answers:
                print(answer)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")
query_loop()

