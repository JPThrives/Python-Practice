def nearestPower (A,B):
    closest_X = None
    min_diff = float("inf")
    P = 0

    while True:
        X = A ** P
        diff = abs(X - B)

        if diff < min_diff:
            min_diff = diff
            closest_X = X
        else:
            break

        P += 1
    return closest_X

print(nearestPower(2,4))