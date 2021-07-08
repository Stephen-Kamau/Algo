

def getSumOf3Numbers(array , target):
    """
    Write a function that takes in a non-empty array of distinct integers
    and an integer representing a target sum. The function should find all
    triplets in the array that sum up to the target sum and return a
    two-dimensional array of all these triplets. The numbers in each
    triplet should be ordered in ascending order, and the triplets
    themselves should be ordered in ascending order with respect to the
    numbers they hold. If no three numbers sum up to the target sum, the
    function should return an empty array.
    """
    #sort the array
    array.sort()
    NumSums = []

    for i in range(len(array)-2):
        right = len(array)-1
        left = i+1

        while left < right:
            # print(right  , left)
            currSum = array[i]+array[left]+array[right]

            if currSum == target:
                NumSums.append([array[i],array[left],array[right]])
                left +=1
                right -=1
            elif currSum < target:
                left +=1
            elif currSum > target:
                right -=1
            else:
                print("passs")
                pass

    return NumSums



def GetSumByIteration(array , target):
    """
    THis function uses iterations
    """
    NumSums =[]
    for i in range(len(array)-2):
        for j in range(i+1 , len(array)-1):
            for k in range(j+1 , len(array)):
                currSum = array[i]+array[j]+array[k]
                if currSum == target:
                    NumSums.append((array[i],array[j],array[k]))
    return NumSums
res1 = GetSumByIteration([12, 3, 1, 2, -6, 5, -8, 6], 0)
print(res1)
res = getSumOf3Numbers([12, 3, 1, 2, -6, 5, -8, 6], 0)
print(res)
