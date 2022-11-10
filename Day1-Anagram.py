# Valid Anagram LeetCode 242

def anagramCheck(s, t):
    # Firstly, if both strings are of unequal length, it's impossible for them to be anagrams.
    if len(s) != len(t):
        return False

    # Using HashMaps for both strings
    hashMapS, hashMapT = {}, {}
    for i in range(len(s)):
        hashMapS[s[i]] = hashMapS.get(s[i], 0) + 1
        hashMapT[t[i]] = hashMapT.get(t[i], 0) + 1

    # Check for character occurences in HashMaps
    for key in hashMapS:
        if hashMapS[key] != hashMapT.get(key, 0):
            return False

    # If both the HasMaps check out to be equal the strings are therefore anagrams.
    return True
