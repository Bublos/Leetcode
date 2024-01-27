#Opět je důležité převést seznam na set, kvůli duplikacím
def findDisappearedNumbers(nums):
        output =[]
        nums_s=set(nums)
        for i in range(1,len(nums)+1):
            if i not in nums_s:
                output.append(i)
        return output

nums = [4,3,2,7,8,2,3,1]

print(findDisappearedNumbers(nums))