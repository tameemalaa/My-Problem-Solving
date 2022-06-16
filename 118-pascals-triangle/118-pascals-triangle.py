class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = defaultdict(list)
        for i in range(numRows):
            for j in range(i+1):
                if j == 0 or j == i:
                    dp[i].append(1)
                else : 
                    dp[i].append(dp[i-1][j-1] + dp[i-1][j])
        return [i for i in dp.values()]