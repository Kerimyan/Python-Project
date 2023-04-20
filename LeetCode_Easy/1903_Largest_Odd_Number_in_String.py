num = "52"
#
# num = "35427"

# num = "4206"

def largestOddNumber(num):
    int_num = int(num)
    for i in num:
        if int_num % 2 != 0:
            return str(int_num)
        else:
            int_num = int_num // 10
    return ''


print(largestOddNumber(num))
