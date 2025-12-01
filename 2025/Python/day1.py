with open("./inputs/in1.txt") as file:
    dial = 50
    part1 = 0
    part2 = 0
    for line in file:
        line = line.strip()
        direction, distance = line[0], int(line[1:])
        for _ in range(distance):
            if direction == "L":
                dial = (dial - 1 + 100) % 100
            else:
                dial = (dial + 1) % 100

            if dial == 0:
                part2 += 1

        if dial == 0:
            part1 += 1

print(f"The answer to part 1 is {part1}")
print(f"The answer to part 2 is {part2}")

