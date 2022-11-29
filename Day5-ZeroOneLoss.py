# Find Players With Zero or One Losses Leetcode 2225
"""
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
"""

class Solution:
    def findWinners(self, matches):
        # Mapping Each player's no. of losses
        counterMap = {}
        for i in range(len(matches)):
            counterMap[matches[i][0]] = counterMap.get(matches[i][0], 0) + 0
            counterMap[matches[i][1]] = counterMap.get(matches[i][1], 0) + 1
        
        # Output array with 2 arrays, one for zero loss teams & 2nd for 1 loss teams
        output = [[], []]
        for player in counterMap:
            # Check for player has 0 loss
            if counterMap[player] == 0:
                output[0].append(player)
            # Check for player has 1 loss
            if counterMap[player] == 1:
                output[1].append(player)
        
        output[0].sort()
        output[1].sort()
        return output

# Chad Solution
# class Solution:
#     def findWinners(self, matches):
#         # Convert matches to [[winner, winner, ...], [loser, loser, ...]]
#         wl = list(zip(*matches))
        
#         # Initialize lostZero to all winners.
#         # We will remove a winner if he/she loses a match.
#         lostZero = set(wl[0])
        
#         # We will append if he/she lost exactly one match.
#         lostOne = []
        
#         # count the number of matches he/she losts.
#         countLost = Counter(wl[1])
        
        
#         for key in countLost.keys():
#             # Remove a winner if he/she lost a match.
#             if countLost[key] > 0 and key in lostZero: lostZero.remove(key)
#             # Append if he/she lost exactly one match.
#             if countLost[key] == 1: lostOne.append(key)
        
#         # Sort the two lists before return
#         return [sorted(list(lostZero)),sorted(lostOne)]