import re

def main():
    with open("input.txt", "r") as f:
        timestamp, schedule = f.read().split("\n")
        schedule = [int(i) for i in schedule.split(",") if i != "x"]

    time_to_wait = dict()
    for bus in schedule:
        time_to_wait[bus] = (bus - (int(timestamp) % bus))
    bus_id = min(time_to_wait.keys(), key=lambda k: time_to_wait[k])
    print(
        bus_id * time_to_wait[bus_id]
    )

if __name__ == "__main__":
    main()
