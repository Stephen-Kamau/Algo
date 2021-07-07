​# O(log(n)) time | O(1) space
def binarySearch(array , target):
    """
    Write a function that takes in a sorted array of
    integers as well as a target integer. The function should use the
    Binary Search algorithm to find if the target number is
    contained in the array and should return its index if it is, otherwise -1.
    Returns position of the target in the array
    """
    left = 0
    right = len(array)-1

    while(left < right):
        mid = (left+right)//2
        if array[mid]== target:
            return mid
        if target >array[mid]:
            left =mid+1
        if target < array[mid]:
            right = midd-1
    return -1


res = binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 720)
print(res)
