import copy, string

def box(coordinate: tuple, height: int, width: int) -> list:
    x, y = coordinate
    return [(x + i, y + j) for i in range(-1,2) for j in range(-1,2) if all([
        x + i >= 0,
        y + j >= 0,
        x + i < height,
        y + j < width,
        (x + i, y + j) != coordinate
    ])]

def iteration(layout: list) -> list:
    stable = False
    layout_copy = copy.deepcopy(layout)
    while not stable:
        # Iterate over seats in layout
        for id_row, row in enumerate(layout):
            for id_seat, seat in enumerate(row):

                # Evaluate if current position is a seat
                if seat != ".":
                    # Generate evaluation box around current position
                    evaluation_box = box((id_row, id_seat), len(layout), len(row))
                    rule_seat_count = 0
                    # Iterate over positions to evaluate around current position
                    for evaluated_position in evaluation_box:
                        i, j = evaluated_position
                        if layout[i][j] == "#":
                            rule_seat_count += 1
                    
                    if layout[id_row][id_seat] == "#" and rule_seat_count >= 4:
                        layout_copy[id_row][id_seat] = "L"
                    elif layout[id_row][id_seat] == "L" and rule_seat_count == 0:
                        layout_copy[id_row][id_seat] = "#"
    
        if layout == layout_copy:
            stable = True
        layout = copy.deepcopy(layout_copy)
    return layout

def main():
    with open("test.txt", "r") as f:
        layout = [list(line) for line in f.read().split("\n")]
    
    occupied_seats = 0
    for row in iteration(layout):
        occupied_seats += row.count("#")

    print(f"Part 1 answer: {occupied_seats}")

if __name__ == "__main__":
    main()
