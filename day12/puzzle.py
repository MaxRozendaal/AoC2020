import re

def changeCourse(input: list, transformations: dict) -> int:
    # Initially heading eastwards from (0, 0)
    pos = 0 + 0j
    heading = 1 + 0j

    # Loop over actions given
    for line in input:
        direction, change = line[0]
        if direction == "F":
            pos += change * heading
        elif direction == "R":
            turns = int(change / 90)
            for _ in range(turns):
                heading *= -1j
        elif direction == "L":
            turns = int(change / 90)
            for _ in range(turns):
                heading *= 1j
        else:
            pos += transformations[direction] * change
        
    
    return int(abs(pos.real)+abs(pos.imag))

# def changeCourseRelative(input: list, transformations: dict) -> int:


def main():
    with open("input.txt", "r") as f:
        input = [[(arg, int(change)) for arg, change in [re.findall("(\d+|\D+)", line)]] for line in f.read().split("\n")]
    
    transformations = {"N": 0 + 1j, "E": 1 + 0j, "S": 0 - 1j, "W": -1 + 0j}
    
    print(f"Answer part 1: {changeCourse(input, transformations)}")


if __name__ == "__main__":
    main()
