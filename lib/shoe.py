#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self._brand = brand
        self._size = size
        self._condition = "Used"

    @property
    def brand(self):
        return self._brand

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        if isinstance(new_size, int):
            self._size = new_size
        else:
            print("size must be an integer")

    @property
    def condition(self):
        return self._condition

    def cobble(self):
        self._condition = "New"
        print("Your shoe is as good as new!")

