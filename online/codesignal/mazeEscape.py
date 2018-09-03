def mazeEscape(w, h, impassable):
    # build
    maze = [[0 for i in range(w)] for j in range(h)]
    for i in range(0, len(impassable), 2):
        by, bx = impassable[i], impassable[i+1]
        maze[bx][by] = -1
    # bfs
    to_visit = [(0, 0)]
    while to_visit:
        y, x = to_visit.pop(0)
        # left
        if x > 0 and maze[y][x-1] == 0:
            maze[y][x-1] = maze[y][x] + 1
            to_visit.append((y, x-1))
        # right
        if x < len(maze[y])-1 and maze[y][x+1] == 0:
            maze[y][x+1] = maze[y][x] + 1
            to_visit.append((y, x+1))
        # up
        if y > 0 and maze[y-1][x] == 0:
            maze[y-1][x] = maze[y][x] + 1
            to_visit.append((y-1, x))
        # down
        if y < len(maze)-1 and maze[y+1][x] == 0:
            maze[y+1][x] = maze[y][x] + 1
            to_visit.append((y+1, x))
        if maze[-1][-1]:
            return maze[-1][-1]
    return -1
