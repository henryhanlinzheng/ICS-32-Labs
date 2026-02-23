#lab8.py

# Starter code for lab 8 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# HENRY HANLIN ZHENG
# HHZHENG1@UCI.EDU
# 19204536

# ---------------------

from pathlib import Path

NOTES_PATH = "."
NOTES_FILE = "pynote.txt"

class Note:
    def __init__(self, filepath:Path):
        self.filepath = filepath
    def remove_note(self, index: int) -> str:
        with self.filepath.open('r') as f:
            lines = f.readlines()
        if 0 <= index < len(lines):
            removed = lines.pop(index)
            with self.filepath.open('w') as f:
                f.writelines(lines)
            return removed.strip()
        raise ValueError("Index out of range")
    def read_notes(self):
        try:
            with self.filepath.open('r') as f:
                return [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            return []
    def save_note(self, note: str):
        with self.filepath.open('a') as f:
            f.write(note + '\n')
        pass

# ---------------------

def print_notes(notes:list[str]):
    id = 0
    for n in notes:
        print(f"{id}: {n}")
        id+=1

def delete_note(note:Note):
    try:
        remove_id = input("Enter the number of the note you would like to remove: ")
        remove_note = note.remove_note(int(remove_id))
        print(f"The following note has been removed: \n\n {remove_note}")
    except FileNotFoundError:
        print("The PyNote.txt file no longer exists")
    except ValueError:
        print("The value you have entered is not a valid integer")

def run():
    p = Path(NOTES_PATH) / NOTES_FILE
    if not p.exists():
        p.touch()
    note = Note(p)
    
    print("Here are your notes: \n")
    print_notes(note.read_notes())

    user_input = input("Please enter a note (enter :d to delete a note or :q to exit):  ")

    if user_input == ":d":
        delete_note(note)
    elif user_input == ":q":
        return
    else:    
        note.save_note(user_input)
    run()


if __name__ == "__main__":
    print("Welcome to PyNote! \n")

    run()
