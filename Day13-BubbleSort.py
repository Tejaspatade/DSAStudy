# Bubble Sort AlgoExpert Easy

def bubbleSort(array):
    # Counter
    counter = 0
    # Traverse Array Indices
    for _ in range(len(array)):
        # Nested Loop for values following i
        flagCheck = False
        for j in range(len(array) - 1 - counter):
            # Check for smaller number
            if array[j] > array[j + 1]:
                # Swapping
                flagCheck = True
                array[j], array[j + 1] = array[j + 1], array[j]
        counter += 1
        if flagCheck == False:
            break
        
    return array