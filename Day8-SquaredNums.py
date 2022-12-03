# Sorted Squared Array EASY AlgoExpert

def sortedSquaredArray(array):
    start = 0
    end = len(array) - 1
    output = [0 for _ in array]
    for i in reversed(range(len(array))):
        if abs(array[start]) > abs(array[end]):
            output[i] = array[start] ** 2
            start += 1
        else:
            output[i] = array[end] ** 2
            end -= 1
        
    return output