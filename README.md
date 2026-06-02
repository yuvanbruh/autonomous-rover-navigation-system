# Autonomous Planetary Rover Navigation and Exploration System

## Overview

This project implements a complete autonomous rover exploration stack capable of localizing itself, building a map of an unknown environment, planning paths, making exploration decisions, and handling sensor and mobility disturbances.

The rover operates in a simulated planetary environment containing obstacles, rough terrain, and crater regions. Using GPS, IMU, and LiDAR sensors, the rover incrementally constructs an occupancy grid map, identifies unexplored frontier regions, autonomously selects exploration goals, plans safe paths, and navigates through the environment.

The rover autonomously transitions between exploration, return-home, and mission-completion states based on mission progress and battery constraints.

The system also evaluates robustness under multiple fault conditions including GPS noise, GPS dropout, and severe wheel-slip disturbances.

---

## Key Features

### Localization

* Extended Kalman Filter (EKF) sensor fusion
* GPS and IMU integration
* State estimation under noisy measurements

### Mapping

* Occupancy Grid Mapping
* Unknown, free, and occupied space representation
* Incremental map updates from LiDAR observations

### Autonomous Exploration

* Frontier Detection
* Frontier Selection
* Autonomous goal generation
* Exploration of unknown regions

### Path Planning

* A* Search Algorithm
* Obstacle-aware navigation
* Periodic replanning

### Control

* Pure Pursuit path tracking
* Proportional steering control
* Smooth waypoint following

### Mission-Level Autonomy

* EXPLORE state
* RETURN_HOME state
* MISSION_COMPLETE state
* Battery-aware decision making

### Fault Tolerance

* Increased GPS Noise
* GPS Dropout
* Severe Wheel Slip

---

## System Architecture

```mermaid
flowchart TD

A[GPS]
B[IMU]
C[LiDAR]

A --> D[EKF Localization]
B --> D

D --> E[Occupancy Grid Mapping]
C --> E

E --> F[Frontier Detection]

F --> G[Frontier Selection]

G --> H[A* Path Planner]

H --> I[Pure Pursuit Controller]

I --> J[Rover Dynamics]

J --> K[Environment Update]

K --> A
K --> B
K --> C

E --> L[Mission State Machine]

L --> L1[EXPLORE]
L --> L2[RETURN_HOME]
L --> L3[MISSION_COMPLETE]

N[GPS Noise] --> D
O[GPS Dropout] --> D

P[Wheel Slip Fault] --> J
```

---

## Fault Injection Experiments

### GPS Noise

Additional Gaussian noise is injected into GPS measurements to evaluate localization robustness under degraded sensor quality.

### GPS Dropout

GPS measurements are temporarily disabled, forcing the EKF to rely on prediction and remaining sensor information.

### Severe Wheel Slip

Terrain-induced wheel slip is increased beyond nominal conditions, introducing discrepancies between commanded and realized rover motion.

---

## Results

### Autonomous Exploration

![Exploration](screenshots/01_exploration.png)

The rover autonomously explores unknown regions using frontier-based exploration and incrementally constructs an occupancy map.

### Localization Performance

![Localization](screenshots/02_localization.png)

Comparison between:

* Ground Truth Trajectory
* GPS Measurements
* EKF Estimated Trajectory

### GPS Noise (σ = 3)

![GPS Noise Sigma 3](screenshots/03_gps_noise_sigma3.png)

### GPS Noise (σ = 5)

![GPS Noise Sigma 5](screenshots/04_gps_noise_sigma5.png)

### GPS Dropout

![GPS Dropout](screenshots/05_gps_dropout.png)

### Severe Wheel Slip

![Wheel Slip](screenshots/06_severe_wheel_slip.png)

### Mission Completion

![Mission Complete](screenshots/07_mission_complete.png)

---

## Project Structure

```text
project/

├── environment/
├── rover/
├── estimation/
├── mapping/
├── planning/
├── intelligence/
├── faults/
├── visualization/
└── main.py
```

---

## Technologies Used

* Python
* NumPy
* Matplotlib
* Extended Kalman Filter (EKF)
* Occupancy Grid Mapping
* A* Search Algorithm
* Pure Pursuit Control

---

## Future Work

* ROS2 Integration
* SLAM-based Localization and Mapping
* Multi-Robot Exploration
* Dynamic Obstacle Avoidance
* Hardware Deployment
* Model Predictive Control (MPC)

---

## Author

**Yuvan Ashrith**

Mechanical Engineering Undergraduate

University College of Engineering, Osmania University
