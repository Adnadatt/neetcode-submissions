# use hashmap (pairs of numbers)
# formula: (j-i) * min(heights[i], heights[j])
# move the pointer with the smaller height
#  (used hints)
# time complexity: O(N)
# space complexity: O(1)

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0

        i = 0
        j = len(heights) - 1

        while i < j:
            area = (j - i) * min(heights[i], heights[j])

            if area > maxA:
                maxA = area
            
            if heights[i] < heights[j]:
                i += 1;
            else: 
                j -= 1;

        return maxA