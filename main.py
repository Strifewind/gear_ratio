# *****************************************************************************
# Author:           Brian O'Grady
# Assignment:       Assignment 03
# Date:             11/10/2025
# Description:      This program calculates the gear ratio by dividing the
#                   number of teeth on the front chainring by the number
#                   of teeth on the rear cog.
# Revisions:        A01.1 - 09/06/2024 - Initialization, set up variables
#                           and initial function logic. Provide a printout of
#                           the variables.
#                   A02.1 - 10/21/2024 - Refactor code to add functions
#                           and improve readability. Add comments.
#                   A02.2 - 10/26/2024 - Update docstring with a corrected
#                           format. Added a description in welcome message.
#                   A03.1 - 11/10/2025 - Cleaned up functions to reduce reused
#                           code. Added Menu loop to allow user controls.
#                   A03.2 - 11/16/2025 - Removed logic from get_options, added
#                           module for input validation. Changed inputs to
#                           use the validation module and functions. Added
#                           error handling for invalid inputs across get funcs
#                   A03.3 - 11/20/2025 - Removed redundant prompts in main loop.
#                           Fixed get_option response after invalid input.
# *****************************************************************************
import valid as v

DESCRIPTION = 1
SUBMIT_BIKE = 2
PRINT_MENU = 3
QUIT = 4
MINIMUM = 11
MAXIMUM = 75


def main():
    bike_id = ""
    chainring_big = 0
    chainring_small = 0
    chainring_count = 0
    cog_big = 0
    cog_small = 0
    cog_count = 0
    gear_ratio = 0.00
    num_gear = 0
    option = 0

    print_intro()
    print_options()
    option = get_option()

    while option != QUIT:
        if option == DESCRIPTION:
            print_description()
        elif option == SUBMIT_BIKE:
            bike_id = get_bike_id()
            (chainring_big,
                chainring_small,
                chainring_count) = get_sprocket("Chainring")
            cog_big, cog_small, cog_count = get_sprocket("Cog")
            gear_ratio = calculate_gear_ratio(chainring_big, cog_small)
            num_gear = calculate_num_gear(chainring_count, cog_count)
            print_bike_info(bike_id,
                            chainring_big,
                            chainring_small,
                            cog_big, cog_small,
                            gear_ratio,
                            num_gear)
        elif option == PRINT_MENU:
            print_options()
        else:
            print("Invalid option. Please choose a valid menu item.")
        
        print_end(option)
        option = get_option()


def print_intro():
    """
    Prints the introduction to the program.
    :param: none
    :return: none
    """

    print("\t\tWelcome to Gear Calculator!")
    print("Let us explore your bike and make calculating gear ratios easy.")


def print_options():
    """
    Displays a list of menu options for the user to choose from.

    :param: None
    :return: None
    """

    print("""
Select from the following options

1.     Program overview 
2.     Enter your bike details
3.     Print menu options
4.     Close program
          """)


def print_description():
    """
    Prints a description of how gear ratios work for bicycles.

    This function explains how to calculate gear ratio and number of gears,
    and describes the benefits of low vs. high gear ratios for different
    riding conditions.

    :param: None
    :return: None
    """

    print("""
Input your chainring and cog sizes to find the perfect ratio!\n
\tGear ratio = Chainring teeth / Cog teeth
\t# Gears = count of chainring + count of cog\n
A lower gear ratio will mean easier pedaling, ideal for climbing hills.
While a higher gear ratio means harder pedaling but more speed, ideal
for flat roads.
          """)


def print_bike_info(bike_id,
                    chainring_big,
                    chainring_small,
                    cog_big, cog_small,
                    gear_ratio,
                    num_gear):
    """
    Prints formatted bike information and the computed gear ratio.
    :param bike_id: the bike identifier (string)
    :param chainring: number of teeth on the front chainring (int)
    :param cog: number of teeth on the rear cog (int)
    :param gear_ratio: computed gear ratio (float)
    :return: none
    """

    bike_t = f"{'Bike ID':<10}"
    chainring_t = f"{'Chainring':<12}"
    cog_t = f"{'Cog':<12}"
    gear_t = f"{'Gear Ratio':<12}"
    gears_t = f"{'# Gears':<8}"
    bike_p = f"{bike_id:<10}"
    chainring_p = f"{f'{chainring_small}-{chainring_big}':<12}"
    cog_p = f"{f'{cog_small}-{cog_big}':<12}"
    gear_p = f"{gear_ratio:<12.2f}"
    gears_p = f"{num_gear:<8}"

    print(f"\n{bike_t} | {chainring_t} | {cog_t} | {gear_t} | {gears_t}")
    print(f"{bike_p} | {chainring_p} | {cog_p} | {gear_p} | {gears_p}")


def print_end(option):
    """
    Prints a message indicating the end of a section based on the option.
    :param option: the menu option selected by the user (int)
    :return: none
    """

    if option == DESCRIPTION:
        print("\nSelect another menu option. Enter 3 to see options.")
    elif option == SUBMIT_BIKE:
        print("\nBike details submitted. Enter 3 to see options.")


def print_outro():
    """
    Prints a short closing message to the user.
    :param: none
    :return: none
    """

    print("\nThank you for using the bicycle gear ratio calculator!")


def get_option():
    """
    Gets the user's menu option choice with validation.
    :param: none
    :return: option selected by the user, integer
    """
    option = v.get_integer("Enter your response: ")

    return option


def get_bike_id():
    """
    Prompts for the bike ID used to identify the bicycle.
    :param: none
    :return: bike id entered by the user, string
    """

    bike_id = v.get_string("Enter a unique bike ID: ")
    return bike_id


def get_sprocket(prompt):
    """
    This function asks the user to enter sprocket sizes and keeps track of
    the largest, smallest, and total number of valid sprockets entered.

    :param prompt: A message to show the user when asking for sprocket sizes.
    :return: A tuple with the largest sprocket, smallest sprocket, and the 
    total count of valid sprockets entered.
    """

    count = 0
    compare_large = 0
    compare_small = 0

    print(f"Enter the sprocket sizes for {prompt} (enter 0 to exit): ")
    sprockets = v.get_integer("Enter Sprocket: ")
    if sprockets == 0:
        print("Please enter at least one sprocket size.")
        sprockets = v.get_integer("Enter Sprocket: ")
    while sprockets != 0:
        if sprockets < MINIMUM or sprockets > MAXIMUM:
            print("Invalid sprocket size,")
            print(f"need a value between {MINIMUM} and {MAXIMUM}")
            sprockets = v.get_integer("Enter Sprocket: ")
        while sprockets > 0:
            count += 1
            compare_large, compare_small = calculate_compare(sprockets,
                                                             compare_small,
                                                             compare_large)
            sprockets = v.get_integer("Enter Sprocket: ")

    return compare_large, compare_small, count


def calculate_gear_ratio(chainring_big, cog_small):
    """
    This function finds the gear ratio by dividing the number of teeth on the
    largest front gear by the number of smallest teeth on the back gear.

    :param chainring_big: The number of teeth on the front chainring.
    :param cog_small: The number of teeth on the rear cog.
    :return: The gear ratio as a float.
    """

    gear_ratio = chainring_big / cog_small
    return gear_ratio


def calculate_num_gear(chainring_count, cog_count):
    """
    This function calculates the total number of gear combinations by 
    multiplying the number of front gears by the number of rear gears.

    :param chainring_count: The number of gears on the front (chainrings).
    :param cog_count: The number of gears on the back (cogs).
    :return: The total number of gear combinations.
    """

    num_gear = chainring_count * cog_count
    return num_gear


def calculate_compare(sprockets, compare_small, compare_large):
    """
    This function checks if the current sprocket value is smaller or larger
    than the ones being compared, and updates them if needed.

    :param sprockets: The current sprocket value to compare.
    :param compare_small: The smallest sprocket value found so far.
    :param compare_large: The largest sprocket value found so far.
    :return: A tuple with the updated largest and smallest sprocket values.
    """

    if compare_large == 0 or sprockets > compare_large:
        compare_large = sprockets
    if compare_small == 0 or sprockets < compare_small:
        compare_small = sprockets
    return compare_large, compare_small


main()
