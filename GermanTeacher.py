import datetime
import time
import tkinter


class OutputPoints:
    def __init__(self, point_total):
        self.total_points = point_total

    def __str__(self):
        return self.display()

    def __repr__(self):
        return self.display()

    def display(self):
        print("\nCalculating results...")
        time.sleep(2)

        if self.total_points == 5:
            output_message = "5 out of 5! Great job!"
        elif 0 > self.total_points > 5:
            output_message = str(self.total_points) + " out of 5. Not bad! Keep working for that perfect score!"
        else:
            output_message = str(self.total_points) + " out of 5. It's alright! Keep practicing!"

        return output_message


def check_username_input(username):
    while len(username) < 1 or not username.isalpha():
        print("Enter a name with no spaces, letters, or special characters.")
        username = input("What is your name?\n")

    return username


def prompt_user_for_single_word_or_phrase_learning():
    user_input = input("Would you like to learn some single words or phrases? Press 1 for single words or 2 for phrases.\n")

    while int(user_input) != 1 and int(user_input) != 2:
        user_input = input("Try again.\n")

    return user_input


def teach_german(section):
    if section == 1:
        teach_single_words()
    elif section == 2:
        teach_phrases()
    else:
        pass


def teach_single_words():
    try:
        print("Here are some words that can help you navigate the German language terrain.")
        print("\nBitte - means many things actually, like PARDON, PLEASE, YOU'RE WELCOME.")
        print("Hallo - you could probably guess what this means! It means HELLO.")
        print("Wasser (sounds like Vasser) - WATER.")
        print("Brot - BREAD.")
        print("Mann - MAN.")
        print("Frau - WOMAN")
        print("Tschüss (the 'tsch' are pronounced like the 'ch' in the beginning of cheese) - BYE")
        print("Danke - THANKS.")
        print("\nPlease take your time learning these words. Don't worry if you forget, you can always come back later!")
        exit_single_words = input("Just press 1 when you want to leave.\n")

        while int(exit_single_words) != 1:
            exit_single_words = input("Try pressing 1 to leave.\n")
    except:
        print("Leaving words section.")

    return


def teach_phrases():
    try:
        print("Here are some phrases that can help you navigate the German language terrain.")
        print("\nGuten Morgen - GOOD MORNING.")
        print("Guten Tag - GOOD AFTERNOON.")
        print("Guten Abend - GOOD EVENING.")
        print("Gute Nacht (notice there is no 'n' at the end of Gute) - GOOD NIGHT.")
        print("Bis Spaeter - SEE YOU LATER.")
        print("Es Tut Mir Leid - I AM SORRY")
        print("\nPlease take your time learning these phrases. Don't worry if you forget, you can always come back later!")
        exit_phrases = input("Just press 1 when you want to leave.\n")

        while int(exit_phrases) != 1:
            exit_phrases = input("Try pressing 1 to leave.\n")
    except:
        print("Leaving phrases section.")

    return


def check_to_learn_again(argument):
    switcher = {
        1: '1'
    }

    return switcher.get(argument, "On to the test!")


def check_answer(label):
    global totalPoints
    global questionOneGuessCount
    global questionTwoGuessCount
    global questionThreeGuessCount
    global questionFourGuessCount
    global questionFiveGuessCount

    if label == questionOneLabel.cget("text"):
        if questionOneGuessCount == 0:
            if var1.get() == 1:
                bottomLabel.config(text="Correct!")
                totalPoints += 1
                questionOneGuessCount += 1
            else:
                bottomLabel.config(text="Incorrect. BITTE was the right answer.")
                questionOneGuessCount += 1
    elif label == questionTwoLabel.cget("text"):
        if questionTwoGuessCount == 0:
            if var6.get() == 1:
                bottomLabel.config(text="Good!")
                totalPoints += 1
                questionTwoGuessCount += 1
            else:
                bottomLabel.config(text="Incorrect. BITTE was the right answer.")
                questionTwoGuessCount += 1
    elif label == questionThreeLabel.cget("text"):
        if questionThreeGuessCount == 0:
            if var12.get() == 1:
                bottomLabel.config(text="Fantastic Answer!")
                totalPoints += 1
                questionThreeGuessCount += 1
            else:
                bottomLabel.config(text="Incorrect. FRAU was the right answer.")
                questionThreeGuessCount += 1
    elif label == questionFourLabel.cget("text"):
        if questionFourGuessCount == 0:
            if var14.get() == 1:
                bottomLabel.config(text="Correctamundo!")
                totalPoints += 1
                questionFourGuessCount += 1
            else:
                bottomLabel.config(text="Incorrect. GUTEN ABEND was the right answer.")
                questionFourGuessCount +=1
    else:
        if questionFiveGuessCount == 0:
            if var17.get() == 1:
                bottomLabel.config(text="Nice! Correct!")
                totalPoints += 1
                questionFiveGuessCount += 1
            else:
                bottomLabel.config(text="Incorrect. ES TUT MIR LEID was the right answer.")
                questionFiveGuessCount += 1


if __name__ == '__main__':
    print("Welcome to the Basic German Learning Program.")

    time.sleep(2)
    userFirstName = input("What is your first name?\n")

    officialName = check_username_input(userFirstName)

    print("\nWelcome " + officialName + ". Hope you are ready to learn some basic German!")
    print("Here is what is going to happen. We will be teaching you some basic German words and phrases.")
    print("Once you reach the end of the teaching section, we will throw a test at you to see if you were paying attention.")
    print("Easy enough, right? Let's start!\n")

    time.sleep(10)

    learningSectionInput = int(prompt_user_for_single_word_or_phrase_learning())
    print("\n")
    teach_german(learningSectionInput)

    try:
        learnAgain = input("Press 1 to go over the material again. Press anything else to continue to the test. "
                           "Caution! \nThe test contains content on words AND phrases. If you haven't gone through"
                           "both, you may want to do that before advancing.\n")
        choiceToLearnAgain = check_to_learn_again(int(learnAgain))

        while choiceToLearnAgain == '1':
            learningSectionInput = int(prompt_user_for_single_word_or_phrase_learning())
            print("\n")
            teach_german(learningSectionInput)
            learnAgain = input("Press 1 to go over the material again. Press anything else to continue to the test.")
            choiceToLearnAgain = check_to_learn_again(int(learnAgain))
    except:
        print("Looks like you didn't press 1. Going to proceed to test.\n")

    print("Quiz will open in a separate window. Maximize the window if possible.")
    print("Your first guess will be the one recorded.")
    print("Press the exit button whenever you want.")

    totalPoints = 0 #this will keep score of the quiz
    questionOneGuessCount = 0 #these will keep track of the guess count for each question
    questionTwoGuessCount = 0
    questionThreeGuessCount = 0
    questionFourGuessCount = 0
    questionFiveGuessCount = 0

    m = tkinter.Tk()  # where m is the name of the main window object
    m.title('German Quiz  ' + str(datetime.datetime.now()))
    questionOneLabel = tkinter.Label(m, text="Which word means 'Pardon'?")
    questionOneLabel.grid(row=0)
    bottomLabel = tkinter.Label(m, text="")
    bottomLabel.grid(row=29)

    var1 = tkinter.IntVar()
    checkButton1 = tkinter.Checkbutton(m, text="BITTE", variable=var1,
                                       command=lambda: check_answer(questionOneLabel.cget("text"))).grid(row=1)
    var2 = tkinter.IntVar()
    checkButton2 = tkinter.Checkbutton(m, text="WILKOMMEN", variable=var2,
                                       command=lambda: check_answer(questionOneLabel.cget("text"))).grid(row=2)
    var3 = tkinter.IntVar()
    checkButton3 = tkinter.Checkbutton(m, text="TSCHUSS", variable=var3,
                                       command=lambda: check_answer(questionOneLabel.cget("text"))).grid(row=3)
    var4 = tkinter.IntVar()
    checkButton4 = tkinter.Checkbutton(m, text="MANN", variable=var4,
                                       command=lambda: check_answer(questionOneLabel.cget("text"))).grid(row=4)

    questionTwoLabel = tkinter.Label(m, text="Which word means 'Please'?")
    questionTwoLabel.grid(row=6)
    var5 = tkinter.IntVar()
    checkButton5 = tkinter.Checkbutton(m, text="TSCHUSS", variable=var5,
                                       command=lambda : check_answer(questionTwoLabel.cget("text"))).grid(row=7)
    var6 = tkinter.IntVar()
    checkButton6 = tkinter.Checkbutton(m, text="BITTE", variable=var6,
                                       command=lambda : check_answer(questionTwoLabel.cget("text"))).grid(row=8)
    var7 = tkinter.IntVar()
    checkButton7 = tkinter.Checkbutton(m, text="BROT", variable=var7,
                                       command=lambda : check_answer(questionTwoLabel.cget("text"))).grid(row=9)
    var8 = tkinter.IntVar()
    checkButton8 = tkinter.Checkbutton(m, text="DANKE", variable=var8,
                                       command=lambda : check_answer(questionTwoLabel.cget("text"))).grid(row=10)

    questionThreeLabel = tkinter.Label(m, text="Which word means 'Woman'?")
    questionThreeLabel.grid(row=12)
    var9 = tkinter.IntVar()
    checkButton9 = tkinter.Checkbutton(m, text="MANN", variable=var9,
                                       command=lambda: check_answer(questionThreeLabel.cget("text"))).grid(row=13)
    var10 = tkinter.IntVar()
    checkButton10 = tkinter.Checkbutton(m, text="FRAUEN", variable=var10,
                                       command=lambda: check_answer(questionThreeLabel.cget("text"))).grid(row=14)
    var11 = tkinter.IntVar()
    checkButton11 = tkinter.Checkbutton(m, text="WASSER", variable=var11,
                                       command=lambda: check_answer(questionThreeLabel.cget("text"))).grid(row=15)
    var12 = tkinter.IntVar()
    checkButton12 = tkinter.Checkbutton(m, text="FRAU", variable=var12,
                                       command=lambda: check_answer(questionThreeLabel.cget("text"))).grid(row=16)

    questionFourLabel = tkinter.Label(m, text="Which phrase means 'Good Evening'?")
    questionFourLabel.grid(row=18)
    var13 = tkinter.IntVar()
    checkButton13 = tkinter.Checkbutton(m, text="GUTE NACHT", variable=var13,
                                       command=lambda: check_answer(questionFourLabel.cget("text"))).grid(row=19)
    var14 = tkinter.IntVar()
    checkButton14 = tkinter.Checkbutton(m, text="GUTEN ABEND", variable=var14,
                                        command=lambda: check_answer(questionFourLabel.cget("text"))).grid(row=20)
    var15 = tkinter.IntVar()
    checkButton15 = tkinter.Checkbutton(m, text="GUTEN MORGEN", variable=var15,
                                        command=lambda: check_answer(questionFourLabel.cget("text"))).grid(row=21)
    var16 = tkinter.IntVar()
    checkButton16 = tkinter.Checkbutton(m, text="ES TUT MIR LEID", variable=var16,
                                        command=lambda: check_answer(questionFourLabel.cget("text"))).grid(row=22)

    questionFiveLabel = tkinter.Label(m, text="Which phrase means 'I am sorry'?")
    questionFiveLabel.grid(row=24)
    var17 = tkinter.IntVar()
    checkButton17 = tkinter.Checkbutton(m, text="ES TUT MIR LEID", variable=var17,
                                        command=lambda: check_answer(questionFiveLabel.cget("text"))).grid(row=25)
    var18 = tkinter.IntVar()
    checkButton18 = tkinter.Checkbutton(m, text="GUTEN ABEND", variable=var18,
                                        command=lambda: check_answer(questionFiveLabel.cget("text"))).grid(row=26)
    var19 = tkinter.IntVar()
    checkButton19 = tkinter.Checkbutton(m, text="GUTEN MORGEN", variable=var19,
                                        command=lambda: check_answer(questionFiveLabel.cget("text"))).grid(row=27)
    var20 = tkinter.IntVar()
    checkButton20 = tkinter.Checkbutton(m, text="BIS BALD", variable=var20,
                                        command=lambda: check_answer(questionFiveLabel.cget("text"))).grid(row=28)

    exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
    exit_button.grid(row=30)

    m.mainloop()

    totalPointsFromQuiz = OutputPoints(totalPoints)
    print(totalPointsFromQuiz.display())

    print("Hope you had fun learning some German. Don't be afraid to come back and learn some more.")