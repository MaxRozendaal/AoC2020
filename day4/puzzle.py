import re


def fields_present(passport: dict) -> bool:
    if len(passport.keys()) == 8:
        return True
    elif len(passport.keys()) == 7 and "cid" not in passport:
        return True
    else:
        return False

def is_valid(passport: dict, validation: dict) -> bool:
    
    if not (validation["byr_min"] <= int(passport["byr"]) <= validation["byr_max"] and len(passport["byr"]) == 4):
        return False
    if not (validation["iyr_min"] <= int(passport["iyr"]) <= validation["iyr_max"] and len(passport["iyr"]) == 4):
        return False
    if not (validation["eyr_min"] <= int(passport["eyr"]) <= validation["eyr_max"] and len(passport["eyr"]) == 4):
        return False
    
    if not (passport["hgt"][-2:] == "cm" or passport["hgt"][-2:] == "in"):
            return False
    if passport["hgt"][-2:] == "cm":
        if not (validation["hgt_cm_min"] <= int(re.findall('\d+', passport["hgt"])[0]) <= validation["hgt_cm_max"]):
            return False
    if passport["hgt"][-2:] == "in":
        if not (validation["hgt_in_min"] <= int(re.findall('\d+', passport["hgt"])[0]) <= validation["hgt_in_max"]):
            return False

    if not re.compile(validation["hcl"]).match(passport["hcl"]):
        return False
    
    if passport["ecl"] not in validation["ecl"]:
        return False
    
    if len(passport["pid"]) != validation["pid"]:
        return False
    
    return True

def part1(passports: list) -> int:
    valid_count = 0
    for passport in passports:
        if fields_present(passport):
            valid_count += 1
    return valid_count

def part2(passports: list, validation: dict) -> int:
    valid_count = 0
    for passport in passports:
        if fields_present(passport):
            if is_valid(passport, validation):
                valid_count += 1
    return valid_count      

def main():
    with open("input.txt", "r") as f:
        
        input = f.read().split("\n\n")
        for i, line in enumerate(input):
            input[i] = re.sub("\n", " ", line).split()
        passports = [dict(s.split(":") for s in input[i]) for i in range(0, len(input))]

        validation = {
            "byr_min":1920,
            "byr_max":2002,
            "iyr_min":2010,
            "iyr_max":2020,
            "eyr_min":2020,
            "eyr_max":2030,
            "hgt_cm_min":150,
            "hgt_cm_max":193,
            "hgt_in_min":59,
            "hgt_in_max":76,
            "hcl": r"^#([a-f0-9]{6})$",
            "ecl":("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
            "pid":9
        }
        
        print("Part 1 answer: {}".format(part1(passports))) 
        print("Part 2 answer: {}".format(part2(passports, validation)))


if __name__ == "__main__":
    main()
