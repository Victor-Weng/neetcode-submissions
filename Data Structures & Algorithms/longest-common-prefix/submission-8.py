from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        ans = []
        for j in range(len(strs[0])):
            char = strs[0][j]
            for s in strs[1:]:
                if j >= len(s) or s[j] != char:
                    return "".join(ans)
            ans.append(char)

        return "".join(ans)