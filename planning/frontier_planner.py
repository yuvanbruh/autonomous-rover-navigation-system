def find_frontier(

    grid

):

    rows, cols = grid.shape


    frontier_cells = []


    for x in range(1, rows - 1):

        for y in range(1, cols - 1):


            if grid[x][y] != 1:

                continue


            neighbors = [

                (x + 1, y),
                (x - 1, y),

                (x, y + 1),
                (x, y - 1)

            ]


            for nx, ny in neighbors:


                if grid[nx][ny] == 0:

                    frontier_cells.append(

                        (x, y)

                    )

                    break


    return frontier_cells

def choose_frontier_goal(
    frontier_cells
):
    if len(frontier_cells)==0:
       return  None
    return frontier_cells[0]