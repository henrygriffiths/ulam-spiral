import math


def main():
    spiral = createspiral(50, False)
    printspiral(spiral, False)

def createspiral(size, printnum):
    spiral = []

    # init spiral
    for y in range(size):
        spiral.append([])
        for x in range(size):
            spiral[y].append(0)
    
    # set starting position and direction
    pos = [math.floor(size / 2) - 1, math.floor(size / 2)]
    if size % 2 == 0:
        pos[1] -= 1
    directions = {0: [1, 0], 1: [0, 1], 2: [-1, 0], 3:[0, -1]}
    direction = 3

    # create spiral
    for n in range(1, int(math.pow(size, 2)) + 1, 1):
        # if cell to left relative to direction is 0, turn left
        if spiral[pos[0] + directions[(direction + 1) % 4][0]][pos[1] + directions[(direction + 1) % 4][1]] == 0:
            direction = (direction + 1) % 4
        
        # move and set array
        pos[0] += directions[direction][0]
        pos[1] += directions[direction][1]
        if printnum:
            spiral[pos[0]][pos[1]] = n
        else:
            if isprime(n):
                spiral[pos[0]][pos[1]] = 'X'
            else:
                spiral[pos[0]][pos[1]] = ' '
    return spiral

def printspiral(spiral, spacing):
    size = len(spiral)
    for y in spiral:
        for x in y:
            print(str(x), end = '')
            if spacing:
                for n in range(len(str(int(math.pow(size, 2)))) - len(str(x)) + 1):
                    print(' ', end = '')
        print()


def isprime(num):
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True

if __name__ == '__main__':
    main()