def check_row_victory():
    for i in range(3):
        if(game[i][0] == game[i][1] and game[i][0] == game[i][2] and (game[i][0] == 1 or game[i][0] == 2)):
            return game[i][0]
    return None

def check_column_victory():
    for i in range(3):
        if(game[0][i] == game[1][i] and game[0][i] == game[2][i] and (game[0][i] == 1 or game[0][i] == 2)):
            return game[0][i]
    return None

def check_diagonal_victory():
    if(game[0][0] == game[1][1] and game[0][0] == game[2][2] and (game[0][0] == 1 or game[0][0] == 2)):
        return game[0][0]
    elif(game[0][2] == game[1][1] and game[0][2] == game[2][0] and (game[0][0] == 1 or game[0][0] == 2)):
        return game[0][2]

game = [[2,2,0],
[2,1,0],
[2,1,1]]
print("Row victory achieved by player: " + str(check_row_victory()))
print("Column victory achieved by player: " + str(check_column_victory()))
print("Diagonal victory achieved by player: " + str(check_diagonal_victory()))
