class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, r = 0, len(s) - 1
        while i < r:
            while i < r and not s[i].isalnum():
                i += 1
            while r > i and not s[r].isalnum():
                r -= 1
            if s[i].lower() != s[r].lower():
                return False
            i += 1
            r -= 1

        return True
