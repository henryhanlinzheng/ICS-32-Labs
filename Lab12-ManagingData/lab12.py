#lab12.py
#
# Starter code for lab 12 in ICS 32
# Programming with Software Libraries in Python
#
# Replace the following placeholders with your information.
# Please see the Canvas assignment prompt for the requirements
# of this lab exercise

# NAME
# EMAIL
# STUDENT ID

import json
import time


def to_json(obj: dict) -> str:
    """
    serializes a python dictionary object to a json formatted string
    returns None if object cannot be serialized to json
    """
    # TODO: implement function
    try:
        return json.dumps(obj)
    except (TypeError, OverflowError) as e:
        print(f"{e}")
        return None


def from_json(obj: str) -> any:
    """
    deserializes a json formatted string to a python type.
    return type depends on json structure.
    returns None if string cannot be deserialized from json
    """
    # TODO: implement function
    try:
        return json.loads(obj)
    except (json.JSONDecodeError, TypeError) as e:
        print(f"{e}")
        return None


def run_test() -> None:
    my_json_format = {
        "url": "https://www.ics.uci.edu",
        "created_at": time.time(),
        "visited": [time.time(), time.time() + 100]
    }# TODO: replace with your format.
    """
    You will have to decide how you will create your format for testing.
    The simplest approach might
    the following (note this example is missing some requirements on purpose):

    my_json_format = {"url": "https://www.ics.uci.edu"}

    A better approach would be to write a function that will accept the
    required data as parameter(s)
    and return a value that is in the format you have designed.

    You might also consider generating multiple test conditions.
    If you would like to place the print test code
    below into a loop to print multiple conditions, feel free to change it.
    """

    j = to_json(my_json_format)

    print(j)

    if j is not None:
        d = from_json(j)
        print(d)
    else:
        print("Unable to deserialize object")


if __name__ == "__main__":
    run_test()
