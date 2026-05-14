class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = [[]for i in range(0,len(nums) + 1)]
        counters = {}
        for num in nums:
            counters[num] = counters.get(num, 0) + 1
        for key, value in counters.items():
            ans[value].append(key)
        print (ans)
        final_ans = []
        for i in range(len(ans) - 1 , 0 ,-1):
            for j in ans[i]:
                final_ans.append(j)
                if len(final_ans ) == k:
                    return final_ans