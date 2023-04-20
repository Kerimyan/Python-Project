# n = 4
# time = 5
#
# n = 3
# time = 2
#
n = 18
time = 38


def passThePillow(n, time):
    second = 0
    pers = 1
    while True:
        for i in range(1, n, +1):
            pers+=1
            second+=1
            if time == second:
                return pers
        for i in range(n, 1, -1):
            pers-=1
            second+=1
            if time == second:
                return pers


print(passThePillow(n, time))