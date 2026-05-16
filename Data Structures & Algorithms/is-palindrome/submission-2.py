class Solution:
    def isPalindrome(self, s: str) -> bool:
        for char in s:
            if not char.isalnum():
                s = s.replace(char,'')
        stringLen = int(len(s))
        s = s.lower()
        for i in range(stringLen // 2):
            if s[i] != s[stringLen - 1 - i]:
                return False
        return True
