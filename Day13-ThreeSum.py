# Three Number Sum AlgoExpert Medium 

def threeNumberSum(array, targetSum):
    # Sort Input array
    array.sort()
    output = []
    for i in range(len(array)-1):
        # Left points to immediate next index
        left = i + 1
        # Right points to last position index
        right = len(array) - 1
        print(left, right)
        while left != right:
            check = array[i] + array[left] + array[right]
            # If we found match
            if check == targetSum:
                output.append([array[i], array[left], array[right]])
            # If check is smaller left++
            if check < targetSum:
                left += 1
            # If check is larger right--
            else:
                right -= 1
    return output