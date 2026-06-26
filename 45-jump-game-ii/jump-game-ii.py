class Solution(object):
    def jump(self, nums):
        jumps = 0
        currentend = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == currentend:
                jumps += 1
                currentend=farthest
        
        return jumps
        