'''
This script is being used as a
simple game called russian roulette.
It allows a single player to play
this famous game with AI using random
library or it allows two players to
play with each other.
'''

__author__ = "Saatvic Sehgal"


import random
import time


def gun_shot() :
    x = r"""
          (                                 _
           )                               /=>
          (  +__________________/\/\___ / /|
           .''.___________'._____      / /|/\
          : () :              :\ ----\|    \ )
           '..'____________.'0|----|      \
                            0_0/____/        \
                                |----    /----\
                               || -\\ --|      \
                               ||   || ||\      \
                                \\____// '|      \
        Bang! Bang!                     .'/       |
                                       .:/        |
                                       :/_________|  """
    print(x)


def gun_click() :
    x = r"""                                  _
                                           /=>
             +____________________/\/\___ / /|
           .''._____________'._____      / /|/\
          : () :              :\ ----\|    \ )
           '..'______________.'0|----|      \
                            0_0/____/        \
                                |----    /----\
                               || -\\ --|      \
                               ||   || ||\      \
                                \\____// '|      \
                                        .'/       |
                                       .:/        |
                                       :/_________|  """
    print(x)



def display() :
    print('_'*75,'\n')
    print("Welcome to this lethal game... THE RUSSIAN ROULETTE!!")
    print("Lets hope you survive this game.")
    print('_'*75,'\n')
    print("1. Play with AI")
    print("2. Play with friend offline")
    print("3. Quit Game")
    print("\nEnter anything to shoot.")
    print()


def player_with_AI(revolver) :
    for i in range(6) :
        if i%2 == 0 :
            player = "You"
        else :
            player = "I"
        print(player + ":")

        if i%2 == 0 :
            input()
        bullet = random.choice(revolver)
        revolver.remove(bullet)
        if bullet == 1 :
            gun_shot()
            print("BOOM!!")
            print(player + " DIED")
            break
        else :
            gun_click()
            print("CLICK")
            print("Phewww... still alive!")
            gun_click()

        time.sleep(2)


def player_with_player(revolver) :
    for i in range(6) :
        if i%2 == 0 :
            player = "Player 1"
        else :
            player = "Player 2"
        print(player + ':')

        input()
        bullet = random.choice(revolver)
        revolver.remove(bullet)
        if bullet == 1 :
            gun_shot()
            print("BOOM!!")
            print(player + " DIED")
            break
        else :
            gun_click()
            print("CLICK")
            print("Phewww... still alive!")

        time.sleep(2)


def main() :
    while True :
        display()
        revolver = [0,0,0,0,0,1]

        option = int(input("Enter play option: "))
        if option == 1 :
            player_with_AI(revolver)
        elif option == 2 :
            player_with_player(revolver)
        elif option == 3 :
            print("Quitting game...")
            break
        else :
            print("Invalid game option.")
    
if __name__ == "__main__" :
    main()
    
    
