class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counters_list = []
        for str in  strs:
            counters_list.append(Counter(str))
        have_seen_numbers = []
        ans = []
        for i in range(len(strs)):
            if strs[i] in have_seen_numbers:
                continue
            else :
                have_seen_numbers.append(strs[i])
            ans.append([strs[i]])
            for j in range(i+1, len(strs)):
               if counters_list[i] == counters_list[j]:
                   ans[-1].append(strs[j])
                   have_seen_numbers.append(strs[j])
        return ans