nums = [1,3,5,6]
target = 7

def func(nums, target):
    len_nums = len(nums)
    if target < nums[0]:
        return 0
    if target > nums[-1]:
        return len_nums
    if target in nums:
       return nums.index(target)
    else:
        for i in range(len_nums):
            if i > 0:
                if nums[i - 1] < target and nums[i] > target:
                    return i


print(func(nums, target))
