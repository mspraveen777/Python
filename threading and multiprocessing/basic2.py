import time, threading


def task(name):
    print(f"{name} is running..\n")
    time.sleep(2)
    print(f"{name} is finshed\n")


print("Main Program Start\n")
t1 = threading.Thread(target=task, args=("cooking",))
t2 = threading.Thread(target=task, args=("swimming",))
t1.start()
t2.start()
t1.join()
t2.join()
print("Main Program End\n")
