class Solution:
    def isPalindrome(self, s: str) -> bool:
        for char in s:
            if not char.isalnum():
                s = s.replace(char,'')

        stringLen = int(len(s))
        s = s.lower()
        
        return s == s[::-1]
