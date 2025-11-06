#******************************************************************************
# Author:           Brian O'Grady
# Assignment:       Assignment 02
# Date:             10/21/2025
# Description:      This program calculates the gear ratio by dividing the 
#                   number of teeth on the front chainring by the number
#                   of teeth on the rear cog.
# Revisions:        A01.1 - 09/06/2024 - Initialization, set up variables
#                           and initial function logic. Provide a printout of
#                           the variables.
#                   A02.1 - 10/21/2024 - Refactor code to add functions
#                           and improve readability. Add comments.
#******************************************************************************
def main():

    bike_id = ""
    chainring = 0
    chainring_count = 0
    cog = 0
    cog_count = 0
    gear_ratio = 0.0
    num_gear = 0

    print_intro()
    bike_id = get_bike_id()
    chainring, chainring_count = get_sprocket("Chainring")
    cog, cog_count = get_sprocket("Cog")
    gear_ratio = calculate_gear_ratio(chainring, cog)
    num_gear = calculate_num_gear(chainring_count, cog_count)
    print_bike_info(bike_id, chainring, cog, gear_ratio, num_gear)
    print_outro()


def print_intro():
    """
    Prints the introduction to the program.
    :param: none
    :return: none
    """

    print("Welcome to the bicycle gear ratio calculator!\n")


def get_bike_id():
    """
    Prompts for the bike ID used to identify the bicycle.
    :param: none
    :return: bike id entered by the user, string
    """

    bike_id = input("Enter a unique bike ID: ")
    return bike_id


def get_sprocket(prompt):
    count = 0
    compare = 0
    sprockets = 0
    print(f"Enter the sprocket sizes for {prompt} (enter 0 to exit): ")
    sprockets = int(input(""))
    compare = sprockets
    while sprockets != 0:
        count += 1
        if sprockets >= compare:
            compare = sprockets
            sprockets = int(input(""))
        else:
            sprockets = int(input(""))
    return compare, count
        

def calculate_gear_ratio(chainring, cog):
    """
    Compute the gear ratio between chainring and cog.

    The gear ratio is defined as chainring divided by cog.

    Parameters
    ----------
    chainring : int or float
        Number of teeth on the front chainring.
    cog : int or float
        Number of teeth on the rear cog. Must be non-zero.

    Returns
    -------
    float
        The gear ratio (chainring / cog).

    Raises
    ------
    ZeroDivisionError
        If ``cog`` is zero.
    """

    gear_ratio = chainring / cog
    return gear_ratio


def calculate_num_gear(chainring_count, cog_count):
    num_gear = chainring_count * cog_count
    return num_gear


def print_bike_info(bike_id, chainring, cog, gear_ratio, num_gear):
    """
    Prints formatted bike information and the computed gear ratio.
    :param bike_id: the bike identifier (string)
    :param chainring: number of teeth on the front chainring (int)
    :param cog: number of teeth on the rear cog (int)
    :param gear_ratio: computed gear ratio (float)
    :return: none
    """

    print("\nBike ID - Chainring - Cog - Gear ratio - # Gears")
    print(f"{bike_id}   |   {chainring}   |   {cog}   |   {gear_ratio:.2f}   |   {num_gear}")


def print_outro():
    """
    Prints a short closing message to the user.
    :param: none
    :return: none
    """

    print("\nThank you for using the bicycle gear ratio calculator!")

main()