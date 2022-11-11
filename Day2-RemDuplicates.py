# Remove Duplicates From Sorted Array LeetCode 26
def removeDuplicates(nums):
    # The index where unique elements will start from
    index = 1
    # Iterate once starting from 1 to end of array
    for i in range(1, len(nums)):
        # If elem at current index is not equal to previous one we insert it at index and increment
        if nums[i-1] != nums[i]:
            nums[index] = nums[i]
            index += 1
    # Index stores the position where all unique elems end
    return index
