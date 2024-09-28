class Solution:
    def maxProduct(self, nums):
        mx=nums[0]
        mn=nums[0]
        x=nums[0]
        n=len(nums)
        for i in range(1,n):
            if nums[i]<0:
                mx,mn=mn,mx
            mx=max(mx*nums[i],nums[i])
            mn=min(nums[i]*mn,nums[i])
            x=max(x,mx)
        return x
sol=Solution()
x=[3,4,-5,10,2,3]
print(sol.maxProduct(x))
