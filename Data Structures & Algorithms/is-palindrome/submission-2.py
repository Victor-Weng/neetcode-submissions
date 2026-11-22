class Solution:
    def isPalindrome(self, s: str) -> bool:
        remove_other = [c for c in "".join(s.split()).lower() if c in list("abcdefghijklmnopqrstuvwxyz0123456789")]
        return remove_other == remove_other[::-1]