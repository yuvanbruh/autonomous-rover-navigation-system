def wheel_slip_model(
    world,
    rover,

):
    terrain = world[
        int(rover.x), int(rover.y)
    ]
    if terrain==1:
                return  0.5
    elif terrain==2:
                return 0.7
    else:
        return 1
    
        
    