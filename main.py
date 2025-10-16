#******************************************************************************
# Author:           Brian O'Grady
# Assignment:       Assignment 01
# Date:             10/06/2025
# Description:      This program calculates the gear ratio by dividing the 
#                   number of teeth on the front chainring by the number
#                   of teeth on the rear cog.
# Revisions:        A01.1 - 09/06/2024 - Initialization, set up variables
#                           and initial function logic. Provide a printout of
#                           the variables.
#******************************************************************************
bike_id = ""
chainring = 0
cog = 0
gear_ratio = 0.0

print("Welcome to the bicycle gear ratio calculator!\n")

bike_id = input("Enter a unique bike ID: ")
chainring = int(input("Enter the number of teeth on the chainring: "))
cog = int(input("Enter the number of teeth on the cog: "))

gear_ratio = chainring / cog
print("\nBike ID - Chainring - Cog - Gear ratio")
print(f"{bike_id}   |   {chainring}   |   {cog}   |   {gear_ratio:.2f}")



print("\nThank you for using the gear ratio calculator!")