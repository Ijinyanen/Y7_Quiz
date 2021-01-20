# challenge 1
print("\nWelcome to Mr Higgin's ultimate Star Trek Quiz!")
print("There will be 10 questions.")
print("You shall be scored for each.\n\n")

# challenge 2
name = input("Please enter your first name. -> ")
surname = input("Please enter your surname. -> ")
age = input("Please enter your age. -> ")
print(" ",name, "   ", surname, "   ", age)
print("\nWelcome to the Ulitmate Quiz, ", name, "\n")

# challeng 3/4
answer1 = input("Q1. What is the name of the ship that features in most Star Trek series?\n-> ").lower()
if answer1 == "enterprise":
    print("\ncorrect.\n")
else:
    print("\nwrong.\n")

#challenge 5
answer2 = input("\nQ2 What is the surname of the captain onf the Entprise D?\n-> ").lower()
if answer2 == "picard":
    print("\nCorrect\n")
else:
    print("\nwrong\n")

answer3 = input("\nQ3 Complete the name of this Star Trek Series. 'Deep Space ____' .\n-> ").lower()
if answer3 == "9" or "nine":
    print("\nCorrect\n")
else:
    print("\nwrong\n")

answer4 = input("\nQ4 How many years is Entprise mission in space in the Original Series?\n-> ").lower()
if answer4 == "5" or "five":
    print("\nCorrect\n")
else:
    print("\nwrong\n")

answer5 = input("\nQ5 What is the name of the Vulcan who features as first officer in the Original Series?\n-> ").lower()
if answer5 == "spock":
    print("\nCorrect\n")
else:
    print("\nwrong\n")

answer6 = input("\nQ6 Complete the title of this film. 'The wrath of ______'. \n-> ").lower()
if answer6 == "khan":
    print("\nCorrect\n")
else:
    print("\nwrong\n")

answer7 = input("\nQ7 How many seasons of The Next Generation are there? \n-> ").lower()
if answer7 == "7" or "seven":
    print("\nCorrect\n")
else:
    print("\nwrong\n")

answer8 = input("\nQ8 what is the name of the ship that is stranded in the Gramma Quadrant with its own series? \n-> ").lower()
if answer8 == "voyager":
    print("\nCorrect\n")
else:
    print("\nwrong\n")

answer9 = input("\nQ9 Give the surname of the female captain who gets her own series of Star Trek starting in 1995? \n-> ").lower()
if answer9 == "janeway":
    print("\nCorrect\n")
else:
    print("\nwrong\n")

answer10 = input("\nQ10 What is the name of the litte ship that is assigned to Sisko's space station? \n-> ").lower()
if answer10 == "defiant":
    print("\nCorrect\n")
else:
    print("\nwrong\n")