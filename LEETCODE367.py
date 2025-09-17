class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0 :
            return False 
        low = 0 
        high = num
        while low<=high:
            mid = low + (high-low)//2
            sq = mid * mid
            if sq == num :
                return True
            elif sq < num :
                low = mid +1
            else:
                high = mid - 1
        return False
        

       

        
