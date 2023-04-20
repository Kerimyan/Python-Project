digits = [9,4,3,9]

def plusOne(digits: list[int]):
    if digits[-1] < 9:
        digits[-1] = digits[-1] +1
        return digits
    else:
        def list_to_int(list):
            res = 0
            for i, v in enumerate(list[::-1]):
                res += v * 10 ** i

            return (res)

        ints = list_to_int(digits) + 1

        def int_to_list(int_1):
            digits = []
            for i in str(int_1):
                digits.append(int(i))
            return digits
        return int_to_list(ints)


print(plusOne(digits))