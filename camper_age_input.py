"""
Program that converts age in years to age in months.
"""

def main():
    age_in_years = input("What is the age of the infant in years?\n")
    age_in_months = convert_to_months(age_in_years)
    print("Age in years converted to months: " + str(age_in_months))

def convert_to_months(age_in_years):
    NUMBER_OF_MONTHS_IN_YEAR = 12
    age_in_months = age_in_years * NUMBER_OF_MONTHS_IN_YEAR
    return age_in_months
    

if __name__ == '__main__':
    main()

#I am not going to lie... this was a really badly worded assignment. I don't
#know how other students are going to complete this without being utterly
#confused. I think this needs to be explained a lot better.
