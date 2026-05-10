class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        have_seen_numbers = []
        ans = []
        for i in range(len(strs)):
            if strs[i] in have_seen_numbers:
                continue
            else :
                have_seen_numbers.append(strs[i])
            ans.append([strs[i]])
            for j in range(i+1, len(strs)):
               if Counter(strs[i]) == Counter(strs[j]):
                   ans[-1].append(strs[j])
                   have_seen_numbers.append(strs[j])
        return ans

