class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
    
        factor =[2,3,5]
     
        for fact in factor:
            while n % fact == 0:
                n= n // fact
        return n ==1      