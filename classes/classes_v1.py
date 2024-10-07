"""Always name classes with UpperLetters"""


class FunnyNumber:
    """Buiid-in function __init__() is always executed when a class is being initiated
    Uses:
    * Assign values to object properties
    * Necessary operations to do when an object is beign created
    """

    def __init__(self, x, name) -> None:
        """x is a property of the class"""

        self.x = x
        self.name = name

    """the str function return what should be return when the class is represented as a string"""

    def __str__(self):
        return f"{self.name}"

    def amount_letters(self):
        # self is a reference to the current instance of the class, is used to access variables
        # that belong to the class
        print(len(self.name))


# Create an object using the class
p1 = FunnyNumber(8, "funny")

# print the property
p1.amount_letters()
