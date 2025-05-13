import random
import sys
wins = 0
losses = 0
ties = 0
print('ROCK, PAPER, SCISSORS')
while True:
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input().lower()
        if player_move in ['r', 'p', 's', 'q']:
            break
        print("Invalid input. Please choose r, p, s, or q.")
    if player_move == 'q':
        print('Thanks for playing!')
        sys.exit()
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')
    moves = ['r', 'p', 's']
    computer_move = random.choice(moves)
    if computer_move == 'r':
        print('ROCK')
    elif computer_move == 'p':
        print('PAPER')
    elif computer_move == 's':
        print('SCISSORS')  
    if player_move == computer_move:
        print('It is a tie!')
        ties += 1
    elif (player_move == 'r' and computer_move == 's') or \
         (player_move == 'p' and computer_move == 'r') or \
         (player_move == 's' and computer_move == 'p'):
        print('You win!')
        wins += 1
    else:
        print('You lose!')
        losses += 1
