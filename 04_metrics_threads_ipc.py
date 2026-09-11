import threading
import multiprocessing

data = [
    ["P1", 0, 5],
    ["P2", 1, 3],
    ["P3", 2, 4]
]


def calculate():
    time = 0
    for p in data:
        time = max(time, p[1])
        start = time
        time += p[2]
        ct = time
        tat = ct - p[1]
        wt = tat - p[2]
        rt = start - p[1]
        p += [ct, tat, wt, rt]


def show_metrics():
    print("\n===== SCHEDULING METRICS =====")
    print("PID  AT  BT  CT  TAT  WT  RT")

    for p in data:
        print(p)

    print("\nAverage TAT:", round(sum(p[4] for p in data)/len(data), 2))
    print("Average WT :", round(sum(p[5] for p in data)/len(data), 2))
    print("Average RT :", round(sum(p[6] for p in data)/len(data), 2))


def thread1():
    print("Thread 1 ID:", threading.get_ident())
    print("Calculating Waiting Time")


def thread2():
    print("Thread 2 ID:", threading.get_ident())
    print("Calculating Turnaround Time")


def sender(pipe):
    pipe.send("Hello from Sender")
    pipe.close()


def receiver(pipe):
    print("Received:", pipe.recv())
    pipe.close()


if __name__ == "__main__":
    calculate()
    show_metrics()

    print("\n===== THREADS =====")
    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Both threads completed.")

    print("\n===== IPC =====")
    a, b = multiprocessing.Pipe()

    p1 = multiprocessing.Process(target=sender, args=(a,))
    p2 = multiprocessing.Process(target=receiver, args=(b,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("IPC completed successfully.")