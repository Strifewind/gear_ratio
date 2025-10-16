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
    print("Welcome to the bicycle gear ratio calculator!\n")


def get_bike_id():
    bike_id = input("Enter a unique bike ID: ")
    return bike_id


def get_chainring_teeth():
    chainring = int(input("Enter the number of teeth on the chainring: "))
    return chainring


def get_cog_teeth():
    cog = int(input("Enter the number of teeth on the cog: "))
    return cog


def calculate_gear_ratio(chainring, cog):
    gear_ratio = chainring / cog
    return gear_ratio


def print_bike_info(bike_id, chainring, cog, gear_ratio):
    print("\nBike ID - Chainring - Cog - Gear ratio")
    print(f"{bike_id}   |   {chainring}   |   {cog}   |   {gear_ratio:.2f}")


def print_outro():
    print("\nThank you for using the bicycle gear ratio calculator!")

main()