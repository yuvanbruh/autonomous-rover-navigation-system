
import random
import math
def add_terrain(world):
    rows, cols = world.shape

    #rough terrain patches 
    for _ in range(4):
        terrain_x = random.randint(15, rows -15)
        terrain_y= random.randint(15, cols-15)
        radius = random.randint(4,8)
        
        for x in range(rows):
            for y in range (cols):
                distance = math.sqrt((x-terrain_x)**2+ (y-terrain_y)**2)
                if (distance < radius):
                    world[x,y]=1
                    
                    
                    
                    ## rough craters 
    for _ in range(5):  
        crater_x= random.randint(20,rows-20)
        crater_y=random.randint(20,cols-20)
        
        radius= random.randint(5,10)
        
        for x in range(rows):
            for y in range(cols):
                distance = math.sqrt((x-crater_x)**2+ (y-crater_y)**2)
                if distance< radius:
                    world[x,y]=2
    return world
