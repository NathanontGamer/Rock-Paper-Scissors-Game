def rps ():
    import random
    totalScore = 0
    print("This is Rock Paper Scissors Game for lonely people ㅠㅠ")
    print("Rock = 1")
    print("Paper = 2")
    print("Scissors = 3")
    n = int(input("How many game do you want to play?\n"))
    for i in range(n):
        rps_random = random.randint(1, 3)
        choice = int(input("What do you choose?\n"))
        if choice == rps_random:
            totalScore = totalScore + 1
            print("You Win!")
        elif choice != rps_random:
            print("You lose!")
        else:
            print("Error!")
    print("Your score is", totalScore)

rps ()