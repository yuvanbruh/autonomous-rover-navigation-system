import random 
def gps_measurement(rover):
    noise_x= random.gauss(0,1)
    noise_y= random.gauss(0,1)
    measured_x= rover.x + noise_x
    measured_y= rover.y + noise_y
    return measured_x, measured_y

def imu_sensormeasurement(rover):
    noise_theta= random.gauss(0, 0.05)
    noise_velocity= random.gauss(0,0.1)
    measured_theta = rover.theta + noise_theta
    measured_velocity = rover.velocity + noise_velocity
    return measured_theta, measured_velocity 