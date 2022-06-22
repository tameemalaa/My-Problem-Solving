class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        x = dict()
        def min_cost(i , c = cost):
            if i == len(cost)-1 or i == len(cost)-2 :
                x[i] = cost[i]
                return x[i]
            if i in x.keys():
                return x[i]
            x[i] = min(min_cost(i+1)+cost[i],min_cost(i+2)+cost[i])
            return x[i]
        return min(min_cost(0),min_cost(1))