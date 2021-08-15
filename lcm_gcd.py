from utils import time_it

@time_it
def lcm(a,b):
    '''
    LCM is the smallest positive integer that is evenly divisible by both a and b
    '''

    if a > b:
        g = a
    else:
        g = b

    while True:
        if (g % a) == 0 and (g % b) == 0:
            lcm_ = g
            break
        g += 1
    return g
@time_it
def gcd(a, b):
    '''
    GCD : greatest positive integer d such that d is a divisor of both a and b
    '''
    if a > b:
        g = a
    else:
        b > a

    gcd_ = []
    for i in range(1, g):
        if (a % i) == 0 and (b % i) == 0:
            gcd_.append(i)

    # or only
    # return (a*b)/lcm(a,b)
    return max(gcd_)


print(lcm(54, 24))

print(gcd(54, 24))