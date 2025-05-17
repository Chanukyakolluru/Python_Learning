# multitasking- execute the functions concurrently using threading module.
#without multi threading
import threading
import time

def drop_kid_school():
    time.sleep(5)
    print("Drop the kid at school bus!")

def goto_gym():
    time.sleep(8)
    print("You go to gym after dropping the kid")

def iron_uniform():
    time.sleep(2)
    print("Iron the clothes!")

drop_kid_school()
goto_gym()
iron_uniform()

#with multi threading constructor Threading()

import threading
import time

def drop_kid_school():
    time.sleep(5)
    print("Drop the kid at school bus!")

def goto_gym():
    time.sleep(8)
    print("You go to gym after dropping the kid")

def iron_uniform():
    time.sleep(2)
    print("Iron the clothes!")

thread1 = threading.Thread(target=drop_kid_school)
thread1.start()

thread2=threading.Thread(target=goto_gym)
thread2.start()

thread3=threading.Thread(target=iron_uniform)
thread3.start()

# join method we will wait for the threads to complete
thread1.join()
thread2.join()
thread3.join()

print("All the tasks are completed!")