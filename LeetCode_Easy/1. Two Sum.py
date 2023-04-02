def twoSum(nums: list[int], target: int):
    seen = {}
    for i, num in enumerate(nums):
        temp1 = target - num
        if temp1 in seen:
            return [seen[temp1], i]
        seen[num] = i


print(twoSum([1, 2, 3, 4, 5], 6))