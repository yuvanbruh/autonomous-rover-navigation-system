import matplotlib.pyplot as plt

def render_path(path):

    if len(path) == 0:
        return

    x_points = []
    y_points = []

    for point in path:

        x, y = point

        x_points.append(y)
        y_points.append(x)

    plt.plot(
        x_points,
        y_points,
        color="cyan",
        linewidth=2,
        label="A* Path"
    )