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
    cog = 0
    gear_ratio = 0.0

    print_intro()
    bike_id = get_bike_id()
    chainring = get_chainring_teeth()
    cog = get_cog_teeth()
    gear_ratio = calculate_gear_ratio(chainring, cog)
    print_bike_info(bike_id, chainring, cog, gear_ratio)
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


def get_chainring_teeth():
    """
    Prompts for the number of teeth on the front chainring.
    :param: none
    :return: number of chainring teeth, int
    """

    chainring = int(input("Enter the number of teeth on the chainring: "))
    return chainring


def get_cog_teeth():
    """
    Prompts for the number of teeth on the rear cog.
    :param: none
    :return: number of cog teeth, int
    """

    cog = int(input("Enter the number of teeth on the cog: "))
    return cog


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


def print_bike_info(bike_id, chainring, cog, gear_ratio):
    """
    Prints formatted bike information and the computed gear ratio.
    :param bike_id: the bike identifier (string)
    :param chainring: number of teeth on the front chainring (int)
    :param cog: number of teeth on the rear cog (int)
    :param gear_ratio: computed gear ratio (float)
    :return: none
    """

    print("\nBike ID - Chainring - Cog - Gear ratio")
    print(f"{bike_id}   |   {chainring}   |   {cog}   |   {gear_ratio:.2f}")


def print_outro():
    """
    Prints a short closing message to the user.
    :param: none
    :return: none
    """

    print("\nThank you for using the bicycle gear ratio calculator!")

main()