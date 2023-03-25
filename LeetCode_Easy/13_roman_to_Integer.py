s = list(input("Please input Roman only numbers::"))

r_keys = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
x = 0
ind = 0
result = 0
for i in s:
    val = r_keys[i]
    ind_2 = ind + 1
    try:
        if i == 'I' and s[ind_2] == 'V' or i == 'I' and s[ind_2] == 'X':
            result -= val
        elif i == 'X' and s[ind_2] == 'L' or i == 'X' and s[ind_2] == 'C':
            result -= val
        elif i == 'C' and s[ind_2] == 'D' or i == 'C' and s[ind_2] == 'M':
            result -= val
        else:
            result += val
    except IndexError:
        result += val
        break
    ind += 1

print(result)
