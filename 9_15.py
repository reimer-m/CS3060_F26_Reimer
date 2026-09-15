def countdown(n):
    if n<=0:
        print('Blastoff')
    else:
        print(n)
        countdown(n-1)

countdown(3)

import sys
sys.setrecursionlimit(1100)

n = 0
def countdown(n):
    print(n)
    n = n+1
    countdown(n)
countdown(n)

def countdown():
    countdown()

countdown()