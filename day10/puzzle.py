from collections import deque

def main():
    with open("input.txt", "r") as f:
        input = [int(line) for line in f.read().split("\n")]
    
    input = [0] + sorted(input) + [(sorted(input)[-1] + 3)]
    
       
    
    diffs = []
    for i in range(len(input) - 1):
        if (diff := abs(input[i] - input[i + 1])) > 3:
            break
        else:
            diffs.append(diff)
    print(diffs.count(1) * diffs.count(3))

    pathways = deque([0, 0, 1])
    for adapter_id in range(1, len(input)):
        possible_paths = 0

        if adapter_id >= 3 and 0 < (input[adapter_id] - input[adapter_id - 3]) <= 3:
            possible_paths += pathways[0]
        if adapter_id >= 2 and 0 < (input[adapter_id] - input[adapter_id - 2]) <= 3:
            possible_paths += pathways[1]
        if adapter_id >= 1 and 0 < (input[adapter_id] - input[adapter_id - 1]) <= 3:
            possible_paths += pathways[2]
        
        pathways.popleft()
        pathways.append(possible_paths)
    
    print(pathways)


if __name__ == "__main__":
    main()
