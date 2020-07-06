class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sa, ta = [0] * 26, [0] * 26
        for i in s:
            sa[ord(i) - ord('a')] += 1
        for j in t:
            ta[ord(j) - ord('a')] += 1
        return sa == ta
