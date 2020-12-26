import re
from collections import defaultdict

def parse_input(data: str) -> defaultdict:
    res = defaultdict(list)
    for line in data.split('\n'):
        if line[:4] == 'mask':
            mask = line[-36:]
        if line[:3] == 'mem':
            match = re.match(r'mem\[(\d+)\] = (\d+)', line)
            res[mask].append((int(match.group(1)), int(match.group(2))))
    return res

def main():
    with open("input.txt", "r") as f:
        input = f.read()

    memory_pool = defaultdict()
    masks = parse_input(input)
    for i, mask in enumerate(masks):
        print(f"line: {i} - mask: {mask} - writes: {masks[mask]}")
        print(f"Mask in binary: {mask}")
        for mem, write in masks[mask]:
            m1 = int(mask.replace('X', '0'), 2)
            m2 = int(mask.replace('X', '1'), 2)
            print(f"memaddr: {mem} - write: {m2 & (m1 | write)}")
            memory_pool[mem] = m2 & (m1 | write)
        
    print(sum(memory_pool.values()))

if __name__ == "__main__":
    main()
