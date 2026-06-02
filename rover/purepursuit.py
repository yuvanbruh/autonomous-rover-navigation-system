import math 
def pure_pursuit_control(
    rover,
    target_x ,
    target_y
):
    dx = target_x-rover.x
    dy = target_y-rover.y

    lookahead_distance = math.sqrt(dx**2 + dy**2)
    if lookahead_distance< 0.001:
        return 0.00
    target_angle = math.atan2(dy,dx)
    alpha =math.atan2 (math.sin( target_angle-rover.theta
                     ),
             math.cos( target_angle-rover.theta)
          
    )
    curvature = (2*math.sin(alpha))/ lookahead_distance
    
    return curvature
    
    