from collections import deque
import sys

def order(order,num=None):
    global my_queue
    if order == 'push':
        my_queue.append(num)
    elif order == 'pop':
        if len(my_queue)!=0 : print(my_queue.popleft())
        else : print(-1)
    elif order == 'size':
        print(len(my_queue))
    elif order == 'empty':
        if len(my_queue) == 0 : print(1)
        else : print(0)
    elif order == 'front':
        if len(my_queue) != 0 : print(my_queue[0])
        else : print(-1)
    elif order == 'back':
        if len(my_queue) != 0 : print(my_queue[len(my_queue)-1])
        else : print(-1)
    else :
        return "error"

N = int(sys.stdin.readline())
my_queue = deque()
for _ in range(N) :
    order(*sys.stdin.readline().split())