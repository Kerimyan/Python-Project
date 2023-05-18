# x = 123
#
# x = -123
#
# x = 120

x = 1534236469

def reverse(x):
    s = str(x)
    s_rev = s[::-1]
    if s_rev[-1] == '-':
        s_rev = s_rev[:-1]
        s_r = '-'
        s_r+=s_rev
        res = int(s_r)
    else:
        res = int(s_rev)
    if res >= 2 ** 31 - 1 or res <= -2 ** 31:
        return 0
    return res

print(reverse(x))


