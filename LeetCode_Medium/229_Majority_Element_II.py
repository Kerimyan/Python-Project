# nums = [3, 2, 3]     #Output: [3]
#
# nums = [1]           #Output: [1]

# nums = [1,2]         #Output: [1,2]

nums = [1, 2, 3]       #Output: []
#
# nums = [3,2,3]         #Output: [3]

def majorityElement(nums):
    temp_dict = {}
    for num in nums:
        if num not in temp_dict:
            temp_dict[num] = 1
        else:
            temp_dict[num]+=1
    else:
        res_list = []
        n_3 = len(nums) / 3
        for i in temp_dict:
            if temp_dict[i] > n_3:
                res_list.append(i)
        return res_list

        # res_list = []
        # m = max(temp_dict.values())
        # for i in temp_dict:
        #     if temp_dict[i] == m:
        #         res_list.append(i)
        # return res_list

print(majorityElement(nums))



