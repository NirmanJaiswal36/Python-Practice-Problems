#007. Rock_Paper_Scissors
#Source:https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
'''Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)'''
import sys

new_game = 'Yes'
win = ['RockScissors','PaperRock','ScissorsPaper']
lose= ['RockPaper','PaperScissors','ScissorsRock']
x = input('What is your name?:')
y = input('And yours?')

while new_game == 'Yes':
    p1 = input('Dear '+ x + ', \n Enter Rock, Paper, or Scissors:')
    p2 = input('Dear '+ y + ', \n Enter Rock, Paper, or Scissors:')
    combination = p1 + p2
    if combination in win:
        print('Congratulations! '+ x +', you have won the game')
    elif combination in lose:
        print('Congratulations! '+ y +', you have won the game')
    elif p1==p2:
        print('It is a tie.')
    else:
        print('Invalid Input, you have not typed Rock, Paper, or Scissors. Please try again')
        sys.exit()
        

    new_game = input('Do you want to start a new game(Yes/No):')    
