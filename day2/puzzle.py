import re

def main():
    with open("input.txt") as f:
        input = [list(filter(None,re.split('\s|-|:', x))) for x in f.readlines()]

    # Part 1
    print(len([x for x in input if int(x[0]) <= x[3].count(x[2]) <= int(x[1])]))
    # Part 2
    print(len([x for x in input if (x[3][int(x[0])-1] == x[2])
               is not (x[3][int(x[1])-1] == x[2])]))
    

if __name__ == "__main__":
    main()

    # Part 1
    # count = 0
    # for line in input:
    #     lb = int(line[0])
    #     ub = int(line[1])
    #     char = line[2]
    #     password = line[3]
    #
    #     if lb <= password.count(char) <= ub:
    #         count += 1
    #
    # print(count)

    # Part 2
    # count = 0
    # for x in input:
    #     p1 = int(x[0])
    #     p2 = int(x[1])
    #     char = x[2]
    #     password = x[3]
    #
    #     if (password[p1 - 1] == char or password[p2 - 1] == char) and password[p1 - 1] != password[p2 - 1]:
    #         count += 1
    #
    # print(count)
