# Rock, Paper, Scissors, game using python program

# impoting the requirements
import random

#intializing

game = ['Rock', 'Paper', 'Scissors']
pscore = 0
cscore = 0

exit = False

print('lets play Rock Paper Scissors....')
while True :
    player = input('Rock / Scissors / Paper :').capitalize()
    computer = random.choice(game)

# exit condition
    if player == 'Exit':   

        exit = True   
        print('\nFinal Score: ')        
        print(f'player score {pscore}')    
        print(f'computer score {cscore}')    
        if  pscore > cscore:
               print('\nYou Won !! congratulation') 

        elif cscore > pscore :
           print('Computer Won !! ')
        else:
               print('its a tie!!')
        break
    if  not exit :

     

    #main logic

     print(f'computer choose {computer}')
    if player == computer:
        print('Tie!')
    elif player == 'Rock' and computer =='Scissors':
        print("Player Won !!")
        pscore +=1
            
    elif player == 'Rock' and computer =='Paper':
            print("computer Won !!")
            cscore +=1
    elif player == 'Scissors' and computer =='Rock':
            print("Computer Won !!")
            cscore +=1  
    elif player == 'Scissors' and computer =='Paper':
           print("Player Won !!")
           pscore +=1
    elif player == 'Paper' and computer =='Scissors':
              print("computer Won !!")
              cscore +=1        
    elif player == 'Paper' and computer =='Rock':
                 print("player Won !!")
                 pscore +=1   
    
    else:
           print('invalid input')        
    print(f'\n player score {pscore}')    
    print(f'computer score {cscore}')                                                                          


    play_again = input('\n you want replay (yes/no):')
    if play_again not in['yes' , 'y']:
                  print('\n thank you enjoy game')
                  break 