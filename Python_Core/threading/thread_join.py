import threading
import time
from colorama import init, Fore, Back, Style

ls = []

def count_red(n, t):
    for i in range(1,n+1):
        ls.append(i)
        time.sleep(t)

def count_green(n, t):
    for i in range(1,n+1):
        ls.append(i)
        time.sleep(t)

x = threading.Thread(target=count_red, args=(5, 0.5))
x.start()

#keeping this here will wait until thread x is done then start the y thread ,output [1,2,3,4,5,1,2,3,4,5]
#x.join()

y = threading.Thread(target=count_green, args=(5, 0.5))
y.start()

x.join()
y.join()

print(ls)
