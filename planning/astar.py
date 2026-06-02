import heapq


def heuristic(

    a,
    b

):

    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(

    grid,
    start,
    goal

):

    open_set = []

    heapq.heappush(

        open_set,

        (0, start)

    )

    came_from = {}

    g_cost = {}

    g_cost[start] = 0

    while open_set:

        current = heapq.heappop(

            open_set

        )[1]

        if current == goal:

            break

        x, y = current

        neighbors = [

            (x + 1, y),

            (x - 1, y),

            (x, y + 1),

            (x, y - 1)

        ]

        for neighbor in neighbors:

            nx, ny = neighbor

            if (

                nx < 0
                or ny < 0
                or nx >= grid.shape[0]
                or ny >= grid.shape[1]

            ):

                continue

            if grid[nx][ny] == -1:

                continue

            tentative_g = g_cost[current] + 1

            if (

                neighbor not in g_cost
                or tentative_g < g_cost[neighbor]

            ):

                g_cost[neighbor] = tentative_g

                f_cost = (

                    tentative_g
                    + heuristic(

                        neighbor,
                        goal

                    )

                )

                heapq.heappush(

                    open_set,

                    (f_cost, neighbor)

                )

                came_from[neighbor] = current

    path = []

    current = goal

    while current in came_from:

        path.append(current)

        current = came_from[current]

    path.reverse()

    return path