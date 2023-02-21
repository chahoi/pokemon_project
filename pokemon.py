import time
import numpy as np
import sys


#Delay printing 

def delay_print(s):
    #we need to print one charracter at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


#create pokemon class - user to create pokemon 
class Pokemon:
    def __init__(self, name, type, moves, EVs, health='===================='):
        self.name = name
        self.type = type 
        self.moves = moves
        self.EVs = EVs['ATTACK']
        self.deffense = EVs['DEFFENSE']
        self.bars = 20 #pokemon default health bar




if __name__ == '__main__':
    pass