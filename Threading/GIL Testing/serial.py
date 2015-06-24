#7.469923 seconds
from time import process_time

NUM = 100000000
def count(n):
    while n > 0:
        n -= 1

start = process_time()
count(NUM)
print(process_time()-start)
