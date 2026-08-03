import threading
import time

balance = 1000
lock = threading.Lock()  # Locking the threads to over come the race condition


def withdrawl(amount: int):
    global balance
    with lock:
        temp = balance
        time.sleep(0.001)
        balance = temp - amount


t1 = threading.Thread(target=withdrawl, args=(100,))
t2 = threading.Thread(target=withdrawl, args=(100,))
t1.start()
t2.start()
t1.join()
t2.join()

print("__Money Transfer__")
print(f"Expected - 800,   Got -{balance}")
