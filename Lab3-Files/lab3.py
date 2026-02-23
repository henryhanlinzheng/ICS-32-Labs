#lab3.py

# Starter code for lab 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the Assignment prompt for the requirements of this lab exercise

# HENRY HANLIN ZHENG
# HHZHENG1@UCI.EDU
# 19204536
from pathlib import Path

def reading(pynote):
    with pynote.open('r') as my_file:
        for line in my_file:
            print(line.strip())
            print()

def appending(pynote, new_note):
    with pynote.open('a') as my_file:
        my_file.write(new_note + '\n')

def run():
    print("Welcome to PyNote!")

    base_dir = Path(__file__).parent
    pynote = base_dir / 'pynote.txt'

    if not pynote.exists():
        my_file = input("Enter the full path to the pynote file, including the filename: ")
        if my_file.strip() != "":
            pynote = Path(my_file)

    pynote.touch(exist_ok=True)

    print("Here are your notes:\n")
    reading(pynote)

    new_note = input("Please enter a new note (enter q to exit): ")
    while new_note != 'q':
        appending(pynote, new_note)
        new_note = input("Please enter a new note (enter q to exit): ")

if __name__ == "__main__":
    run()