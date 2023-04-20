# ransomNote = "a"
# magazine = "b"
#
#
# ransomNote = "aa"
# magazine = "ab"


ransomNote = "aa"
magazine = "aab"

def canConstruct(ransomNote: str, magazine: str):
    lst_mag = list(magazine)
    for i in ransomNote:
        if i in lst_mag:
            lst_mag.remove(i)
        else:
            return False
    return True


print(canConstruct(ransomNote, magazine))
