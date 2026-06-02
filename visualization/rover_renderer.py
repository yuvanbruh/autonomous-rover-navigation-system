import matplotlib.pyplot as plt

def render_rover(state):

    plt.plot(
        state.y,
        state.x,
        "ko",
        markersize=10,
        label="Rover"
    )

def render_lidar(obstacles):

    first = True

    for obstacle in obstacles:

        x, y = obstacle

        if first:

            plt.plot(
                y,
                x,
                "bo",
                markersize=4,
                label="Detected Obstacles"
            )

            first = False

        else:

            plt.plot(
                y,
                x,
                "bo",
                markersize=4
            )