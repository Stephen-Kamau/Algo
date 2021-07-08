

def SumOfTwoNums(array , target):
    """
    Get THe Sum of Two Numbers from an array to match the required target
    """
    #sort the array
    array.sort()
    NumSums = []
    left = 0
    right = len(array)-1

    while left < right:
        currSum = array[left] + array[right]
        # print(left , right , currSum)
        if currSum == target:
            NumSums.append((array[left] , array[right]))
            right -=1
            left +=1
        elif currSum > target:
            right -=1
        elif currSum < target:
            left +=1
        else:
            print("passs")
            pass
    return NumSums

# using iterations

def GetTwoSumByIteration(array , target):
    NumSums =[]
    for i in range(len(array)-1):
        for j in range(i+1 , len(array)):
            currSum = array[i]+array[j]
            if currSum == target:
                NumSums.append((array[i],array[j]))
    return NumSums

res = SumOfTwoNums([3,5,-5,8,11,1,-1,6 ,4] , 10)
print(res)
res1 = GetTwoSumByIteration([3,5,-5,8,11,1,-1,6 ,4] , 10)
print(res1)
