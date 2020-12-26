def main():
    with open("input.txt", "r") as f:
        input = f.read().split("\n\n")

        count1 = count2 = 0
        for group in input:
            print(group)
            print('')
            count1 += len(set(group.replace("\n", "")))
            count2 += len(set.intersection(
                *map(set, group.split())
            ))
        print(f"Part 1 answer: {count1}")
        print(f"Part 2 answer: {count2}")
        
            

if __name__ == "__main__":
    main()