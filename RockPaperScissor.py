import random
player1 = input("Enter player 1:")
print(player1)
player2 = input("Enter player 2:")
print(player2)
'''
player1_choice = input("Enter your choice:rock,paper,scissor:")
print(player1_choice)

Li1 = ["rock","paper","scissor"]
player2_choice = random.choice(Li1)
print(player2_choice)
'''
user_score=0
system_score = 0
n = int(input("Enter how many times you want to play:"))
print(n)
for i in range(1,n+1):
    print("GAME-",i)
    player1_choice = input("Enter your choice:rock,paper,scissor:")
    #print(player1_choice)
    Li1 = ["rock","paper","scissor"]
    player2_choice = random.choice(Li1)
    #print(player2_choice)
    if player1_choice == player2_choice:
        print("Tie")
        user_score = user_score+1
        system_score = system_score+1
        print("Current User score is:",user_score)
        print("Current System score is:",system_score)
    elif player1_choice == "rock" and player2_choice == "scissor" :
            print("User wins!,"+str(player1_choice))
            user_score = user_score+1
            system_score = system_score+1
            print("Current User score is:",user_score)
    elif player1_choice == "scissor" and player2_choice == "paper":
            print("User wins!,"+str(player1_choice))
            user_score = user_score+1
            system_score = system_score+1
            print("Current User score is:",user_score)
    elif player1_choice == "paper" and player2_choice == "rock":
            print("User wins!,"+str(player1_choice))
            user_score = user_score+1
            system_score = system_score+1
            print("Current User score is:",user_score)
        
print("Total Number of Games:",i)
print("Total User Scores:",user_score)
print("Total System Score:",system_score)
if user_score > system_score:
    print("USER wins the game !!! Congrats !!!!")
else:
    print("System wins the game")
