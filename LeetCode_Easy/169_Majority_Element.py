# nums = [3,2,3]
#
# nums = [2,2,1,1,1,2,2]
#
nums = [6,5,5]


def majorityElement(nums):
    temp_dict = {}
    for num in nums:
        if num not in temp_dict:
            temp_dict[num] = 1
        else:
            temp_dict[num]+=1
    len_num = len(nums) / 2
    for v in temp_dict:
        if temp_dict[v] >= len_num:
            return v

print(majorityElement(nums))
