class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        i = 0
        j = len(heights)-1
        while i < j:
            width = j-i
            new_area = width * min(heights[i], heights[j])
            if new_area > area:
                area = new_area
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return area