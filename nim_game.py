import time
import random

def comp_wins():
    print()
    time.sleep(1)
    print('I was the first to reach 0. I win.')

def player_choice(number):
    while number > 0:
        time.sleep(1)
        print()
        print('Enter the number which you would like to subtract. 1 or 2. ')
        choice = int(input())
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

            
play_again = 'y'
number = 0
while play_again.lower().startswith('y') == True:
    time.sleep(1)
    print('Choose a start number which is greater than 6. ')
    number = int(input())
    if number>6:
        if number%3==0:
            player_choice(number)
        else:
            if number%3==1:
                number-=1
                time.sleep(1)
                print()
                print('I have subtracted 1. The number is now:')
                print()
                print(number)
                player_choice(number)
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
