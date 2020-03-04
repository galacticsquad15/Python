"""Create a project Module 8 and directories more_fun_with_collections and test.

Create a file test_set_membership.py, a unit test in test.
Create a file set_membership.py in more_fun_with_collections.
In set_membership.py
declare an unimplemented function in_set. This will eventually accept a set and
return a boolean value stating if the element is in the set. First, it contains pass only.
In test_set_membership.py,
Write a test test_in_set_true
assertion for an item in the set (expect True)
Write a test test_in_set_false
One assertion for an item not in the set (expect False)
Run the test, see it fail, commit to github
Write the in_set function.
Run the test, see it pass, commit to github."""

def main():
    my_set = {1, 2, 3, 4, 5}
    is_in = in_set(1, my_set)
    print(is_in)


def in_set(looking_for, the_set):
    for i in the_set:
        if i == looking_for:
            the_truth = True
            break
        else:
            the_truth = False

    return the_truth

if __name__ == '__main__':
    main()