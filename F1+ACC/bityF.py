import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.
class Example(object):
    def __init__(self):
        self.a = 7
        print("START")
    # game loop
    def main(self):
        while True:
            for i in range(8):
                mountain_h = int(input())  # represents the height of one mountain.
                self.a =-1
    # W rite an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # The index of the mountain to fire on.
            print('a')
ex = Example()
while(True):
    if __name__ == '__main__':
        #time.sleep(1)
        ex.main()