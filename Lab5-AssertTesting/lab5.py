"""
This program enables a user to input short one line notes and have them stored in a file called pynote.txt
"""

from pathlib import Path

NOTES_PATH = "."
NOTES_FILE = "pynote.txt"

def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

def save_note(note: str):
    # create path obj to notes storage file
    p = Path(NOTES_PATH) / NOTES_FILE

    # check if storage file exists, if not create it.
    if not p.exists():
        p.touch(exist_ok=True)
    
    # open and write user note to file
    f = p.open('a')
    f.write(note + '\n')
    f.close()

def read_notes():
    p = Path(NOTES_PATH) / NOTES_FILE

    # check if storage file exists, if not return.
    if not p.exists():
        return
    
    print("Here are your notes: \n")
    # open and write user note to file
    f = p.open()
    for line in f:
        print(line)
    f.close()

def remove_note() -> str:
    p = Path(NOTES_PATH) / NOTES_FILE

    # check if storage file exists, if not raise FileNotFoundError per L5-REQ-2.
    if not p.exists():
        """
        REQUIREMENT 3 - Should be very similar, custom message not required.
        - remove the 'raise FileNotFoundError' line below and uncomment the 'return' if you want original behavior.
        """
        # raise FileNotFoundError("Notes file not found: pynote.txt")
        # return
    
    print("Here are your notes: \n")
    # open and write user note to file
    f = p.open()
    id = 1
    lines = []

    # print each note with an id and store each line in a list
    for line in f:
        lines.append(line)
        print(f"{id}: {line}")
        id = id+1
    f.close()

    remove_id = input("Enter the number of the note you would like to remove: ")
    if not is_int(remove_id):
        print ("Not a valid number, cancelling operation.")
        return ""

    # open as write to overwrite existing notes, add notes back while skipping user selection 
    f = p.open('w')
    id = 1
    removed_note = ""

    for line in lines:
        if id == int(remove_id):
            removed_note = line
        else:
            f.write(line)
        id = id+1
    f.close()

    return removed_note

def run():
    note = input("Please enter a note (enter :d to delete a note or :q to exit):  ")
    if note == ":d":
        try:
            note = remove_note()
            print(f"The following note has been removed: \n\n {note}")
        except FileNotFoundError:
            print("No notes file found to delete from.")
    elif note == ":q":
        return
    else:    
        save_note(note)
    run()


if __name__ == "__main__":
    p_test = Path(NOTES_PATH) / NOTES_FILE
    if p_test.exists():
        p_test.unlink()
    
    # L5-REQ-1
    assert is_int("5") == True, "is_int should return True for numeric string '5'"
    assert is_int(5) == True, "is_int should return True for integer 5"
    assert is_int(5.0) == True, "is_int should return True for float 5.0"
    assert is_int("5.0") == False, "is_int should return False for string '5.0'"
    assert is_int("hello") == False, "is_int should return False for 'hello'"
    assert is_int(True) == True, "is_int should return True for True (int(True) == 1)"

    # L5-REQ-2
    p = Path(NOTES_PATH) / NOTES_FILE
    try:
        remove_note()
        assert False, "Expected FileNotFoundError when pynote.txt is missing"
    except FileNotFoundError:
        print("FileNotFoundError correctly raised for missing pynote.txt")

    print("Welcome to PyNote! \n")
    read_notes()

    run()

