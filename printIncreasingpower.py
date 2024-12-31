def printIncreasingpower(x):
    power = 1
    square = 0
    while(1):
        square = power * power
        if square > x:
            break
        print(square,end = " ")
        power += 1
printIncreasingpower(10)