class Solution:
  

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def gcd1(a,b):
            while b!= 0:
                a,b = b,a%b
            return a 
        top=-1
        for x in nums:
            cur=x
            while top!=-1:
                g=gcd1(nums[top], cur)
                if g==1: break
                cur=nums[top]//g*cur
                top-=1
            top+=1
            nums[top]=cur
        return nums[:top+1]
        
