# Validaate Subsequence AlgoExpert

def isValidSubsequence(array, sequence):
    # Pointer for sequence array traverse
    pointer = 0
    # TC: O(n) SC: O(1)
    for i in range(len(array)):
        # Check if pointer has reached end of our sequence, break loop is yes
        if pointer == len(sequence):
            return True
        # Check if current item from iteration is one in our sequence if yes increment our pointer to look for next element in our sequence
        if array[i] == sequence[pointer]:
            pointer += 1
    # Return true if after traversal thru array, pointer points to last element of sequence otherwise some elements from sequence were missing in our array thus returning False
    return pointer == len(sequence)