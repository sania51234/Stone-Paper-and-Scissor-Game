import random

dict1 = {-1: "Stone", 0: "Paper", 1: "Scissor"}
dict2 = {"St": -1, "P": 0, "S": 1}




user_score = 0
computer_score = 0
rounds = int(input("How many rounds do you want to play? "))

for i in range(rounds):
    computer = random.choice([1, -1, 0])
    you = input("Enter your choice (St for Stone, P for Paper, S for Scissor): ")
    while you not in dict2:
        you = input("Invalid choice! Please enter again (St for Stone, P for Paper, S for Scissor): ")
    c = dict2[you]
    print(f"You chose: {dict1[c]}")
    print(f"Computer chose: {dict1[computer]}")
    # Game logic here, and update the scores based on who wins
    if (c == -1 and computer == 1) or (c == 0 and computer == -1) or (c == 1 and computer == 0):
        user_score += 1
        print("You Win!")
    else:
        computer_score += 1
        print("You Lose!")
print(f"Final Score - You: {user_score}, Computer: {computer_score}")

