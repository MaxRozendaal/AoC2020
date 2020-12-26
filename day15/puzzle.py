def rambunctious_recitation(end: int, input: dict) -> int:
    a = 0
    for i in range(len(input) + 1, end):
        if a in input:
            input[a], a = i, i - input[a]
        else:
            input[a], a = i, 0
    return a

def main():
    input = [0, 6, 1, 7, 2, 19, 20]
    spoken = {input[i]: i + 1 for i in range(len(input))}
    
    print(spoken)
    print(rambunctious_recitation(30000000, spoken))
    print(spoken)
    

    # for i in range(2021):


if __name__ == "__main__":
    main()
