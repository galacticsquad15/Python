"""
Creating function to prompt user to enter information and get their average test score
"""


def main():
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    user_age = input("Please enter your age: ")
    first_input = float(input("Enter score 1: "))

    while first_input < 0:
        first_input = float(input("Enter score 1: "))

    second_input = float(input("Enter score 2: "))

    while second_input < 0:
        second_input = float(input("Enter score 2: "))

    third_input = float(input("Enter score 3: "))

    while third_input < 0:
        third_input = float(input("Enter score 3: "))

    average_scores = average(first_input, second_input, third_input)
    print(last_name + ", " + first_name + " Age: " + user_age + " Average Grade: %.2f" % average_scores)


def average(first_input, second_input, third_input):
    try:
        if first_input < 0 or second_input < 0 or third_input < 0:
            raise ValueError
    except ValueError:
        print("Negative number entered for one of the values.")
    scores_average = (first_input + second_input + third_input) / 3
    return scores_average


if __name__ == '__main__':
    main()

"""
See test_validation_with_try for various input tests.
"""