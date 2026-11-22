class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n) time
        # Sequence when the next num is +1 last num
        # sort then set

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        sorted_set = list(sorted(set(nums)))

        print(sorted_set)

        longest_sequence = 1
        current_sequence = 1
        i = 1
        while i < len(sorted_set):
            if sorted_set[i] == sorted_set[i-1]+1:
                current_sequence += 1
                if current_sequence > longest_sequence:
                    longest_sequence = current_sequence
            else:
                current_sequence = 1 # reset
            i+=1

        return longest_sequence

        