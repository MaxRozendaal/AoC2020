from itertools import combinations

def part1(data: list) -> int:
    for i in range(25, len(data) + 1):
        if data[i] not in map(sum, combinations([data[j] for j in range(i -25, i)], 2)):
            return data[i]

def part2(data: list, invalid_number: int) -> int:
    contiguous = []
    for i in range(len(data)):
        contiguous.clear
        for j in range(i, len(data)):
            while sum(contiguous) != invalid_number and sum(contiguous) < invalid_number:
                contiguous.append(data[j])
                continue
        
            if sum(contiguous) == invalid_number:
                break
            
    
    return(min(contiguous) + max(contiguous))
    



def main():
    with open("input.txt", "r") as f:
        input = [int(line) for line in f.read().split("\n")]
    
    invalid_number = part1(input)
    print(f"Part 1 answer: {invalid_number}")

    contiguous_start = contiguous_end = contiguous_sum = 0

    while contiguous_sum != invalid_number:
        while contiguous_sum < invalid_number:
            contiguous_sum += input[contiguous_end]
            contiguous_end += 1
        while contiguous_sum > invalid_number:
            contiguous_sum -= input[contiguous_start]
            contiguous_start += 1

    contiguous_lo, contiguous_hi = min(input[contiguous_start:contiguous_end]), max(input[contiguous_start:contiguous_end])
    print(f"Part 2 answer: {contiguous_lo + contiguous_hi}")
    

    


if __name__ == "__main__":
    main()
