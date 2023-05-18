class Solution:
    def reverseWords(self, s: str) -> str:
        lst = list(s.split(' '))
        while '' in lst:
            lst.remove('')
        lst.reverse()
        res = ''
        res = ' '.join(lst)
        return res






s = Solution()
# res = s.reverseWords("the sky is blue")
# print(res)
# print(res == "blue is sky the")
#
#
res = s.reverseWords("  hello world  ")
print(res)
print(res == "world hello")
#