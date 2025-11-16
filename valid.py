def get_integer(prompt):

    num = 0
    valid = False

    while valid != True:
        try:
            num = int(input(prompt))
            valid = True
        except:
            print("Invalid integer.")

    return num


def get_string(prompt):

    s = ""
    valid = False

    while valid != True:
        try:
            s = input(prompt)
            valid = True
        except:
            print("Invalid string")
    return s
