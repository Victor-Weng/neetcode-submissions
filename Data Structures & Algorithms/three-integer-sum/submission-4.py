class Solution:
    def twoSum(self, subnums, anchor, target):
        
        l = 0
        r = len(subnums)-1

        resp = []
        while l < r:



            if subnums[l] + subnums[r] == target:
                resp.append([anchor, subnums[l],subnums[r]])
                l += 1 # randomly chosen
                while l < r and subnums[l] == subnums[l-1]:
                    l+=1
            elif subnums[l] + subnums[r] > target:
                r -= 1
            elif subnums[l] + subnums[r] < target:
                l += 1

        return resp
            


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # idea: O(n) iteration over a 2 sum problem?

        sorted_nums = sorted(nums)
        # O(nlogn)
        ans = []

        for i,n in enumerate(sorted_nums):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue # skip same triplet
            res = self.twoSum(sorted_nums[i+1:],n,-n) # dont pass in the same number
            if len(res) > 0:
                ans += res

        return ans


