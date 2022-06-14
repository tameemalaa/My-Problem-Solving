class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # g [1,2,3,4,5]
        # c [3,4,5,1.2]
        #  total [-2 , ]
        #  curr [-2,]
        
        
        curr_gas = 0
        total_gas = 0
        postion = 0
        for i in range(len(gas)):
            total_gas+= gas[i]
            total_gas-=cost[i]
            curr_gas+=gas[i]
            curr_gas-=cost[i]
            if curr_gas < 0 :
                postion = i+1
                curr_gas = 0
            
        
        
        return -1 if total_gas < 0 else postion