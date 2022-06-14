class Solution:
    def maxArea(self, height: List[int]) -> int:
        s = 0
        e = len(height)-1
        w = e - s
        optimal_space = w * min(height[s],height[e])
        while s!= e:
            if height[s] <= height[e]:
                s+=1
            else: e-=1
            w = e - s
            local_space= w * min(height[s],height[e])
            optimal_space= max(optimal_space, local_space)

        return optimal_space