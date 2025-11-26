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
#                   A04.1 - 11/24/2025 - Refactor code to utilize parellel lists
#                           User input is going to be stored in lists in the
#                           index which they were entered. Calculated values
#                           will be determined before printed.
# *****************************************************************************
import valid as v
import helper as w

DESCRIPTION = 1
SUBMIT_BIKE = 2
PRINT_BIKES = 3
QUIT = 4
MINIMUM = 11
MAXIMUM = 75


def main():
    
    bike_id = []
    chainring_list = []
    cog_list = []

    option = 0

    print_intro()    

    while option != QUIT:
        print_options()
        option = get_option()
        
        if option == DESCRIPTION:
            print_description()
        
        elif option == SUBMIT_BIKE:
            add_entry(bike_id, chainring_list, cog_list)

        elif option == PRINT_BIKES:
            process_list(bike_id, chainring_list, cog_list)

        elif option == QUIT:
            print_statistics(bike_id, chainring_list, cog_list)
            print_outro()

        else:
            print("Invalid option. Please choose a valid menu item.")


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
2.     Add bike entry
3.     List added bikes
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
    Ask the user to enter sprocket sizes for a given component (e.g., Chainring or Cog).
    
    Rules:
    - User must enter at least one valid sprocket size before stopping.
    - Input '0' means stop (but only after the first valid value).
    - Valid sprocket sizes fall between MINIMUM and MAXIMUM.
    - Values are inserted in sorted order as they are entered.
    
    Returns:
        A sorted list of all valid sprocket sizes entered.
    """
    print(f"Enter the sprocket sizes for {prompt} (enter 0 to stop): ")

    sprockets = []
    sprocket = v.get_integer("Enter sprocket: ")

    # Require at least one valid sprocket
    while len(sprockets) == 0:
        if sprocket == 0:
            print("Please enter at least one sprocket size.")
        elif sprocket < MINIMUM or sprocket > MAXIMUM:
            print(f"Invalid sprocket size, need between {MINIMUM} and {MAXIMUM}.")
        else:
            sprockets.append(sprocket)

        sprocket = v.get_integer("Enter sprocket: ")

    # Main input loop after first valid entry
    while sprocket != 0:
        if sprocket < MINIMUM or sprocket > MAXIMUM:
            print(f"Invalid sprocket size, need between {MINIMUM} and {MAXIMUM}.")
        else:
            w.insert_sorted(sprockets, sprocket)

        sprocket = v.get_integer("Enter sprocket: ")

    return sprockets


def add_entry(bike_id, chainring_list, cog_list):

    print("\n--- Add a New Bike Entry ---")
    bike_id.append(get_bike_id())

    chainring_list.append(get_sprocket("Chainring"))

    cog_list.append(get_sprocket("Cog"))


def process_list(bike_id, chainring_list, cog_list):

    if len(bike_id) == 0:
        print("No bikes stored yet.\n")
    else:

        print("\n--- Stored Bike Entries ---")

        index = 0
        while index < len(bike_id):

            ch_small, ch_big, cg_small, cg_big, ratio, num_gears = \
                w.extract_bike_stats(chainring_list[index], cog_list[index])

            print_bike_info(
                bike_id[index],
                ch_big, ch_small,
                cg_big, cg_small,
                ratio,
                num_gears
            )

            index = index + 1


def print_statistics(bike_id, chainring_list, cog_list):

    if len(bike_id) == 0:
        print("No statistics available.\n")
    else:

        ch_small, ch_big, cg_small, cg_big, ratio, num_gears = \
            w.extract_bike_stats(chainring_list[0], cog_list[0])

        best_climb_ratio = ratio
        best_climb_index = 0

        best_speed_ratio = ratio
        best_speed_index = 0

        index = 1
        while index < len(bike_id):

            stats = w.extract_bike_stats(chainring_list[index],
                                cog_list[index])

            curr_ratio = stats[4]   # ratio value

            if curr_ratio < best_climb_ratio:
                best_climb_ratio = curr_ratio
                best_climb_index = index

            if curr_ratio > best_speed_ratio:
                best_speed_ratio = curr_ratio
                best_speed_index = index

            index = index + 1

        print("\n--- Statistics ---")

        print("Bike with BEST climbing ratio (lowest):")
        print(f"  {bike_id[best_climb_index]}")
        print(f"  Ratio = {best_climb_ratio:.2f}\n")

        print("Bike with BEST top-speed ratio (highest):")
        print(f"  {bike_id[best_speed_index]}")
        print(f"  Ratio = {best_speed_ratio:.2f}\n")


main()

