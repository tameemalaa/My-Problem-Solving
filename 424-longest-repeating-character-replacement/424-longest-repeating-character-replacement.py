class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c= defaultdict(int)
        ans = 0
        j=0
        for i in range(len(s)):
            c[s[i]] +=1
            while ((i-j+1)-max(c.values())) > k:
                c[s[j]] -=1
                j+=1
            ans = max(ans,i-j+1)
        return ans
            