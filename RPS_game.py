player1=input("Player 1, draw Your Choice:")
player2 = input("Player 2, draw Your Choice:")

def compare(player1, player2):
    if player1 == player2:
        return("It's a tie!")
    elif player1 == 'rock':
        if player2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif player1 == 'scissors':
        if player2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif player1 == 'paper':
        if player2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(player1, player2))
