class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if '*' not in p and '?' not in p and s != p:
            return False
        elif '*' not in p and len(p) != len(s):
            return False
        s_point = 0
        p_point = 0
        mat_po = -1
        st_po = -1

        while s_point < len(s):
            if p_point < len(p) and (p[p_point] == s[s_point] or p[p_point] == '?'):
                s_point += 1
                p_point += 1
            elif p_point < len(p) and p[p_point] == '*':
                mat_po = s_point
                st_po = p_point
                p_point += 1
            elif st_po != -1:
                mat_po += 1
                s_point = mat_po
                p_point = st_po + 1
            else:
                return False

        while p_point < len(p) and p[p_point] == '*':
            p_point += 1

        return p_point == len(p)

        return True


s = Solution()

print("1", s.isMatch(s="aa", p="a") == False)

print("2", s.isMatch(s="aa", p="*") == True)

print("3", s.isMatch(s="cb", p="?b") == True)

print("3", s.isMatch(s="abcd", p="a*") == True)

print('4', s.isMatch(s="asd", p="sad") == False)

print('5', s.isMatch(s="asdfgh", p="a*gh") == True)

print('5', s.isMatch(s='aaa', p='aaa') == True)

print('6', s.isMatch(s="azsxdcfv", p="az?x*") == True)

print('7', s.isMatch(s="cb", p="?a") == False)

print('8', s.isMatch(s="acdcb", p="a*c?b") == False)
