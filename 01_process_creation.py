import os
import multiprocessing


def child():
    print("\n--- CHILD PROCESS ---")
    print("Child PID:", os.getpid())
    print("Parent PID:", os.getppid())
    print("Child is working...")


if __name__ == "__main__":
    print("===== PROCESS CREATION =====")
    print("Parent PID:", os.getpid())

    p = multiprocessing.Process(target=child)
    p.start()
    p.join()

    print("\nChild process finished.")

    print("\n===== FILE OPERATION =====")
    try:
        with open("test.txt", "w") as f:
            f.write("Operating Systems Practical")

        with open("test.txt", "r") as f:
            print("File data:", f.read())

        print("File operation successful.")
    except Exception as e:
        print("File error:", e)

    print("\n===== ERROR HANDLING =====")
    try:
        open("wrong_file.txt", "r")
    except FileNotFoundError:
        print("Error handled: File not found.")

    print("\nProgram completed normally.")