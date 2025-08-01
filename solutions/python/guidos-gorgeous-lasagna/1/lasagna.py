"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 40

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(a):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    remaining_time = EXPECTED_BAKE_TIME - a
    return int(remaining_time)


#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.

def preparation_time_in_minutes(num_of_layers):
    """Calculate the bake time remaining.

    :param num_of_layers: int - the number of layers you desire the lasagna to have.
    :return: int - prep time (in minutes).

    Function that takes the number of layers the user wants the lasagna to have
    and returns how many minutes the lasagna will take to be prepared.
    """
    preparation_time = 2 * num_of_layers
    return(preparation_time)

#TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
def elapsed_time_in_minutes(num_of_layers, elapsed_time_baking):
    """Calculate the bake time remaining.

    :param number_of_layers: int - the number of layers you desire the lasagna to have.
    :param elapsed_time_baking: int - the ammount of time you have been baking the lasagna.
    :return: int - total time (in minutes).

    Function that takes the number of layers and the elapsed time
    and returns how many minutes has been preparing and baking.
    """
    elapsed_time = num_of_layers * 2 + elapsed_time_baking
    return(elapsed_time)