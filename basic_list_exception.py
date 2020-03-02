def main():
    my_list = make_list()

    for i in my_list:
        print(i)


def make_list():
    times = 0
    the_list = []

    while times < 3:
        try:
            list_input = get_input()
        except ValueError:
            print("Input not valid")
        else:
            the_list.append(float(list_input))
            times += 1

    return the_list


def get_input():
    try:
        user_input = input("Enter a number: ")
    except ValueError:
        print("Not valid input")
    else:
        while float(user_input) < 1 or float(user_input) > 50:
            print("Out of range")
            user_input = input("Enter a number: ")

    return float(user_input)




if __name__ == '__main__':
    main()