import random

MOVES = ('rock', 'paper', 'scissors')
WIN = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

while True: 
    player = input('rock, paper, or scissors? ').strip().lower()
    
    if player not in MOVES:
        print(f'Invalid choice. Please try again with one of {MOVES}.')
        continue 

    computer = random.choice(MOVES)  
    print(f'Computer chose {computer}')

    if player == computer:
        print("Both players in a tie! Please play again.")
        continue  
    
    elif WIN[player] == computer:
        print("You win! Computer loses!") 
    else:
        print("You lose! Computer wins!")  
    
    break  