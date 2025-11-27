def get_integer(prompt):
    """
    This function gets a valid integer from the user.
    :param prompt: A message to show the user when asking for an integer.
    :return: The valid integer entered by the user.
    """
    num = 0
    valid = False

    while not valid:
        try:
            num = int(input(prompt))
            while num < 0:
                print("Invalid integer. Please enter an integer.")
                num = int(input(prompt))
            valid = True
        except ValueError:
            print("Invalid integer.")

    return num


def get_string(prompt):
    """
    This function gets a valid non-empty string from the user.
    :param prompt: A message to show the user when asking for a string.
    :return: The valid string entered by the user.
    """
    strand = ""
    valid = False

    while not valid:
        strand = input(prompt)
        if strand == "":
            print("Invalid string. Please enter a string.")
        else:
            valid = True

    return strand
