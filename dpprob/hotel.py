__author__ = 'lol'
l = [7, 3, 5, 6]
l1 = [1,2,3,4,5,1]

def hotel(l, M):
    currSum = 0
    maxSum = 0
    lo = 0
    for x in range(len(l)):
        if currSum + l[x] <=M:
            currSum += l[x]
            if currSum > maxSum:
                maxSum = currSum
        else:
            while (lo <= x) and (currSum + l[x] > M):
                currSum -= l[lo]
                lo += 1
            currSum += l[x]
            if currSum > maxSum:
                maxSum = currSum
    return maxSum

print hotel(l,9)
