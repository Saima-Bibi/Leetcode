class Solution(object):
    def maxProduct(self, nums):
        res=max(nums)
        currMax,currMin=1 , 1
        
        for i in  nums:
            if i==0:
                currMax,currMin=1 , 1   
                continue
            temp=currMax*i    
            currMax= max(i*currMax,i*currMin,i)
            currMin= min(temp,i*currMin,i)
            res=max(res,currMax)
        return res    