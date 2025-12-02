def invalid_1(x):
    x = str(x)
    return len(x) % 2 == 0 and x[:len(x) // 2] == x[len(x) // 2:]

def invalid_2(x):
    x = str(x)
    return x in (x + x)[1: -1]

with open("./inputs/in2.txt") as file:
    part1 = 0
    part2 = 0
    line = file.read().strip().split(",")
    for ranges in line:
        first_id, last_id = [int(x) for x in ranges.split("-")]
        product_ids = [id for id in range(first_id, last_id + 1)]
        for product_id in product_ids:
            if invalid_1(product_id):
                part1 += product_id

            if invalid_2(product_id):
                part2 += product_id

print(f"The answer to part 1 is {part1}")
print(f"The answer to part 2 is {part2}")

