from penguin_game import *


def do_turn(game):
    """
    Makes the bot run a single turn

    :param game: the current game state
    :type game: Game
    """
    print "Starting"
    my_player = game.get_myself()
    # Get the list of all my penguins
    my_penguins = game.get_myself().get_my_penguins()
    # Find the closest free island
    closest = game.get_neutral_icebergs()[0]
    for island in game.get_neutral_icebergs():
        # Find the closes island
        if island.get_distance(my_penguins[0]) < closest.get_distance(my_penguins[0]):
            closest = island

    # Move the closest penguin to the closest island
    my_penguins[0].move(closest)
