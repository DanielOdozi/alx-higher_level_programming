#!/usr/nbin/python3
'''A class that inherits from list'''


class MyList(list):
    """
    Function that returns the list of available attributes and methods,
    of an object

    Args:
        list (class): list
    """
    def __init__(self) -> None:
        """
        Call the main class into the sub-class

        Args:
            self (class): self
        """
        super().__init__()

    def print_sorted(self):
        """
        Print the list out but sorted

        Args:
            self (class): self

        Print:
            list: The list sorted
        """
        print(sorted(self))
