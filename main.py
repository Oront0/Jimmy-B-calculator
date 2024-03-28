import keyboard
import os
import time
from stringcolor import *


def menu():
    print("""
What's your programming skill level?
------------------------------------
          
1. Beginner
2. Intermediate
3. Expert
          
Press ESC to quit.
          
------------------------------------
""")


def calculating():
    for _ in range(1, 4):
        print("---------------------------------------------")
        print("Calculating..." + cs('\\', 'red'))
        print("---------------------------------------------")
        time.sleep(0.2)
        os.system('cls')
        print("---------------------------------------------")
        print("Calculating..." + cs('|', 'red'))
        print("---------------------------------------------")
        time.sleep(0.2)
        os.system('cls')
        print("---------------------------------------------")
        print("Calculating..." + cs('/', 'red'))
        print("---------------------------------------------")
        time.sleep(0.2)
        os.system('cls')
        print("---------------------------------------------")
        print("Calculating..." + cs('-', 'red'))
        print("---------------------------------------------")
        time.sleep(0.2)
        os.system('cls')
    print("---------------------------------------------")
    print("Calculating..." + cs('COMPLETE', 'green'))
    print("---------------------------------------------")
    time.sleep(1)
    os.system('cls')
        

def beginner(n):
    os.system('cls')
    res = n * 10
    calculating()
    print("---------------------------------------------")
    print("It will take approximately " + cs(str(res), "red") + " hours.")
    print("---------------------------------------------")
    input("Press Enter to continues...")


def intermediate(n):
    os.system('cls')
    res = n * 7
    calculating()
    print("---------------------------------------------")
    print("It will take approximately " + cs(str(res), "orange") + " hours.")
    print("---------------------------------------------")
    input("Press Enter to continues...")


def expert(n):
    os.system('cls')
    res = n * 4
    calculating()
    print("---------------------------------------------")
    print("It will take approximately " + cs(str(res), "green") + " hours.")
    print("---------------------------------------------")
    input("Press Enter to continues...")


def run():
    while True:
        os.system('cls')
        menu()
        choice = keyboard.read_key(suppress=True)

        if choice == '1':
            os.system('cls')
            print("---------------------------------------------")
            print('\rHow many minutes did Jimmy say the task would take?')
            print("---------------------------------------------")
            try:
                n = int(input('> '))
                beginner(n)
            except ValueError:
                print("Please enter a valid integer.")
                input("Press Enter to continue...")
            
        elif choice == '2':
            os.system('cls')
            print("---------------------------------------------")
            print('\rHow many minutes did Jimmy say the task would take?')
            print("---------------------------------------------")
            try:
                n = int(input('> '))
                intermediate(n)
            except ValueError:
                print("Please enter a valid integer.")
                input("Press Enter to continue...")

        elif choice == '3':
            os.system('cls')
            print("---------------------------------------------")
            print('\rHow many minutes did Jimmy say the task would take?')
            print("---------------------------------------------")
            try:
                n = int(input('> '))
                expert(n)
            except ValueError:
                print("Please enter a valid integer.")
                input("Press Enter to continue...")

        elif choice == 'esc':
            os.system('cls')
            break


if __name__ == '__main__':
    run()