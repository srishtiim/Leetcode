class Solution(object):
    def canJump(self, nums):
        farthestindexwecanreach = 0

        for i in range(len(nums)):
            if i > farthestindexwecanreach:
                return False

            farthestindexwecanreach = max(farthestindexwecanreach, i + nums[i])

        return True