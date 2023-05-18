class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        res = []
        for i in nums:
            if i < 10:
                res.append(i)
            else:
                for j in str(i):
                    res.append(int(j))

        return res




s = Solution()

res1 = s.separateDigits([13,25,83,77])
print(res1, res1 == [1,3,2,5,8,3,7,7])

res2 = s.separateDigits([7,1,3,9])
print(res2, res2== [7,1,3,9])