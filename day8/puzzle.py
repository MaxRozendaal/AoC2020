from typing import Tuple

def run(bootcode: list, previous_index: int = None) -> Tuple[int, int, set]:
    accumulator, op_index, ops_executed = 0, 0, set()
    
    while op_index not in ops_executed and op_index < len(bootcode):
        ops_executed.add(op_index)
        op, arg = bootcode[op_index]

        if op_index == previous_index:
            op = "nop" if op == "jmp" else "jmp"

        if op == "acc":
            accumulator += arg
            op_index += 1
            
        elif op == "nop":
            op_index += 1
            
        elif op == "jmp":
            op_index += arg
            
    
    return accumulator, op_index, ops_executed


def main():
    bootcode = []
    with open("input.txt", "r") as f:
        for line in f.read().split("\n"):
            op, arg = line.split()
            bootcode.append((op, int(arg)))

    # print(bootcode)
    accumulator, _, ops_executed = run(bootcode)
    print(f"Part 1 answer: {accumulator}")

    for previous_index in ops_executed:
        if bootcode[previous_index][0] in ("jmp", "nop"):
            accumulator, op_index, _ = run(bootcode, previous_index)
            if op_index >= len(bootcode):
                print(f"Part 2 answer: {accumulator}")
                break




if __name__ == "__main__":
    main()
  
