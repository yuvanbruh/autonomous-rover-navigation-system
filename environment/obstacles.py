import numpy as np
import random 
def add_obstacles(world):
    row, col = world.shape
    for _ in range(150):
      x= random.randint(0, row-1)
      y= random.randint(0,col-1)
      world[x][y]=3
    
    return world