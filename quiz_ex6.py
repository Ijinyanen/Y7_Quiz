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

# challeng 3/4/6
answer1 = input("Q1. What is the name of the ship that features in most Star Trek series?\n-> ").lower()

while answer1 != "enterprise":

    print("\nwrong\n")
    answer1 = input("Q1. What is the name of the ship that features in most Star Trek series?\n-> ").lower()
print("\ncorrect\n")

#challenge 5/6
answer2 = input("\nQ2 What is the surname of the captain of the Entprise D?\n-> ").lower()
while answer2 != "picard":
    print("\nwrong\n")
    answer2 = input("\nQ2 What is the surname of the captain of the Entprise D?\n-> ").lower()
print("\ncorrect\n")

answer3 = input("\nQ3 Complete the name of this Star Trek Series. 'Deep Space ____' .\n-> ").lower()
while answer3 != "9" or "nine":
    print("\nwrong\n")
    answer3 = input("\nQ3 Complete the name of this Star Trek Series. 'Deep Space ____' .\n-> ").lower()
print("\ncorrect\n")

answer4 = input("\nQ4 How many years is Entprise's mission in space in the Original Series?\n-> ").lower()
while answer4 != "5" or "five":
    print("\nwrong\n")
    answer4 = input("\nQ3 Complete the name of this Star Trek Series. 'Deep Space ____' .\n-> ").lower()
print("\ncorrect\n")

answer5 = input("\nQ5 What is the name of the Vulcan who features as first officer in the Original Series?\n-> ").lower()
while answer5 != "spock":
    print("\nwrong\n")
    answer5 = input("\nQ5 What is the name of the Vulcan who features as first officer in the Original Series?\n-> ").lower()
print("\ncorrect\n")

answer6 = input("\nQ6 Complete the title of this film. 'The wrath of ______'. \n-> ").lower()
while answer6 == "khan":
    print("\nwrong\n")
    answer6 = input("\nQ6 Complete the title of this film. 'The wrath of ______'. \n-> ").lower()
print("\ncorrect\n")

answer7 = input("\nQ7 How many seasons of The Next Generation are there? \n-> ").lower()
while answer7 == "7" or "seven":
    print("\nwrong\n")
    answer7 = input("\nQ7 How many seasons of The Next Generation are there? \n-> ").lower()
print("\ncorrect\n")

answer8 = input("\nQ8 what is the name of the ship that is stranded in the Gramma Quadrant with its own series? \n-> ").lower()
while answer8 == "voyager":
    print("\nwrong\n")
    answer8 = input("\nQ8 what is the name of the ship that is stranded in the Gramma Quadrant with its own series? \n-> ").lower()
print("\ncorrect\n")

answer9 = input("\nQ9 Give the surname of the female captain who gets her own series of Star Trek starting in 1995? \n-> ").lower()
while answer9 == "janeway":
    print("\nwrong\n")
    answer9 = input("\nQ9 Give the surname of the female captain who gets her own series of Star Trek starting in 1995? \n-> ").lower()
print("\ncorrect\n")

answer10 = input("\nQ10 What is the name of the litte ship that is assigned to Sisko's space station? \n-> ").lower()
while answer10 == "defiant":
    print("\nwrong\n")
    answer10 = input("\nQ10 What is the name of the litte ship that is assigned to Sisko's space station? \n-> ").lower()
print("\ncorrect\n")