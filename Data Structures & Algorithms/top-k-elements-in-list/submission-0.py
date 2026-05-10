class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        sorted_counter = sorted(counter.items(),reverse=True,key=lambda x: x[1])
        ans = []
        for i in range(k):
            ans.append(sorted_counter[i][0])
        return ans
