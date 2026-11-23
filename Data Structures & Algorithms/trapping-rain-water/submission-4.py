class Solution:
    def trap(self, height: List[int]) -> int:
        # idea: 
        # fill numbers inwards on a new filled array then subtract differences
        # left pointer and right pointer
        # everytime a pointer moves IT FILLS THE NEW ARRAY
        # pointer with the lower number moves in until equal or higher than the pointer with larger number
        # if equal: randomly move one of the pointers in. if the new value is lower than before, fill it with the other side's value (basically the last highest value) -> while loop keeps it moving.
        if len(height) < 3:
            return 0

        l = 0
        r = len(height) - 1
        filled_list = height.copy()
        last_l = height[l]
        last_r = height[r]
        water = 0
        while l < r:
            if height[l] > last_l:
                last_l = height[l]
            elif height[r] > last_r:
                last_r = height[r]

            if height[l] < height[r]:
                # filled_list[l] = last_l
                water += last_l - height[l]
                l += 1
            elif height[r] < height[l]:
                # filled_list[r] = last_r
                water += last_r - height[r]
                r -= 1
            elif height[r] == height[l]:
                # filled_list[r] = last_r
                water += last_r - height[r]
                r-=1
        
        # water = 0
        # for i in range(len(filled_list)):
        #     water += filled_list[i] - height[i]
        return water


                