
def containsDuplicate(nums):
        nums2 = set(nums)
        #print(f"{nums}:    {nums2}")
        if len(nums2)<len(nums):
            return True
        return False

#Není optimální pro hodně čísel, trvá dlouho, než se projede celý seznam
""" def containsDuplicate(nums):
        for i in nums:
            nums.next()
            if nums.count(i)!=1:
                return True
            else:
                continue
        return False """


nums = [1,1,1,3,3,4,3,2,4,2]

print(containsDuplicate(nums))