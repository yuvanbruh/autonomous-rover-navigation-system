
import math
import numpy as np


class EKF:

    def __init__(self):

        # estimated state
        # [x, y, theta]

        self.state = np.array([

            0.0,
            0.0,
            0.0

        ])

        # covariance matrix

        self.P = np.eye(3)

        # GPS measurement uncertainty

        self.R = np.array([

            [20.0, 0.0],

            [0.0, 20.0]

        ])


    def predict(

        self,
        velocity,
        angular_velocity,
        dt=1

    ):

        # current estimated state

        x = self.state[0]

        y = self.state[1]

        theta = self.state[2]


        # motion model prediction

        x = x + velocity * math.cos(theta) * dt

        y = y + velocity * math.sin(theta) * dt

        theta = theta + angular_velocity * dt


        # update predicted state

        self.state = np.array([

            x,
            y,
            theta

        ])


        # Jacobian matrix

        F = np.array([

            [1, 0, -velocity * math.sin(theta) * dt],

            [0, 1,  velocity * math.cos(theta) * dt],

            [0, 0, 1]

        ])


        # process noise

        Q = 1.3 * np.eye(3)


        # covariance propagation

        self.P = F @ self.P @ F.T + Q


    def update(

        self,
        gps_x,
        gps_y

    ):

        # GPS measurement vector

        z = np.array([

            gps_x,
            gps_y

        ])


        # measurement matrix

        H = np.array([

            [1, 0, 0],

            [0, 1, 0]

        ])


        # residual

        y = z - H @ self.state


        # residual covariance

        S = H @ self.P @ H.T + self.R


        # Kalman Gain

        K = self.P @ H.T @ np.linalg.inv(S)


        # corrected state estimate

        self.state = self.state + K @ y


        # covariance update

        I = np.eye(3)

        self.P = (I - K @ H) @ self.P
