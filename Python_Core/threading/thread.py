import threading
import time
from colorama import init, Fore, Back, Style

"""
def func():
    print("hello")
    time.sleep(2)
    print("world")

x = threading.Thread(target=func)
x.start()
print(threading.active_count())
"""

#example with two func with different delats

def count_red(n):
    for i in range(1,n+1):
        print(Fore.RED + str(i))
        #time.sleep(t)

def count_green(n):
    for i in range(1,n+1):
        print(Fore.GREEN + str(i))
        #time.sleep(t)

x = threading.Thread(target=count_red, args=(10,))
x.start()

#x = threading.Thread(target=count_green, args=(10, 0.01))
y = threading.Thread(target=count_green, args=(10,))  # by chaging the sleep time , we see that the first thread runs twive 
                                                            # before this second thread is launched one
y.start()

print(Fore.BLUE + "Done")

# Threads basically run in paralelle , meaning that each thread is stoped only by the cpu , the cpu decided when to switch
# from one to other , but they are actually running just like other processes at the same time , the cpu switches from one 
# to the other , this is why this code everytime is going to give a different order , because the cpu switches happens at different
# times in each launch .

# -------------------
