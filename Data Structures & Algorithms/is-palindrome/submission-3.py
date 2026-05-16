class Solution:
    def isPalindrome(self, s: str) -> bool:
        for char in s:
            if not char.isalnum():
                s = s.replace(char,'')

        stringLen = int(len(s))

        for i in range(stringLen // 2):
            if s[i].lower() != s[stringLen - 1 - i].lower():
                return False
        return True
