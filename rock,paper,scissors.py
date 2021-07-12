import random
player_1_mist = 0
player_2_mist = 0
l = ["rock", "scissor", "paper"]

while player_1_mist<3 and player_2_mist<3:
    player_1 = str(input('Player 1: rock, scissor or paper?'))



    if player_1 not in l:
        print("\nPlayer 1 entered an invalid word:",player_1+".","Please write rock, scissor or paper!\n")
        continue

    player_2=random.choice(l)
    print('Player 2: rock, scissor or paper?'+player_2)
    if player_1 not in l:
        print("\nPlayer 1 entered an invalid word. Please write rock, scissor or paper!\n")

    elif player_1 == player_2:
         print("\nIt's a tie!\n")

    elif player_1 == "rock" and player_2 == "scissor":
        player_2_mist += 1
        print("\nPlayer 1 wins!\n")
        print("Scor:\nPlayer 1:", player_1_mist,"\nPlayer 2:",player_2_mist,"\n")

    elif player_1 == "scissor" and player_2 == "rock":
        player_1_mist += 1
        print("\nPlayer 2 wins!\n")
        print("Scor:\nPlayer 1:", player_1_mist,"\nPlayer 2:",player_2_mist,"\n")

    elif player_1 == "paper" and player_2 == "rock":
        player_2_mist += 1
        print("\nPlayer 1 wins!\n")
        print("Scor:\nPlayer 1:", player_1_mist,"\nPlayer 2:",player_2_mist,"\n")

    elif player_1 == "rock" and player_2 == "paper":
        player_1_mist += 1
        print("\nPlayer 2 wins!\n")
        print("Scor:\nPlayer 1:", player_1_mist,"\nPlayer 2:",player_2_mist,"\n")

    elif player_1 == "scissor" and player_2 == "paper":
        player_2_mist += 1
        print("\nPlayer 1 wins!\n")
        print("Scor:\nPlayer 1:", player_1_mist,"\nPlayer 2:",player_2_mist,"\n")

    elif player_1 == "paper" and player_2 == "scissor":
        player_1_mist += 1
        print("\nPlayer 2 wins!\n")
        print("Scor:\nPlayer 1:", player_1_mist,"\nPlayer 2:",player_2_mist,"\n")


else:
        if player_1_mist ==3:
            print("\nGame over. Player 2 win!")

        elif player_2_mist ==3:
            print("\nGame over. Player 1 win!")
