class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        s = set(nums)
        d = {}
        for num in s:
            if num % 2 == 0:
                d[num] = nums.count(num)
        if d == {}:
            return -1
        max_v = max(d.values())
        l = []
        for k in d:
            if d[k] == max_v:
                l.append(k)
        if len(l) == 1:
            return l[0]
        else:
            return min(l)



s = Solution()
print(s.mostFrequentEven([0,1,2,2,4,4,1]), 2)
print(s.mostFrequentEven([0,1,2,2,4,4,1]) == 2)

print(s.mostFrequentEven([4,4,4,9,2,4]), 4)
print(s.mostFrequentEven([4,4,4,9,2,4]) == 4)

print(s.mostFrequentEven([29,47,21,41,13,37,25,7]), -1)
print(s.mostFrequentEven([29,47,21,41,13,37,25,7]) ==  -1)

print(s.mostFrequentEven([0,0,0,0]), 0)
print(s.mostFrequentEven([0,0,0,0]) == 0)



