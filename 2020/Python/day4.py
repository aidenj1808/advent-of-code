with open("./inputs/in4.txt") as file:
    passports = file.read().split("\n\n")

passports_dict = {}
passport_num = 1
for passport in passports:
    fields = passport.split()
    passports_dict[passport_num] = {}
    for field in fields:
        info = field.split(':')
        passports_dict[passport_num].update({info[0]: info[1]})
    passport_num += 1

fields_needed = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
]
part1 = 0 
part2 = 0
for _, passport in passports_dict.items():
    valid = True
    for field in fields_needed:
        if field not in passport:
            valid = False

    if valid:
        part1 += 1

    for field, info in passport.items():
        match field:
            case "byr":
                if not (1920 <= int(info) <= 2002):
                    valid = False
            case "iyr":
                if not (2010 <= int(info) <= 2020):
                    valid = False
            case "eyr":
                if not (2020 <= int(info) <= 2030):
                    valid = False
            case "hgt":
                if info.endswith("cm") and not (150 <= int(info[:-2]) <= 193):
                    valid = False
                elif info.endswith("in") and not (59 <= int(info[:-2]) <= 76):
                    valid = False
            case "hcl":
                if info[0] != '#' or any([ch not in "0123456789abcdef" for ch in info[1:]]):
                    valid = False
            case "ecl":
                if info not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    valid = False
            case "pid":
                if not (info.isdigit() and len(info) == 9):
                    valid = False

    if valid:
        part2 += 1

print(f"The answer to part 1 is {part1}")
print(f"The answer to part 2 is {part2 - 1}")

