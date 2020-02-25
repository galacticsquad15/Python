def main():
    testMessage = score_input('Python Test', int(101))
    print(testMessage)


def score_input(test_name, test_score = 0, invalid_message = 'Invalid test score, try again!'):
    """
    This will be prompting a user to enter a test score in a specified range until they do so. It will
    then print out the test score.
    :param test_name: Name of the test
    :param test_score: Between 0 and 100
    :param invalid_message: Defaults to invalid test score, try again.
    :return: Will print out test message
    """

    testScore = str(test_score)

    if test_score > 100 or test_score < 0 or testScore.isalpha():
        message = invalid_message
    else:
        message = test_name + ': ' + testScore

    return message


if __name__ == '__main__':
    main()