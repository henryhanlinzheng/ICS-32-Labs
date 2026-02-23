from pathlib import Path

def get_notes_path(filename) -> Path:
    return Path(".") / filename

def ensure_file_exists(filename: Path):
    return get_notes_path(filename).exists()

def save_note(filename: str, note: str):
    # create path obj to notes storage file
    p = get_notes_path(filename)
    # check if storage file exists, if not create it.
    if not p.exists():
        p.touch(exist_ok=True)
    
    # open and write user note to file
    f = p.open('a')
    f.write(note + '\n')

def read_notes(filename: str):
    p = get_notes_path(filename)

    # check if storage file exists, if not return.
    if not ensure_file_exists(filename):
        return
    
    print("Here are your notes: \n")
    # open and write user note to file
    f = p.open()
    for line in f:
        print(line)

def remove_note(filename: str, note: list[str]) -> str:
    with get_notes_path(filename).open('w') as f:
        f.writelines(note)