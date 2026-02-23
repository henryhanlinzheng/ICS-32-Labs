#lab4.py

# Starter code for lab 4 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# NAME
# EMAIL
# STUDENT ID

from itertools import count
import random

"""
The default numbers here are generally good enough to create a rich tree. 
You are free to play with the numbers if you want. Lower numbers will simplify the results, 
larger numbers will take more time to render and create hundreds of acorns.
"""

TREE_DEPTH = 5
NODE_DEPTH = 5

def tree_builder(nodes:list, level:int, acorn:str) -> list:
    """
    Builds a tree using the random integers selected from the tree_depth and node_depth defaults
    """
    r = random.randrange(1, NODE_DEPTH)
    for i in range(r):
        if level < TREE_DEPTH:
            level_id  = f"L{level}-{i}"
            if level_id == acorn:
                level_id += "(acorn)"
            n = [level_id]
            nodes.append(tree_builder(n, level+1, acorn_placer()))

    return nodes

def acorn_placer() -> str:
    """
    Returns a random acorn location based on tree_depth and node_depth defaults
    """
    return f"L{random.randrange(1,TREE_DEPTH)}-{random.randrange(1,NODE_DEPTH)}"

def acorn_finder(tree:list, parent_path="L0-0 -> "):
    """
    Searches the tree for the acorn location
    """
    # insert your solution code here (using recursion)
    found_path = []
    for node in tree:
        node_id = node[0]
        cleaned_node_id = node_id.replace("(acorn)", "")
        current_path = parent_path + cleaned_node_id
        if "(acorn)" in node_id:
            found_path.append(current_path)
        for child in node[1:]:
            found_path.extend(acorn_finder([child], current_path + " -> "))
    return found_path

    # end solution

def run():
    # create a tree and start placing acorns
    tree = tree_builder([], 1, acorn_placer())
    # print the tree for testing. 
    # TODO: REMOVE THIS PRINT STATEMENT BEFORE YOU SUBMIT YOUR LAB
    
    # insert your solution code here
    print("Welcome to PyAcornFinder! \n")

    acorn_paths = acorn_finder(tree)
    print(f"You have {len(acorn_paths)} acorns on your tree.")
    print("They are located on the following branches:")

    for path in acorn_paths:
        print(path)

    
    # end solution

if __name__ == "__main__":
    print("Welcome to PyAcornFinder! \n")

    run()
