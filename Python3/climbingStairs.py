##Feel free to use this code.
## OpenSource Rulez

def climbingStairs(n):
    one = 1
    two = 1
    for i in range(n-1):
        tot = one + two
        two = one
        one = tot
    return one
