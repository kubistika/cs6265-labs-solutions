import time
import sys
import random
from pwn import *

def bruteforce():
    p = log.progress('Bruteforce')
    options = [b'paper\n', b'rock\n', b'scissors\n']

    while True:
        s = remote("localhost", 1234)
        s.recv(100) # read welcome
        s.send(b"kubistika\n") # send name
        time.sleep(1)

        while True:
            s.send(random.choice(options))
            resp = s.recv(100)
            if b'Game over' in resp:
                s.close()
                break
            elif b'You win!' in resp:
                p.success('Game won!')
                return
            elif b'Tie' in resp:
                # Got a tie, try another guess
                pass

bruteforce()

