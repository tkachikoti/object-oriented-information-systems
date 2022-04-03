"""This module contains a class that represents a person.

Module by: Tinashe Nigel Kachikoti (@TNKachikoti)
"""
class Person:
    """Represents a generic Person."""
    def __init__(self, first, last, weight, height):
        """Initializes a person with first name, last name, weight and
        height.

        :param first: The first name of the person.
        :type first: str

        :param last: The last name of the person.
        :type last: str

        :param weight: The weight of the person.
        :type weight: int

        :param height: The height of the person.
        :type height: int

        :return: None
        """
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height

def main():
    """Demonstrates the functionality of the three functions."""
    p1 = Person("Tom", "Smith", 150, 77)
    p2 = Person("Fred", "Jones", 155, 73)
    p3 = Person("George", "Williams", 201, 91)
    p4 = Person("Tanya", "Davies", 152, 68)
    p5 = Person("Mary", "Taylor", 159, 83)

    people = [p1, p2, p3, p4, p5]

    for person in people:
        print(person.first_name)

if __name__ == '__main__':
    main()
