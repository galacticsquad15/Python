import array as arr


def main():
    my_array = arr.array('I', [3, 2, 1])
    sorted_list = sort_array(my_array)

    print("Sorted list is: ")
    print(sorted_list)

    output = search_array(5, my_array)
    print(output)


def sort_array(the_array):
    a_list = the_array.tolist()
    a_list.sort()

    return a_list


def search_array(search_for, the_array):
    new_list = the_array.tolist()

    if search_for in new_list:
        statement = "Found!"
    else:
        statement = "Not found."

    return statement


if __name__ == '__main__':
    main()