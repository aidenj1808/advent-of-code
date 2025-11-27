with open("./inputs/in2.txt") as file:
    part1 = 0
    part2 = 0
    for line in file:
        line = line.strip().split()
        min, max = [int(x) for x in line[0].split("-")]
        letter = line[1][0]
        password = line[2]
        
        # Part 1
        if min <= password.count(letter) <= max:
            part1 += 1
        
        # Part 2
        if (password[min - 1] == letter) + (password[max - 1] == letter) == 1:
            part2 += 1

print(f"The answer to part 1 is {part1}")
print(f"The answer to part 2 is {part2}")
