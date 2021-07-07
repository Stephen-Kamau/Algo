

class BST:
    """
    BST DATASTRUCTURE IMPLIMENTATION
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self


def findClosestValueInBST(bst , target):
    """
    You are given a BST data structure consisting of BST nodes.
    Each BST node has an integer value stored in a property
    called "value" and two children nodes stored in properties called
    "left" and "right," respectively. A node is said to be a
    BST node if and only if it satisfies the BST property:
    its value is strictly greater than the values of every
    node to its left; its value is less than or equal to the
    values of every node to its right; and both of its children
    nodes are either BST nodes themselves or None (null) values.
    You are also given a target integer value; write a function
    that finds the closest value to that target value contained in the BST.
    Assume that there will only be one closest value.
    """

    currentNode = bst
    closs_val = 0
    while(currentNode is not None):
        if((target - closs_val) >abs(target - currentNode.value)):
            closs_val = currentNode.value
        if target > currentNode.value:
            # print(currentNode.right.value)
            currentNode = currentNode.right
        elif target<currentNode.value:
            currentNode = currentNode.left
        else:
            break
    return closs_val


test_case = (
    BST(100)
    .insert(5)
    .insert(15)
    .insert(5)
    .insert(2)
    .insert(1)
    .insert(22)
    .insert(1)
    .insert(1)
    .insert(3)
    .insert(1)
    .insert(1)
    .insert(502)
    .insert(55000)
    .insert(204)
    .insert(205)
    .insert(207)
    .insert(206)
    .insert(208)
    .insert(203)
    .insert(-51)
    .insert(-403)
    .insert(1001)
    .insert(57)
    .insert(60)
    .insert(4500)
)

res = findClosestValueInBST(test_case , 2000)
print(res)
