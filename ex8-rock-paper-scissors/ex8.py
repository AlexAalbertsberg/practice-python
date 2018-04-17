while(True):
    player_one_input = input("Make your choice (rock,paper,scissors): ")
    player_two_input = input("Make your choice (rock,paper,scissors): ")

    if(player_one_input == player_two_input):
        print("It's a draw!")
    elif(player_one_input == "rock"):
        if(player_two_input == "paper"):
            print("Player two wins!")
        elif(player_two_input == "scissors"):
            print("Player one wins!")
    elif(player_one_input == "scissors"):
        if(player_two_input == "paper"):
            print("Player one wins!")
        elif(player_two_input == "rock"):
            print("Player two wins!")
    elif(player_one_input == "paper"):
        if(player_two_input == "scissors"):
            print("Player two wins!")
        elif(player_two_input == "rock"):
            print("Player one wins!")

    keepPlaying = input("Press y to keep playing: ")
    if(keepPlaying != "y"):
        break
