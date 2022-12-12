# Valid Anagram LeetCode 242
"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""


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
