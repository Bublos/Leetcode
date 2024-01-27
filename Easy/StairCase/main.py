"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

#Fibonacci
def climbStairs(n):
        """
        :type n: int
        :rtype: int
        """
        a,b=0,1
        output=0
        
        for _ in range(n):
            output+=a
            a,b=b,a+b
        return output+1
        
    

print(climbStairs(6))