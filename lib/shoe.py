#!/usr/bin/env python3

class Shoe:
    def __init__(self,brand="adidas" ,size=9):
        self.size = size  # Initialize using the property setter
        self.brand= brand
        self.condition ='New'

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")
    
    def repair(self):
        print("The shoe has been repaired.")
        self.condition='New'

    def cobble(self):
        print("Your shoe is as good as new!")