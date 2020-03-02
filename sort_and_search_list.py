def main():
    the_list = [2, 1, 3, 0, 1]
    sorted_list = sort_list(the_list)

    print("Sorted list is: ")
    print(sorted_list)

    output = search_list(5, the_list)
    print(output)

def sort_list(the_list):
    the_list.sort()

    return the_list


def search_list(search_for, the_list):
    if search_for in the_list:
        the_string = "Found!"
    else:
        the_string = "Not found."

    return the_string
#Will return cause it is easier for testing.


if __name__ == '__main__':
    main()