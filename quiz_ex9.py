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

# challeng 3/4/6/7
tries = 0
answer1 = input("Q1. What is the name of the ship that features in most Star Trek series?\n-> ").lower()
tries = tries + 1 
while answer1 != "enterprise" and tries < 3:
    print("\nwrong")
    if tries == 1:
        print("You have had 1 try.\n")
    else:
        print("You have had ", tries, " tries.\n")
    answer1 = input("Q1. What is the name of the ship that features in most Star Trek series?\n-> ").lower()
    tries = tries + 1
print("\ncorrect\n")

#challenge 5/6/7
tries = 0
answer2 = input("\nQ2 What is the surname of the captain of the Entprise D?\n-> ").lower()
tries = tries + 1
while answer2 != "picard" and tries < 3:
    print("\nwrong")
    if tries == 1:
        print("You have had 1 try.\n")
    else:   
        print("You have had ", tries, " tries.\n")
    answer2 = input("\nQ2 What is the surname of the captain of the Entprise D?\n-> ").lower()
    tries = tries + 1

if answer2 == "picard":
    print("\ncorrect\n")
else:
    print("You have had ", tries, " tries.")
    print("The answer was Picard.")

tries = 0
answer3 = input("\nQ3 Complete the name of this Star Trek Series. 'Deep Space ____' .\n-> ").lower()
tries =  tries + 1
while answer3 != "9" and answer3 != "nine" and tries <3:
    print("\nwrong")
    if tries == 1:
        print("You have had 1 try.\n")
    else:
        print("you have had ", tries, " tries.\n")
    answer3 = input("\nQ3 Complete the name of this Star Trek Series. 'Deep Space ____' .\n-> ").lower()
    tries = tries + 1
print("\ncorrect\n")

tries = 0
answer4 = input("\nQ4 How many years is Entprise's mission in space in the Original Series?\n-> ").lower()
tries = tries + 1
while answer4 != "5" and answer4 != "five" and tries < 3:
    print("\nwrong")
    if tries == 1:
        print("You have had 1 try.\n")
    else:
        print("You have had ", tries, " tries.\n")
    answer4 = input("\nQ3 Complete the name of this Star Trek Series. 'Deep Space ____' .\n-> ").lower()
    tries = tries + 1
print("\ncorrect\n")

tries = 0
answer5 = input("\nQ5 What is the name of the Vulcan who features as first officer in the Original Series?\n-> ").lower()
tries = tries + 1
while answer5 != "spock" and tries < 3:
    print("\nwrong")
    if tries ==1:
        print("You have had 1 try. \n")
    else:
        print("You have had ", tries, " tries.\n")
    answer5 = input("\nQ5 What is the name of the Vulcan who features as first officer in the Original Series?\n-> ").lower()
    tries = tries + 1
print("\ncorrect\n")

tries = 0
answer6 = input("\nQ6 Complete the title of this film. 'The wrath of ______'. \n-> ").lower()
tries = tries + 1
while answer6 != "khan" and tries < 3:
    print("\nwrong")
    if tries == 1:
        print("You have had 1 try.\n")
    else:
        print("you have had ", tries, " tries.\n")  
    answer6 = input("\nQ6 Complete the title of this film. 'The wrath of ______'. \n-> ").lower()
    tries = tries + 1  
print("\ncorrect\n")

tries = 0
answer7 = input("\nQ7 How many seasons of The Next Generation are there? \n-> ").lower()
tries = tries + 1
while answer7 != "7" and answer7 != "seven" and tries < 3:
    print("\nwrong")
    if tries ==1:
        print("You have had 1 try.\n")
    else:
        print("you have had ", tries, " tries.\n")
    answer7 = input("\nQ7 How many seasons of The Next Generation are there? \n-> ").lower()
    tries = tries + 1
print("\ncorrect\n")

tries = 0
answer8 = input("\nQ8 what is the name of the ship that is stranded in the Gramma Quadrant with its own series? \n-> ").lower()
tries = tries + 1
while answer8 != "voyager" and tries < 3:
    print("\nwrong")
    if tries == 1:
        print("You have had 1 try.\n")
    else:
        print("You have had ", tries, " tries.\n")
    answer8 = input("\nQ8 what is the name of the ship that is stranded in the Gramma Quadrant with its own series? \n-> ").lower()
    tries = tries + 1
print("\ncorrect\n")

tries = 0
answer9 = input("\nQ9 Give the surname of the female captain who gets her own series of Star Trek starting in 1995? \n-> ").lower()
tries = tries + 1
while answer9 != "janeway" and tries < 3:
    print("\nwrong")
    if tries == 1:
        print("You have had 1 try.\n")
    else:
        print("You have had ", tries, " tries.\n")
    answer9 = input("\nQ9 Give the surname of the female captain who gets her own series of Star Trek starting in 1995? \n-> ").lower()
    tries = tries + 1
print("\ncorrect\n")

tries = 0
answer10 = input("\nQ10 What is the name of the litte ship that is assigned to Sisko's space station? \n-> ").lower()
tries = tries + 1
while answer10 != "defiant" and tries < 3:
    print("\nwrong")
    if tries == 1:
        print("You have had 1 try.\n")
    else:
        print("You have had ", tries, " tries.\n")
    answer10 = input("\nQ10 What is the name of the litte ship that is assigned to Sisko's space station? \n-> ").lower()
    tries = tries + 1
print("\ncorrect\n")