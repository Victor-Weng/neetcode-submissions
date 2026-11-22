from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # Pass 1: Store the product of all elements to the left of index i
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        # Pass 2: Multiply by the product of all elements to the right of index i
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output