# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:


from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        Adds values to a bag
        """
        # Uses the Dynamic Array's append method
        self._da.append(value)

    def remove(self, value: object) -> bool:
        """
        This method removes any one element from the bag that
        matches the provided value object
        """

        # Determine the length
        length = self._da.length()

        # Iterates over the array
        # Checks if current index is equal to the value
        # If so, calls the remove_at_index() method
        for i in range(length):
            if self._da.get_at_index(i) == value:
                self._da.remove_at_index(i)

                return True
        return False

    def count(self, value: object) -> int:
        """
        This method returns the number of elements in the
        bag that match the provided value object
        """

        # Counter for value
        num = 0

        # Determines the length
        length = self._da.length()

        # Iterates through the array
        # Uses get_at_index() to check if its equal to value
        # num then increments by 1
        for i in range(length):
            if self._da.get_at_index(i) == value:
                num += 1

        return num

    def clear(self) -> None:
        """
        This method clears the contents of the bag
        """

        # Determines the length
        length = self._da.length()

        # Iterates over the array
        # Removes in reverse order to keep correct indices
        for i in range(length-1, -1, -1):
            self._da.remove_at_index(i)

    def equal(self, second_bag: "Bag") -> bool:
        """
        This method compares the contents of a bag with the
        contents of a second bag provided as a parameter
        """
        # Determines the length
        length = self._da.length()

        # Checks first if bags are the same size
        if length != second_bag._da.length():
            return False

        # Iterates over the array
        # Sets value to current index
        # Checks if value equals current index of second_bag
        for i in range(length):
            value = self._da.get_at_index(i)

            if value == second_bag._da.get_at_index(i):
                return False
        return True


    def __iter__(self):
        """
        TODO: Write this implementation
        """
        pass

    def __next__(self):
        """
        TODO: Write this implementation
        """
        pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)
