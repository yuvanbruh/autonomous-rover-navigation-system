import math

def lidar_scan(world, rover, scan_radius=25):

    obstacles = []

    rows, cols = world.shape

    rover_x = int(rover.x)
    rover_y = int(rover.y)

    for x in range(rows):
        for y in range(cols):

            distance = math.sqrt(
                (x - rover_x)**2 +
                (y - rover_y)**2
            )

            if distance < scan_radius:

                if world[x, y] == 3:

                    obstacles.append((x, y))

    return obstacles