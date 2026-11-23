class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # 0110

        digits = len(s)
        num_ones = sum([1 for n in list(s) if n == "1"])

        ans = ["0"]*digits
        
        for i in range(num_ones-1):
            ans[i] = "1"
        
        ans[-1] = "1" # make the last one a 1

        return "".join(ans)
        
        