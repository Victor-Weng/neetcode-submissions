from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        charcount = 0
        strcount = 0
        payload = []

        for s in strs:
            charcount += len(str(len(s)))
            strcount += 1
            payload.append(f";{len(s)}")

        base = charcount + strcount + 1
        digits = len(str(base))
        if len(str(base + digits)) > digits:
            digits += 1

        payload.append(f";{base + digits}")
        return "".join(strs + payload)

    def decode(self, s: str) -> List[str]:
        payloadend = int(s.split(";")[-1])
        charlengths = [
            int(num) for num in s[-payloadend + 1:].split(";")[:-1]
        ]

        reconstructed = []
        i = 0
        for length in charlengths:
            reconstructed.append(s[i : i + length])
            i += length

        return reconstructed