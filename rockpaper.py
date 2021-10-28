#rock paper scissor using function

player1=input("Player 1, draw Your Choice:")
player2 = input("Player 2, draw Your Choice:")

def result(player1,player2):

        if player1 == player2:
            return ("Its a tie!!!")

        elif player1 == 'rock':
            if player2 == 'scissors':
                return ("Player 1 is the winner ")
            else:
                return ("Player 2 is the winner ")
        elif player1 == 'scissors':
            if player2 == 'paper':
                return ("Player 1 is the winner ")
            else:
                return ("Player 2 is the winner ")
        elif player1 == 'paper':
            if player2 == 'rock':
                return ("Player 1 is the winner ")
            else:
                return ("Player 2 is the winner ")




