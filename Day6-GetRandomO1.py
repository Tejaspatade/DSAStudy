# Insert Delete GetRandom O(1) LeetCode 380
import random
class RandomizedSet:
    def __init__(self) -> None:
        # Array storing values
        self.values = list()
        # HashMap storing values mapped to their indices Space Complexity: O(n)
        self.indices = dict()


    def insert(self, value):
        # If value exists, reject insertion
        if value in self.indices: return False

        # ->Inserting value at end of array & index in hashMap
        # TC: O(1)
        self.values.append(value)
        self.indices[value] = len(self.values) - 1
        return True

    def remove(self, value):
        # If value doesn't exist, reject deletion
        if value not in self.indices: return False

        # ->Swapping value with last element in array for TC O(1) deletion
        # Retrieving index of element to be deleted
        index = self.indices[value]
        # Store last element of array here and update hashMap as well
        self.indices[self.values[-1]] = index
        self.values[index] = self.values[-1]
        # Remove value from hashMap
        self.indices.pop(value)
        # Pop last element of array
        self.values.pop()
        return True

    def getRandom(self):
        # TC:O(1)
        return random.choice(self.values)


class RandomizedSet:

    def __init__(self):
        # Store the index of each val in self.arr.
        self.indices = {}
        # Store all vals.
        self.arr = []

    def insert(self, val: int) -> bool:
        # Return False if val is already present as requested.
        if val in self.indices: return False
        
        # Append val to the array.
        # Store its index in the hashmap
        self.arr.append(val)
        self.indices[val] = len(self.arr)-1
        return True
    
    def remove(self, val: int) -> bool:
        # Return False if val is not present as requested.
        if val not in self.indices: return False
        
        # Get the index of the val that needs to be removed.
        i = self.indices[val]
        
        # Update the index of arr[-1] in the indices.
        self.indices[self.arr[-1]] = i
        
        # Move the last element to the i th position.
        self.arr[i] = self.arr[-1]
        
        # remove the last element, and remove the index of val
        self.indices.pop(val)
        self.arr.pop()
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)