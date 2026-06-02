import matplotlib.pyplot as plt
import math
from intelligence.mission_state import *
from rover.purepursuit import pure_pursuit_control
from planning.frontier_planner import *
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

replan_counter=0
REPLAN_INTERVAL = 20
path=[]
current_state = MISSION_EXPLORE
battery=80
home_x = rover.x 
home_y = rover.y

current_goal =None
# this while loop forms the ultimate autonomy . and we removed the plt.show becuse its basic and used to map . 
while True:
    battery -=0.01
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
    
    frontiers= find_frontier(
         occupancy_grid
        )
    dist_to_home= math.sqrt((home_x-rover.x)**2+ (home_y-rover.y)**2)
    current_state = update_mission_state(
            frontiers, 
            current_state,
            battery,
            dist_to_home
            
        )
    if current_state== MISSION_EXPLORE:
        if current_goal is None:
        
         current_goal= choose_frontier_goal(
            frontiers
        )
    elif current_state== RETURN_HOME:
        current_goal= (
            int(home_x),
            int(home_y)
        )
    elif current_state== MISSION_COMPLETE:
        print("MISSION COMPLETE")
        break
    
    replan_counter+=1
    if(
        current_goal is not  None and (len(path)==0 or replan_counter>REPLAN_INTERVAL)
    ):
        path=astar(
            occupancy_grid,
            start,
            current_goal
        )
        replan_counter=0
    if len(path)>1:
        lookahead_index = min(
            4, len(path)-1
        )
        target=path[lookahead_index]
        
        target_x, target_y= target
        dx = target_x- rover.x
        dy = target_y-rover.y
        curvature = pure_pursuit_control(
            rover,
            target_x,
            target_y
        )
        steering_gain =0.5
        rover.theta += steering_gain*curvature
    update_rover(rover)
    if current_goal is not None:

     goal_x, goal_y = current_goal

     goal_distance = math.sqrt(

     (goal_x - rover.x)**2
    +
    (goal_y - rover.y)**2

    )
    
     if goal_distance < 3:

      current_goal = None
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

