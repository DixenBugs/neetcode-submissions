
class Solution:
   def maxArea(self, heights: List[int]) -> int:
      ans = 0
      for i in range(len(heights)):
         l , r=   0 , len(heights) - i - 1
         while l < r:
            curr_area = min(heights[l], heights[r]) * (r - l)
            ans = max(ans, curr_area)
            l += 1
      return ans
     
