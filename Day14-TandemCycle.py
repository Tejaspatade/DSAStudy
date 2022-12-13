# Tandem bicycle AlgoExpert Easy

def tandemBicycle(redSpeeds, blueSpeeds, fastest):
    # Sorting speeds based on fastest TC:O(nlogn)
    redSpeeds.sort(reverse=True)
    blueSpeeds.sort(reverse=(not fastest))
    output = 0
    # Iterate Array TC: O(n)
    for i in range(len(redSpeeds)):
        # Add max speed between two riders of tandem cycle to output
        output += max(redSpeeds[i], blueSpeeds[i])
    return output