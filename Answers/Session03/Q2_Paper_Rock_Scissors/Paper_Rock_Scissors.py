import random
game=['Rock','Paper','Scissors']
while(True):
    player=input('Paper Scissors Rock \n' \
    'Player: ')
    print('----====----====----')
        
    computer=random.choice(game)

    if player.lstrip().upper() == 'ROCK' and computer == 'Paper':
        print('----====----====----')
        print(f'Computer: {computer}\n    Computer Win')
        print('----====----====----')
    elif player.lstrip().upper() == 'PAPER' and computer == 'Rock':
        print('----====----====----')
        print(f'Computer: {computer}')
        print('----====----====----')
        print('----====----====----')
        print('     Player Win')
        print('----====----====----')
    elif player.lstrip().upper() == 'SCISSORS' and computer == 'Rock':
        print('----====----====----')
        print(f'Computer: {computer}\n    Computer Win')
        print('----====----====----')
    elif player.lstrip().upper() == 'ROCK' and computer == 'Scissors':
        print(f'Computer: {computer}')
        print('----====----====----')
        print('     Player Win')
        print('----====----====----')
    elif player.lstrip().upper() == 'PAPER' and computer == 'Scissors':
        print('----====----====----')
        print(f'Computer: {computer}\n    Computer Win')
        print('----====----====----')
    elif player.lstrip().upper() == 'SCISSORS' and computer == 'Paper':
        print(f'Computer: {computer}')
        print('----====----====----')
        print('     Player Win')
        print('----====----====----')
    elif player.lstrip().upper() == 'EXIT':
        break
    elif  player.lstrip().upper() != 'ROCK' or player.lstrip().upper() != 'PAPER' or player.lstrip().upper() != 'SCISSORS':
        while player.lstrip().upper() != 'C':
          print('----====----====----')
          player=input('Paper Scissors Rock (Only)\n' \
          'press (C) : ')
          print('----====----====----')
          continue
    elif player.lstrip().upper() =='PAPER' and computer == 'Paper':
        print(f'Comupter: {computer}')
        print('No Winners')
    elif player.lstrip().upper() =='SCISSORS' and computer == 'Scissors':
        print(f'Computer: {computer}')
        print('No Winners')     
    elif player.lstrip().upper() =='ROCK' and computer == 'Rock':
        print(f'Computer: {computer}')
        print('No Winners')
