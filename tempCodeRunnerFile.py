         computerMove = 'SCISSORS'
     print(computerMove)
     time.sleep(0.5)
 
     # Display and record the win/loss/tie:
     if playerMove == computerMove:
         print('It\'s a tie!')
         ties = ties + 1
     elif playerMove == 'ROCK' and computerMove == 'SCISSORS':
         print('You win!')
         wins = wins + 1
     elif playerMove == 'PAPER' and computerMove == 'ROCK':
         print('You win!')
         wins = wins + 1
     elif playerMove == 'SCISSORS' and computerMove == 'PAPER':
         print('You win!')
         wins = wins + 1
     elif playerMove == 'ROCK' and computerMove == 'PAPER':