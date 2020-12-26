from math import prod

def part1(input: list, slope: tuple) -> int:
    trees = 0
    # Initial coordinates on map
    slope_right, slope_down = (0, 0)
    length = len(input[0])
    while slope_down < len(input):
        if input[slope_down][slope_right % length] == '#':
            trees += 1
        slope_right += slope[1]
        slope_down += slope[0]
    return trees

def part2(input: list, slopes: list) -> int:
    return prod(part1(input, slope) for slope in slopes)

def main():
    with open("input.txt", "r") as f:
        input = [x.strip() for x in f.readlines()]
        
    # ('down', 'right')
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    print(part1(input, slopes[1]))
    print(part2(input, slopes))
            

if __name__ == "__main__":
    main()
