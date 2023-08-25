"""
This file setups the world to live for animals, it creates
terrain to numpy array with forest, and field
"""
# programs own imports
from forest import Forest
from open_area import OpenArea
# --------------------
# Other imports
import numpy as np
import random

# --------------------

class World:

    def __init__(self,world_name,size:tuple):
        self.world_name = world_name
        self.size = size

    def create_word(self):
        arr = np.zeros(self.size,dtype=object)
        arr = self.create_nature(arr)
        print(arr.sum())
        print(arr)

    def create_nature(self,arr):
        """
        Creates random ecosystem to 'map'
        return numpy array
        """
        ecosystems = [Forest,OpenArea]
        iterations = int(self.size[0]/10)
        for i in range(0,iterations):
            ecosystem = random.choice(ecosystems)
            print(ecosystem)
            x_start = random.randint(0,self.size[0])
            x_end = random.randint(x_start,self.size[0])
            y_start = random.randint(0,self.size[0])
            y_end = random.randint(y_start,self.size[0])
            arr[x_start:x_end,y_start:y_end] = 1
        return arr


if __name__ == "__main__":
    world = World("test",(50,50))
    world.create_word()