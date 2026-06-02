import numpy as np


def create_grid(
    rows,
    cols
):

    grid = np.zeros(
        (rows, cols)
    )

    return grid


def update_grid(
    grid,
    obstacles,
    rover_x,
    rover_y
):
    grid[int(rover_x),int(rover_y)]=1
    for obstacle in obstacles:

        x, y = obstacle

        grid[int(x),int(y)] = -1

    return grid

