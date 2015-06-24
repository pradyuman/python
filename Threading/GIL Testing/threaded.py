#Multi core - 9.343469 seconds
#Single core - 7.848209 seconds
from time import process_time
from threading import Thread

NUM = 100000000
def count(n):
    while n > 0:
        n -= 1

a = Thread(target=count, args=(NUM//2,))
b = Thread(target=count, args=(NUM//2,))
start = process_time()
a.start()
b.start()
a.join()
b.join()
print(process_time()-start)
