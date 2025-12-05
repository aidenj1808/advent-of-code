with open("./inputs/in3.txt") as file:
    part1 = 0
    part2 = 0
    for line in file:
        batteries = [int(batterie) for batterie in line.strip()]
        max_part_1 = 0
        for i in range(len(batteries)):
            for j in range(i + 1, len(batteries)):
                joltage = batteries[i] * 10 + batteries[j]
                max_part_1 = max(max_part_1, joltage)
        part1 += max_part_1

print(part1)
            
