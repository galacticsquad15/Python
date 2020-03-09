def main():
    my_output = switch_average('A')
    print(my_output)


def switch_average(value):
    the_case = {
        'A' : 1,
        'B' : 2,
        'C' : 3,
        'D' : 4,
        'E' : 5,
    }

    the_output = the_case.get(value, "Invalid entry")

    return the_output


if __name__ == '__main__':
    main()