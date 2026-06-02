import math

WORLD_SIZE = 100

def update_rover(rover):
    rover.theta += rover.angular_velocity
    actual_velocity = rover.velocity*rover.slip_factor
    new_x = rover.x + actual_velocity * math.cos(rover.theta)

    new_y = rover.y + actual_velocity * math.sin(rover.theta)

    rover.x = max(0, min(new_x, WORLD_SIZE - 1))

    rover.y = max(0, min(new_y, WORLD_SIZE - 1))
    
 
    