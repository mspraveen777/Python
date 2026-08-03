import threading
import time


def task():
    print("The task is Running..\n")
    time.sleep(2)
    print("The task is Ended\n")


print("Start of main program\n")
t = threading.Thread(target=task)
t.start()
print("End of main program\n")
