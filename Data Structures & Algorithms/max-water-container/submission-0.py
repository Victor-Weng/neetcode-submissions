class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # width = ir - il
        # height = min(heights[ir],heights[il])
        # return width*height

        l = 0
        r = len(heights) - 1
        max_water = min(heights)
        while l < r:
            currwater = (r-l)*(min(heights[r],heights[l]))
            if currwater > max_water:
                max_water = currwater

            if heights[l] > heights[r]:
                r -= 1
            else:
                l +=1

        return max_water

        