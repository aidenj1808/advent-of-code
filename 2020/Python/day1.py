nums = []
with open("./inputs/in1.txt") as file:
    for line in file:
        line = int(line.strip())
        nums.append(line)

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == 2020:
            part1 = nums[i] * nums[j]
        for k in range(j + 1, len(nums)):
            if nums[i] + nums[j] + nums[k] == 2020:
                part2 = nums[i] * nums[j] * nums[k]

print(f"The answer to part 1 is {part1}")
print(f"The answer to part 2 is {part2}")
