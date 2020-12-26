def main():
    with open("input.txt", "r") as f:
        input = f.read().split("\n")
    
    seat_id = set(int(line.translate(str.maketrans("FBLR", "0101")), 2) for line in input)
    hi, lo = max(seat_id), min(seat_id)
    print("Highest seat ID - {}".format(hi))
    print("Missing seat ID - {}".format(set(range(lo,hi)).difference(seat_id).pop()))
    

if __name__ == "__main__":
    main()
