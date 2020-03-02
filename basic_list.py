def main():
    my_list = make_list()

    for i in my_list:
        print(i)


def make_list():
    times = 0
    the_list = []

    while times < 3:
        list_input = get_input()
        the_list.append(float(list_input))
        times += 1

    return the_list


def get_input():
    user_input = input("Enter a number: ")

    while not user_input.isnumeric():
        user_input = input("Enter a number: ")

    final = float(user_input)

    return final




if __name__ == '__main__':
    main()