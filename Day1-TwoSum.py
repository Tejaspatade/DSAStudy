def twoSumCheck(array, target):
    # We Use HasMap here and iterate through the Array Just Once.
    hashMap = {}

    for index, element in enumerate(array):
        # Compute the difference between target and curent element
        difference = target - element

        # Difference has to be in hashMap so that together current element & difference give us target
        if difference in hashMap:
            return [hashMap[difference], hashMap[index]]

        # If difference was absent in hashMap then we just add the current elem into hashMap
        hashMap[element] = index

    return
