import random
def monty_hall_game(switch_door):

    door_choices = ['goat', 'goat', 'car']
    random.shuffle(door_choices)

    initial_choice = random.choice(range(3))

    revealed_doors = [i for i in range(3) if i != initial_choice and door_choices[i] != "car"]
    revealed_door = random.choice(revealed_doors)

    if switch_door:
        final_choice = [i for i in range(3) if i != revealed_door and i != initial_choice][0]
    else: 
        final_choice = initial_choice

    return door_choices[final_choice] == 'car'


def simulate(num_of_games):
    wins_without_switching = sum(monty_hall_game(False) for _ in range(num_of_games))
    wins_with_switching = sum(monty_hall_game(True) for _ in range(num_of_games))
    return wins_without_switching / num_of_games, wins_with_switching / num_of_games


if __name__ == '__main__':
    num_of_games = 1000
    Percent_win_with_switching, percent_win_without_switching = simulate(num_of_games)