def input_data():
    while True:
        try:
            n = int(input("Number of processes: "))
            if n > 0:
                break
            print("Enter a number greater than 0.")
        except ValueError:
            print("Enter a valid number.")

    data = []
    for i in range(n):
        pid = input(f"\nProcess {i+1} ID: ")

        while True:
            try:
                at = int(input("Arrival Time: "))
                bt = int(input("Burst Time: "))
                if at >= 0 and bt > 0:
                    break
                print("Arrival >= 0 and Burst > 0.")
            except ValueError:
                print("Enter numbers only.")

        data.append([pid, at, bt, i])
    return data


def fcfs(data):
    time, result = 0, []
    for p in sorted(data, key=lambda x: (x[1], x[3])):
        if time < p[1]:
            result.append(("IDLE", time, p[1]))
            time = p[1]
        result.append((p[0], time, time + p[2]))
        time += p[2]
    return result


def sjf(data):
    left, result, time = data[:], [], 0
    while left:
        ready = [p for p in left if p[1] <= time]
        if not ready:
            next_time = min(p[1] for p in left)
            result.append(("IDLE", time, next_time))
            time = next_time
            continue
        p = min(ready, key=lambda x: (x[2], x[1], x[3]))
        result.append((p[0], time, time + p[2]))
        time += p[2]
        left.remove(p)
    return result


def show(name, result):
    print(f"\n===== {name} =====")
    print("Execution:")
    print(" -> ".join(x[0] for x in result))
    print("Intervals:")
    for x in result:
        print(x[0], ":", x[1], "-", x[2])


data = input_data()

print("\n===== ORIGINAL DATA =====")
for p in data:
    print(p[0], "AT:", p[1], "BT:", p[2])

show("FCFS", fcfs(data))
show("SJF", sjf(data))

print("\nSame original data used for both algorithms.")