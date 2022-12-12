# First Duplicate Value AlgoExpert Medium

# TC: O(n), SC: O(n)
def firstDuplicateValue(array):
    # 
    hSet = set()
    # Iterate vals from array
    for num in array:
        if num in hSet:
            return num
        # Construct hMap
        hSet.add(num)
    
    return -1

# TC: O(n), SC: O(1)
def firstDuplicateValue(array):
    for num in array:
        absNum = abs(num)
        if array[absNum - 1] < 0:
            print(absNum)
            return absNum
        array[absNum - 1] = -1 * array[absNum-1]
    return -1