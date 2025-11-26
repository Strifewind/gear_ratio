def insert_sorted(s, value):
    """
    Insert a value into a list while keeping it sorted (ascending).
    Uses only while loops, no built-in sorting.
    """
    i = 0
    while i < len(s) and s[i] < value:
        i += 1
    s.insert(i, value)


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


def extract_bike_stats(chainrings, cogs):
    """
    Returns (ch_small, ch_big, cg_small, cg_big, ratio, num_gears)
    NO dictionaries.
    """

    ch_small = chainrings[0]
    ch_big   = chainrings[-1]

    cg_small = cogs[0]
    cg_big   = cogs[-1]

    ratio = calculate_gear_ratio(ch_big, cg_small)
    num_gears = calculate_num_gear(len(chainrings), len(cogs))

    return ch_small, ch_big, cg_small, cg_big, ratio, num_gears
