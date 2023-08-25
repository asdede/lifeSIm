"""

"""

import random
import numpy as np

class Forest:

    def __init__(self):
        self.nutrients = random.randint(0,9999)
        self.area = np.zeros((50,50),dtype=object)
    
    def create_forest(self):
        """
        Creates randomly trees to area
        """
        iters = random.randint(5,20)
        for i in range (iters+1):
            row = np.random.randint(self.area.shape[0])
            col = np.random.randint(self.area.shape[1])
            self.area[row,col] = Tree(is_adult=True) # random amount of adult trees to area
    
    def grow_in_forest(self):
        mask = np.vectorize(lambda x: isinstance(x, Tree))(self.area)
        trees = self.area[mask]
        grow_function = np.vectorize(lambda x: x.grow(forest.nutrients) if isinstance(x, Tree) else x)
        self.nutrients -= np.sum(grow_function(self.area))
    
    def breeding_time(self):
        pass

        
    

class Tree:
    """ IS a tree"""
    def __init__(self,is_adult=False,A=None,B=None,C=None,D=None,F=None):
        if (is_adult):
            self.age = 15 # in years
            self.size = 800.00 # in cm's
            self.gene_A = np.random.uniform(1.0,10.0) # growth hormone
            self.gene_B = np.random.uniform(1.0,10.0) # immunity
            self.gene_C = np.random.uniform(1.0,10.0) # fertility
            self.gene_D = np.random.uniform(1.0,10.0) # nutrient gathering
            self.gene_F = np.random.uniform(1.0,10.0) # nutrient consumption
        else:
            self.age = 1
            self.size = 10.00
            self.gene_A = A # growth hormone
            self.gene_B = B # immunity
            self.gene_C = C # fertility
            self.gene_D = D # nutrient gathering
            self.gene_F = F # nutrient consumption
        

    def grow(self,nutrients):
        """
        Grows trees based on their age
        takes x amount of nutrients from ground, depending how big they are
        """
        if nutrients == 0:
            return
        if self.age < 10:
            growth = (10 * (10 - self.age)) # grow rapidly when yonger
        else:
            growth = self.get_growth_amount()
        self.size += growth
        self.age +=1
        nutrients_consumed = (self.age * growth) / 100
        print(growth,nutrients_consumed)
        return nutrients_consumed
    
    def get_growth_amount(self):
        """
        Checks how many grow factors this has, calculates how much it grows.
        Returns nutrient consumption, and growth amount

        So A,D,F genes impact on growth
        A is most heaviest and affects with nutrient consumption (F)
        D Also has great impact on growing

        for now at date of 25.9.2023 i determine weights from my head
        Weight for A is 4
        weight for D is 2
        weight for F is 2
        and i will divide this with (D/F)
        """
        A = self.gene_A * 4
        D = self.gene_D * 3
        F = self.gene_F * 2
        growth  = sum((A,D,F)) / ((D / F))
        return growth
    
    def breed(self):
        pass



    

if __name__ == "__main__":
    forest = Forest()
    forest.create_forest()
    
    print("Before growth:")
    print(forest.nutrients)
    
    forest.grow_in_forest()
    
    print("\nAfter growth:")
    print(forest.nutrients)
    mask = np.vectorize(lambda x: isinstance(x, Tree))(forest.area)
    #trees = forest.area[mask]
    #for tree in trees:
    #    print(tree.size)