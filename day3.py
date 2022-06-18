class Solution(object):
    def shuffle(self, nums, n):
        rnums=[]
        for i in range(n):
            rnums.append(nums[i])
            rnums.append(nums[n+i])
        return rnums


Solution().shuffle([2,5,1,3,4,7] , 3)