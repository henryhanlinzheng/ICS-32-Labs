from abc import ABC, abstractmethod
from dataclasses import dataclass
import random

"""
This module simulates a Dog Care program. You can create dogs, feed them, and check their hunger levels.
"""
@dataclass
class Appetite:
    """Holds appetite levels for dogs."""
    LOW = 3
    """Low appetite dogs will be hungry after 3 time units."""
    MEDIUM = 4
    """Medium appetite dogs will be hungry after 4 time units."""
    HIGH = 5
    """High appetite dogs will be hungry after 5 time units."""


class Dog(ABC):
    """
    Abstract base class for all dogs.

    Attributes: 

        hunger_clock (int): Time since last fed.  
        _name (str): Name of the dog.  
        _age (int): Age of the dog.  
        appetite (int): Appetite level of the dog.  
    """
    def __init__(self, name, age, appetite) -> None:
        """
        Make an arbitrary dog with a name, age, and appetite level.
        
        Args:  

            name (str): Name of the dog.  
            age (int): Age of the dog.  
            appetite (int): Appetite level of the dog.  
        """
        self.hunger_clock = 0
        """Time since last fed."""
        self._name = name
        """Name of the dog."""
        self._age = age
        """Age of the dog."""
        self.appetite = appetite
        """Appetite level of the dog."""

    @abstractmethod
    def breed(self):
        """Abstract method to return the breed of the dog."""
        pass

    def name(self):
        """ Returns name of the dog."""
        return self._name

    def age(self):
        """Returns age of the dog."""
        return self._age

    def hungry(self):
        """
        The hungry method will check the hungry clock to see if some time has
        passed since the last feeding. If clock is greater than breed typical
        appetite, hunger assessment is randomly selected,
        otherwise hunger clock increases
        """
        hungry_bool = False
        if self.hunger_clock > self.appetite:
            hungry_bool = bool(random.getrandbits(1))
        else:
            self.hunger_clock += 1
            hungry_bool = False
        return hungry_bool

    def feed(self):
        """
        Feeds the dog. Hunger clock is reset
        """
        self.hunger_clock = 0


class GermanShepherd(Dog):
    """A German Shepherd dog."""
    def __init__(self, name, age):
        """
        Make a German Shepherd with a name and age. Appetite is set to medium by default.
        
        Args:  

            name (str): Name of the dog.  
            age (int): Age of the dog.  
        """
        super().__init__(name, age, appetite=Appetite.MEDIUM)

    def breed(self):
        """Return the breed of the dog. (German Shepherd)"""
        return "German Shepherd"


class GoldenRetriever(Dog):
    """A Golden Retriever dog."""
    def __init__(self, name, age):
        """
        Make a Golden Retriever with a name and age. Appetite is set to medium by default.
        
        Args:  

            name (str): Name of the dog.  
            age (int): Age of the dog.  
        """
        super().__init__(name, age, appetite=Appetite.MEDIUM)

    def breed(self):
        """Return the breed of the dog. (Golden Retriever)"""
        return "Golden Retriever"


class AnatolianShepherd(Dog):
    """An Anatolian Shepherd dog."""
    def __init__(self, name, age):
        """
        Make an Anatolian Shepherd with a name and age. Appetite is set to medium by default.
        
        Args:  

            name (str): Name of the dog.  
            age (int): Age of the dog.  
        """
        super().__init__(name, age, appetite=Appetite.MEDIUM)

    def breed(self):
        """Return the breed of the dog. (Anatolian Shepherd)"""
        return "Anatolian Shepherd"


def create_dog() -> Dog:
    """Create a dog based on user input."""
    tmp_dog = None
    breed = input("What breed of dog would you like to care for? \n\n" +
                  " 1. German Shepherd \n" +
                  " 2. Golden Retriever \n" +
                  " 3. Anatolian Shepherd \n: ")
    name = input("What would you like to name your dog? ")
    age = input("How old would you like your dog to be? ")
    age = int(age)
    if breed == "1":
        tmp_dog = GermanShepherd(name, age)
    elif breed == "2":
        tmp_dog = GoldenRetriever(name, age)
    elif breed == "3":
        tmp_dog = AnatolianShepherd(name, age)
    else:
        print("I didn't understand your entry, please run again.")
    return tmp_dog


def feed_dog(dog: Dog) -> None:
    """
    Feed the dog until the user decides to quit or until dog is no longer hungry.
    
    Args:  

        dog (Dog): The dog to be fed.  
    """
    while True:
        h_text = ""
        if dog.hungry() is False:
            h_text = "not "
        print(f"Your {dog.breed()}, {dog.name()} is {h_text}hungry.")
        feed = input(f"Would you like to feed {dog.name()}? (y/n/q): ")

        if feed == "y":
            dog.feed()
        elif feed == "q":
            break


def main() -> None:
    """Main function to run the dog care program."""
    # Create a dog
    my_dog = None
    while my_dog is None:
        my_dog = create_dog()
    # Feed the dog
    feed_dog(my_dog)


if __name__ == '__main__':
    main()
