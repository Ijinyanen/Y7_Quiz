# challenge 1
print("\nWelcome to Mr Higgin's ultimate Star Trek Quiz!")
print("There will be 10 questions.")
print("You shalt be scored for each.\n\n")

# challenge 2
bucket = input("Please enter your first name. -> ")
surname = input("Please enter your surname. -> ")
age = input("Please enter your age. -> ")
print(bucket, surname, age)
print("\nWelcome to the Ulitmate Quiz, ", bucket, "\n")



# challeng 3/4
answer1 = input("Q1. What is the name of the ship that features in most Star Trek series?\n-> ").upper()
if answer1 == "ENTERPRISE":
    print("\ncorrect.\n")
else:
    print("\nwrong.\n")

#challenge 5
answer2 = input("\nQ2 What is the surname of the captain of the Entprise D?\n-> ").lower()
if answer2 == "picard":
    print("\nCorrect\n")
else:
    print("\nwrong\n")