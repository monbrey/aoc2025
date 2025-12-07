from utils.io import read_input_for


def read_input(strip: bool = True) -> str:
    """Return the contents of this module's `input.txt`."""
    return read_input_for(__file__, strip=strip)


def a():
    """Part a for day4."""
    data = read_input()
    if not data:
        return "input.txt not found or empty"

    grid = [l for l in data.splitlines()]
    adjacency = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]

    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == "@":
                for i in range(y-1, y+2):
                    for j in range(x-1, x+2):
                            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and not (i == y and j == x):
                                adjacency[i][j] += 1

    access = sum(1 for y in range(0, len(grid)) for x in range(0, len(grid[y])) if adjacency[y][x] < 4 and grid[y][x] == "@")
    print(access)

    # TODO: implement solution
    return access


def b():
    """Part b for day4."""
    data = read_input()
    if not data:
        return "input.txt not found or empty"

    grid = [l for l in data.splitlines()]
    more_access = True
    total_access = 0

    while more_access:
        # Need to now check adjacency every loop
        adjacency = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                if grid[y][x] == "@":
                    for i in range(y-1, y+2):
                        for j in range(x-1, x+2):
                                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and not (i == y and j == x):
                                    adjacency[i][j] += 1

        access = sum(1 for y in range(0, len(grid)) for x in range(0, len(grid[y])) if adjacency[y][x] < 4 and grid[y][x] == "@")
        if(access == 0):
            more_access = False

        total_access += access

        # Update the grid
        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                if adjacency[y][x] < 4 and grid[y][x] == "@":
                    grid[y] = grid[y][:x] + "." + grid[y][x+1:]


    # TODO: implement solution
    return total_access
