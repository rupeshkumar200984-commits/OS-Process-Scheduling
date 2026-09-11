from collections import deque

data = [
    ["P1", 0, 5, 2],
    ["P2", 1, 3, 1],
    ["P3", 2, 4, 3],
    ["P4", 4, 2, 1]
]


def priority(data):
    left, result, time = data[:], [], 0

    while left:
        ready = [p for p in left if p[1] <= time]

        if not ready:
            t = min(p[1] for p in left)
            result.append(("IDLE", time, t))
            time = t
            continue

        p = min(ready, key=lambda x: (x[3], x[1]))
        result.append((p[0], time, time + p[2]))
        time += p[2]
        left.remove(p)

    return result


def round_robin(data, q):
    left = [p[:] + [p[2]] for p in data]
    queue, result, time = deque(), [], 0

    while left or queue:
        for p in left[:]:
            if p[1] <= time:
                queue.append(p)
                left.remove(p)

        if not queue:
            time = min(p[1] for p in left)
            continue

        p = queue.popleft()
        run = min(q, p[4])
        result.append((p[0], time, time + run))
        time += run
        p[4] -= run

        for x in left[:]:
            if x[1] <= time:
                queue.append(x)
                left.remove(x)

        if p[4] > 0:
            queue.append(p)

    return result


def show(name, result):
    print(f"\n===== {name} =====")
    print(" -> ".join(x[0] for x in result))
    for x in result:
        print(x[0], ":", x[1], "-", x[2])


print("===== PRIORITY AND ROUND ROBIN =====")
print("Priority rule: Lower number = Higher priority")

print("\nTime Quantum must be greater than 0.")
while True:
    try:
        q = int(input("Enter Time Quantum: "))
        if q > 0:
            break
        print("Invalid quantum.")
    except ValueError:
        print("Enter a number.")

show("PRIORITY", priority(data))
show("ROUND ROBIN", round_robin(data, q))

print("\nTime Quantum:", q)