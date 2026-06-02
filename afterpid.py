import matplotlib.pyplot as plt
import math
from visualization.trajectory_plotter import plot_trajectory
from rover.sensors import lidar_scan
from environment.mars_world import create_world
from visualization.renderer import render_world
from environment.terrain import add_terrain
from environment.obstacles import add_obstacles
from estimation.ekf import EKF
from planning.astar import astar
from visualization.path_renderer import render_path
from mapping.occupancy_grid import *
# from  rover.sensors import lidar_scan
# from visualization.renderer import render_rove
from visualization.rover_renderer import render_rover
from rover.state import RoverState
from visualization.rover_renderer import render_lidar
from rover.dynamics import update_rover
from estimation.localisation import gps_measurement
from estimation.localisation import imu_sensormeasurement
world= create_world()
world=add_terrain(world)
world=add_obstacles(world) 
rover= RoverState()
rows,cols= world.shape
occupancy_grid = create_grid(
    rows,cols
)


ekf=EKF()
rover.velocity=1
# plt.figure(figsize=(8,8))
plt.figure(1, figsize=(8,8))

true_x=[]
true_y=[]
gps_x_list=[]
gps_y_list=[]
ekf_x_list=[]
ekf_y_list=[]



# this while loop forms the ultimate autonomy . and we removed the plt.show becuse its basic and used to map . 
while True:
    
    render_world(occupancy_grid)
    render_rover(rover)
    obstacle= lidar_scan(world,rover)
    render_lidar(obstacle)
    gps_x, gps_y= gps_measurement(rover)
 
    imu_theta , imu_velocity = imu_sensormeasurement(rover)
    ekf.predict(
    
    imu_velocity,
    0.0

)
    ekf.update(

    gps_x,
    gps_y

)
    occupancy_grid=update_grid(occupancy_grid,obstacle,
                rover.x,
                rover.y)
    start = (
        int(rover.x),
        int(rover.y)
    )
    goal=(90,90)
    path =astar(
        occupancy_grid,
        start,
        goal
    )
    if len(path)>1:
        target = path[1]
        target_x, target_y= target
        dx = target_x- rover.x
        dy = target_y-rover.y
        desired_theta = math.atan2(
            dy,dx
        )
        heading_error = math.atan2(

        math.sin(
        desired_theta - rover.theta
        ),

        math.cos(
        desired_theta - rover.theta
        )

)
        kp=0.15
        rover.theta+= (kp*heading_error)
        update_rover(rover)
        render_path(path)
        ekf_x = ekf.state[0]
        ekf_y = ekf.state[1]
        ekf_theta = ekf.state[2]
    true_x.append(rover.x)
    true_y.append(rover.y)
    gps_x_list.append(gps_x)
    gps_y_list.append(gps_y)
    ekf_x_list.append(ekf_x)
    ekf_y_list.append(ekf_y)
    
    plot_trajectory(
        true_x,
        true_y,
        gps_x_list,
        gps_y_list,
        ekf_x_list,
        ekf_y_list
    )
    # print("GPS:")
    # print("EKF:")
    # print(ekf_x, ekf_y)
    
    # print(gps_x,gps_y)
    # print(imu_theta,imu_velocity)
    plt.pause(0.05)
    # print(obstacle)
    plt.figure(1)

    plt.clf()

