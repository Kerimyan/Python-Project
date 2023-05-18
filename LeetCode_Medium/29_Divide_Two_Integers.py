# dividend = 10
# divisor = 3


# dividend = 7
# divisor = -3

dividend = -2147483648
divisor = -1


def divide(dividend: int, divisor: int):
    r = dividend / divisor
    res = int(r)
    if 2**31 >= res > 2**31-1:
        res -=1
    return res

print(divide(dividend, divisor))