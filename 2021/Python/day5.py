# Get line segment points from input file
with open("./inputs/in5.txt") as file:
    first_points = []
    second_points = []
    for line in file:
        points = line.strip().split(" -> ")
        first_points.append([int(x) for x in points[0].split(",")])
        second_points.append([int(x) for x in points[1].split(",")])

# Determine size of grid
max_x = 0
max_y = 0
for x2, y2 in second_points:
    max_x = max(max_x, x2)
    max_y = max(max_y, y2)

# Create grids for part 1 and part 2
grid1 = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
grid2 = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

# Increment occupied space by the lines on the grid
for first_point, second_point in zip(first_points, second_points):
    x1 = first_point[0]
    y1 = first_point[1]
    x2 = second_point[0]
    y2 = second_point[1]

    # Part 1
    if x1 == x2:
        a = min(y1, y2)
        b = max(y1, y2)
        for y in range(a, b + 1):
            grid1[x1][y] += 1
            grid2[x1][y] += 1
    elif y1 == y2:
        a = min(x1, x2)
        b = max(x1, x2)
        for x in range(a, b + 1):
            grid1[x][y1] += 1
            grid2[x][y1] += 1
    
    # Part 2
    line_length = abs(x1 - x2) + 1
    if x1 < x2 and y1 < y2:
        for x in range(line_length):
            grid2[x1 + x][y1 + x] += 1
    elif x1 < x2 and y1 > y2:
        for x in range(line_length):
            grid2[x1 + x][y1 - x] += 1
    elif x1 > x2 and y1 < y2:
        for x in range(line_length):
            grid2[x1 - x][y1 + x] += 1
    elif x1 > x2 and y1 > y2:
        for x in range(line_length):
            grid2[x1 - x][y1 - x] += 1

# Count how many lines overlap
part1 = 0
part2 = 0
for i in range(len(grid1)):
    for j in range(len(grid1[0])):
        if grid1[i][j] > 1:
            part1 += 1
        
        if grid2[i][j] > 1:
            part2 += 1
print(f"The answer to part 1 is {part1}")
print(f"The answer to part 2 is {part2}")

