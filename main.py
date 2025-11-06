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
    chainring_big = 0
    chainring_small = 0
    chainring_count = 0
    cog_big = 0
    cog_small = 0
    cog_count = 0
    gear_ratio = 0.0
    num_gear = 0

    print_intro()
    bike_id = get_bike_id()
    chainring_big, chainring_small, chainring_count = get_sprocket("Chainring")
    cog_big, cog_small, cog_count = get_sprocket("Cog")
    gear_ratio = calculate_gear_ratio(chainring_big, cog_small)
    num_gear = calculate_num_gear(chainring_count, cog_count)
    print_bike_info(bike_id, chainring_big, chainring_small, cog_big, cog_small, gear_ratio, num_gear)
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
    compare_large = None
    compare_small = None
    sprockets = None
    print(f"Enter the sprocket sizes for {prompt} (enter 0 to exit): ")
    while sprockets != 0:
        try:
            sprockets = int(input(""))
            if sprockets < 0:
                print("Please enter only positive whole numbers.")
                continue
            if sprockets == 0:
                break

            count += 1

            if compare_large is None or sprockets > compare_large:
                compare_large = sprockets
            if compare_small is None or sprockets < compare_small:
                compare_small = sprockets
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    return compare_large, compare_small, count
        

def calculate_gear_ratio(chainring_big, cog_small):
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

    gear_ratio = chainring_big / cog_small
    return gear_ratio


def calculate_num_gear(chainring_count, cog_count):
    num_gear = chainring_count * cog_count
    return num_gear


def print_bike_info(bike_id, chainring_big, chainring_small, cog_big, cog_small, gear_ratio, num_gear):
    """
    Prints formatted bike information and the computed gear ratio.
    :param bike_id: the bike identifier (string)
    :param chainring: number of teeth on the front chainring (int)
    :param cog: number of teeth on the rear cog (int)
    :param gear_ratio: computed gear ratio (float)
    :return: none
    """

    print(f"\n{'Bike ID':<10} | {'Chainring':<12} | {'Cog':<12} | {'Gear Ratio':<12} | {'# Gears':<8}")
    print(f"{bike_id:<10} | {f'{chainring_small}-{chainring_big}':<12} | {f'{cog_small}-{cog_big}':<12} | {gear_ratio:<12.2f} | {num_gear:<8}")


def print_outro():
    """
    Prints a short closing message to the user.
    :param: none
    :return: none
    """

    print("\nThank you for using the bicycle gear ratio calculator!")

main()