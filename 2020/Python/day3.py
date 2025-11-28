with open("./inputs/in3.txt") as file:
    map = [line.strip() for line in file]

rows = len(map)
cols = len(map[0])
trees_encountered = []
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

for right, down in slopes:
    trees = 0
    current_pos = [0, 0]
    while current_pos[1] < rows:
        if map[current_pos[1]][current_pos[0]] == '#':
            trees += 1
        current_pos[1] += down
        current_pos[0] = (current_pos[0] + right) % cols
    trees_encountered.append(trees)

part1 = trees_encountered[1]
part2 = 1
for trees in trees_encountered:
    part2 *= trees

print(f"The answer to part 1 is {part1}")
print(f"The answer to part 2 is {part2}")
