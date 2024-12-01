def twoLists(locationIDs):
    leftList = []
    rightList = []
    
    with open (locationIDs, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            leftList.append(left)
            rightList.append(right)
    
    return leftList, rightList

def totalDistance(leftList, rightList):
    leftList.sort()
    rightList.sort()
    
    totalDistance = sum(abs(a - b) for a, b in zip(leftList, rightList))
    
    return totalDistance

def similarity(leftList, rightList):
    score = 0
    for line in leftList:
        amount = rightList.count(line)
        score += line*amount

    return score


locationIDs = "locationIDs.txt"

leftList, rightList = twoLists(locationIDs)

result = totalDistance(leftList, rightList)
score = similarity(leftList, rightList)

print("Total Distance:", result)
print("Similarity score:", score)