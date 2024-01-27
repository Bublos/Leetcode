"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
"""

def missingNumber(nums):
        for i in range(len(nums)+1):
            if i not in nums:
                return i
            

#Lepší optimalizace
""" def missingNumber(nums):
    length = len(nums)
    total = int((length*(length+1))/2)
    return total - sum(nums) """

nums = [9,6,4,2,3,5,7,0,1]

print(missingNumber(nums))