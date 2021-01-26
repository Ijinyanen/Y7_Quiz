
tries = 0
answer1 = input("Q1. What is the name of the ship that features in most Star Trek series?\n-> ").upper()
while answer1 != "ENTERPRISE":
    print("\nwrong.\n")
    tries = tries + 1
    print("you have had", tries, " tries.")
    answer1 = input("Q1. What is the name of the ship that features in most Star Trek series?\n-> ").upper()


print("correct")