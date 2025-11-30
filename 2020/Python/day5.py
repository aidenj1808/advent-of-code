import math

with open("./inputs/in5.txt") as file:
    boarding_passes = file.read().split()

part1 = 0
seat_ids = []
for boarding_pass in boarding_passes:
    left_row = 0
    right_row = 127
    left_col = 0
    right_col = 7
    for letter in boarding_pass:
        if letter == 'F':
            right_row -= math.ceil((right_row - left_row) / 2)
        elif letter == 'B':
            left_row += math.ceil((right_row - left_row) / 2)
        elif letter == 'L':
            right_col -= math.ceil((right_col - left_col) / 2)
        elif letter == 'R':
            left_col += math.ceil((right_col - left_col) / 2)
    
    if boarding_pass[6] == 'B':
        row = left_row
    else:
        row = right_row

    if boarding_pass[-1] == 'L':
        col = left_col
    else:
        col = right_col
    
    seat_id = row * 8 + col
    part1 = max(part1, seat_id)
    seat_ids.append(seat_id)

all_seat_ids = set([seat_id for seat_id in range(min(seat_ids), max(seat_ids) + 1)])
part2 = all_seat_ids - set(seat_ids)

print(f"The answer to part 1 is {part1}")
print(f"The answer to part 2 is {part2}")

