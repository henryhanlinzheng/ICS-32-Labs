"""

This program enables a user to input short one line notes and have them stored in a file called pynote.txt

"""
import helpers

NOTES_PATH = "."
NOTES_FILE = "pynote.txt"

def is_int(val):
    if isinstance(val, int) and not isinstance(val, bool):
        return True
    return False

def print_notes(notes: list[str]):
    print("Here are your notes: \n")
    for id, line in enumerate(notes, start=1):
        print(f"{id}: {line}", end='')

def remove_note() -> str:
    if not helpers.ensure_file_exists(NOTES_FILE):
        raise FileNotFoundError("Notes file has been deleted unexpectedly")
    
    lines = helpers.read_notes(NOTES_FILE)

    print_notes(lines)

    remove_id = input("Enter the number of the note you would like to remove: ")
    if not is_int(remove_id):
        print ("Not a valid number, cancelling operation.")
        return ""

    index = int(remove_id) - 1
    if 0 <= index < len(lines):
        removed_note = lines.pop(index)
        helpers.overwrite_notes(NOTES_FILE, lines)
        return removed_note
    else:
        print("Invalid note number.")
        return ""

def run():
    note = input("Please enter a note (enter :d to delete a note or :q to exit):  ")
    if note == ":d":
        try:
            removed = remove_note()
            if removed:
                assert False, "FileNotFoundError should have been raised"
            
            print(f"The following note has been removed: \n\n {note}")
        except FileNotFoundError:
            print("The PyNote.txt file no longer exists")
    elif note == ":q":
        return
    else:    
        helpers.save_note(NOTES_FILE,note)
    run()


if __name__ == "__main__":
    assert is_int("5") == False, "is_int should return False for numeric string '5'"
    assert is_int(5) == True, "is_int should return True for integer 5"
    assert is_int(5.0) == False, "is_int should return False for float 5.0"
    assert is_int("5.0") == False, "is_int should return False for string '5.0'"
    assert is_int("hello") == False, "is_int should return False for 'hello'"
    assert is_int(True) == False, "is_int should return False for True (int(True) == 1)"
    
    print("Welcome to PyNote! \n")  
    current_notes = helpers.read_notes(NOTES_FILE)
    if current_notes:
        print_notes(current_notes)

    run()
    