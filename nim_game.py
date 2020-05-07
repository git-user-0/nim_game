import time
import random

def comp_wins():
    ## called when the computer wins
    print()
    time.sleep(1)
    print('I was the first to reach 0. I win.')

def player_choice(number):
    # the game will continue according to pre-defined rules until the number is 0 or less than 0
    # at this point, the computer will definitely have won because of the rules of the game
    while number > 0:
        time.sleep(1)
        print()
        print('Enter the number which you would like to subtract. 1 or 2. ')
        choice = int(input())
        # the rules now are simple - if the player subtracts 1, the computer subtracts 2
        # and if the player subtracts 1, the computer subtracts 2
        # this will always result in the computer winning - artificial intelligence!
        if choice == 1:
            number-=1
            time.sleep(1)
            print()
            print('You have subtracted 1. The number is now:')
            print()
            print(number)
            time.sleep(1)
            number -=2
            print()
            print('I have subtracted 2. The number is now:')
            print()
            print(number)
        elif choice == 2:
            number -=2
            time.sleep(1)
            print()
            print('You have subtracted 2. The number is now:')
            print()
            print(number)
            time.sleep(1)
            number -=1
            print()
            print('I have subtracted 1. The number is now:')
            print()
            print(number)
        else:
            print('The number you subtract must be 1 or 2.')
    comp_wins()

# main            
play_again = 'y'
number = 0
while play_again.lower().startswith('y') == True:
    time.sleep(1)
    print('Choose a start number which is greater than 6. ')
    number = int(input())
    if number>6:
        # if the start number is divisible by 3, the player must go first in order for the computer to win
        # so we call player_choice to let the player go first
        if number%3==0:
            player_choice(number)
        else:
            # if the chosen start number is not divisible by 3, but it leaves a remainder of 1 when it is divided
            # by 3, then the computer must subtract 1 to start with in order to win (this gets it to a multiple of 3
            # before the player has a go)
            if number%3==1:
                number-=1
                time.sleep(1)
                print()
                print('I have subtracted 1. The number is now:')
                print()
                print(number)
                player_choice(number)
            # if the start number is not divisible by 3 but has a remainder of 2 when it is divided by 3, the
            # computer subtracts 2 to get to a multiple of 3 before the player can have a go
            elif number%3==2:
                number-=2
                time.sleep(1)
                print()
                print('I have subtracted 2. The number is now:')
                print()
                print(number)
                player_choice(number)
    else:
        print()
        print('You must choose a number which is greater than 6.')
    time.sleep(1)
    print()
    play_again = input('Would you like to play again? Enter yes or no. ')
    play_again = play_again.lower()
