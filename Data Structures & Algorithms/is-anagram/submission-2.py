class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_chars_list = []
        t_chars_list = []
        for x in range(0, len(s)):
            s_chars_list.append(s[x])
            t_chars_list.append(t[x])
        s_chars_list.sort()
        t_chars_list.sort()
        if s_chars_list == t_chars_list:
            return True
        else :
            return False

