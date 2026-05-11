class Solution:
    def encode(self, strs: List[str]) -> str:
        ans = ''
        for str in strs :
            ans +=f'{len(str)}#{str}' 
        return ans

    def decode(self, s: str) -> List[str]:
        ans, i = [], 0
        while i < len(s):
            j = i
            while s[j]!= '#':
                j += 1
            
            length = int(s[i : j])
            i =  length + j + 1
            ans.append(s[j+1: length + j + 1])
        return ans

