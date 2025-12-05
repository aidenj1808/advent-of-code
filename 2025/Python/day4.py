with open("./inputs/in4.txt") as file:
    grid = []
    for line in file:
        line = line.strip()
        grid.append([char for char in line])

ROWS = len(grid)
COLS = len(grid[0])

def paper_is_accessible(i, j):
    if grid[i][j] == ".":
        return -1

    rolls_of_paper = 0
    for x_dir in [-1, 0, 1]:
        for y_dir in [-1, 0, 1]:
            if x_dir == 0 and y_dir == 0 :
                continue

            if 0 <= i + y_dir < ROWS and 0 <= j + x_dir < COLS and \
                grid[i + y_dir][j + x_dir] == "@":
                    rolls_of_paper += 1

    if rolls_of_paper < 4:
        return True
    return False


part1 = 0
for i in range(ROWS):
    for j in range(COLS):
        check = paper_is_accessible(i, j)
        if check == -1:
            continue

        if check:
            part1 += 1

part2 = 0
paper_to_remove = [""]
while paper_to_remove:
    paper_to_remove = []
    for i in range(ROWS):
        for j in range(COLS):
            check = paper_is_accessible(i, j)
            if check == -1:
                continue

            if check:
                paper_to_remove.append((i, j))
                part2 += 1

    for i, j in paper_to_remove:
        grid[i][j] = "."

print(f"The answer to part 1 is {part1}")
print(f"The answer to part 2 is {part2}")

