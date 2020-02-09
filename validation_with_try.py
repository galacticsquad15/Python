"""
Creating function to prompt user to enter information and get their average test score
"""


def main():
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    user_age = input("Please enter your age: ")
    average_scores = average()
    print(last_name + ", " + first_name + " Age: " + user_age + " Average Grade: %.2f" % average_scores)


def average(first_input, second_input, third_input):
    scores_average = (first_input + second_input + third_input) / 3
    return scores_average


if __name__ == '__main__':
    main()

"""
See test_average_scores for various input tests.
"""