import math

def lcmofarray(a):
    # return the lowest common multiple of elements in an array
    lcm = a[0][2]
    for i in range(1, len(a)):
        lcm = lcm * a[i][2] // math.gcd(lcm, a[i][2])
    return lcm


def sortbyperiod(elem):
    # helper function to sort array by 3rd value in element-array
    return elem[2]


def sortbydeadline(elem):
    # helper function to sort array by 4th value in element-array
    return elem[3]


def getutil(arr):
    # Calculate the utilization from the given array
    u = 0
    for task in arr:
        u = u + (task[1] / task[2])
    return u
