
# num = 9669     # 9969
#
# num = 9996     # 9999

num = 9999     # 9999

def maximum69Number(num: int):
    t_list = []
    t_list.append(num)
    q = 1
    x = 0
    for i in range(len(str(num))):
        temp_num = num
        q = q * 10
        temp_val = temp_num % q - x
        x+=temp_val
        temp_num = temp_num - temp_val
        if temp_val == 9:
            val = 6 * 10**i
            temp_num = temp_num + val
            t_list.append(temp_num)
            continue
        else:
            val = 9 * 10**i
            temp_num = temp_num + val
            t_list.append(temp_num)
            continue
    return max(t_list)


print(maximum69Number(num))

