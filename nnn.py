def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    index = 0
    for i  in range(0, len(nums)-1):
        if nums[index] == nums[index+1]:
            for j in range(index,len(nums)-1):
                nums[j] = nums[j + 1]
            #print(nums)
        else:
            index +=1
    return index+1,nums[:index+1]

nums = [1,1,2]
print(removeDuplicates(nums))
nums = [0,0,0,0,0,0,1,1,1,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4]
print(removeDuplicates(nums))
