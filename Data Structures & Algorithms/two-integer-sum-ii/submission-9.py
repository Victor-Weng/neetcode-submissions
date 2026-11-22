class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(1) additional space -> pointers so its in place?
        # its given as non decreasing i.e. monotonic increase
        # Only one valid solution

        curr_sum = 0
        l = 0
        r = len(numbers)-1

        while l<r:
            
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] == target:
                return [l+1,r+1]
