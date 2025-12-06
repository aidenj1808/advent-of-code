with open("./inputs/in5.txt") as file:
    data = file.read().split("\n\n")

fresh_ing_rngs = []
for rng in data[0].split():
    start_stop = rng.split("-")
    start, stop = int(start_stop[0]), int(start_stop[1])
    fresh_ing_rngs.append([start, stop])

ingredients = [int(x) for x in data[1].split()]

part1 = 0
for ingredient in ingredients:
    is_fresh = False
    for start, stop in fresh_ing_rngs:
        if start <= ingredient <= stop:
            is_fresh = True

    if is_fresh:
        part1 += 1

part2 = 0
fresh_ing_rngs_sorted = sorted(fresh_ing_rngs)
current_stop = -1
for start, stop in fresh_ing_rngs_sorted:
    if start <= current_stop:
        start = current_stop + 1

    if start <= stop:
        part2 += stop - start + 1
    current_stop = max(current_stop, stop)

print(f"The answer to part 1 is {part1}")
print(f"The answer to part 2 is {part2}")

