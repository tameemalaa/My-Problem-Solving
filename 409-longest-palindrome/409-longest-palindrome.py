class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        ans = 0
        odd_exists = 0
        for i in c.keys():
            if c[i] % 2:
                odd_exists = 1
            ans += c[i]//2 *2
        return ans + odd_exists