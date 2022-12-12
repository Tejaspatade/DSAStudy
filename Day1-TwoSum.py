def twoSumCheck(array, target):
    # We Use HasMap here and iterate through the Array Just Once.
    hashMap = {}

    for index, element in enumerate(array):
        # Compute the difference between target and curent element
        difference = target - element

        # Difference has to be in hashMap so that together current element & difference give us target
        if difference in hashMap:
            return [hashMap[difference], index]

        # If difference was absent in hashMap then we just add the current elem into hashMap
        hashMap[element] = index

    return

# Another Solution
def twoSumCheck(array, target):
    # Two pointers SC: O(1)
    left = 0
    right = len(array) - 1
    # Sort Array TC: O(nlogn)
    array.sort()
    # Traverse Array with 2 pointers TC: O(n)
    while left != right:
        sum = array[left] + array[right]
        # Found Target
        if sum == target:
            return[array[left], array[right]]
        # Sum is smaller than target
        if sum < target:
            left += 1
        # Sum is larger than target
        else:
            right -= 1
    return
