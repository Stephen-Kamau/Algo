

class BST:
    """
    Write a Binary Search Tree (BST) class.
    The class should have a "value" property set to be an integer,
    as well as "left" and "right" properties, both of which should
    point to either the None (null) value or to another BST.
    A node is said to be a BST node if and only if it satisfies
    the BST property: its value is strictly greater than the
    values of every node to its left; its value is less than or
    equal to the values of every node to its right; and both of its
    children nodes are either BST nodes themselves or None (null) values.
    The BST class should support insertion, searching, and removal of values.
    The removal method should only remove the first instance of the target value.
    """
    def __init__(self ,data):
        self.data = data
        self.left =None
        self.right =None

    # avg O(1) space and Olog(N) time
    #worst O(1) space and O(N) time
    def insert(self ,value):
        currNode = self

        while True:
            if value < currNode.data:
                #move leftmost
                if currNode.left is None:
                    currNode.left = BST(value)
                    break;
                else:
                    currNode = currNode.left
            else:
                #move rightmost
                if currNode.right is None:
                    currNode.right = BST(value)
                    break;
                else:
                    currNode = currNode.right

        return self

    # avg O(1) space and Olog(N) time
    #worst O(1) space and O(N) time
    def search(self , target):
        currNode = self

        while currNode is not None:
            if currNode.data == target:
                return True
            elif target < currNode.data:
                currNode = currNode.left
            else:
                currNode = currNode.right
        return False

    def delete(self , target , parentNode =None):
        currNode = self

        while currNode is not None:
            if target < currNode.data:
                parentNode = currNode
                currNode = currNode.left
            elif target > currNode.data:
                parentNode = currNode
                currNode = currNode.right
            #target == currentNode.data
            else:
                if currNode.left is not None and currNode.right is not None:
                    currNode.data = currNode.right.getMinValue()
                    # print("MOved Out",target ,self.search(target))
                    currNode.right.delete(currNode.data , currNode)

                # if we are deleting the root node as the only value in tree
                elif parentNode is None:
                    print("Parent Node is None")
                    if currNode.left is not None:
                        currNode.data = currNode.left.data
                        currNode.left = currNode.left.left.data
                        currNode.right = currNode.left.right.data
                    elif currNode.right is not None:
                        currNode.data = currNode.right.data
                        currNode.left = currNode.right.left.data
                        currNode.right = currNode.right.right.data
                    else:
                        currNode.data = None

                elif parentNode.left == currNode:
                    parentNode.left = currNode.left if currNode.left is not None else currNode.right
                elif parentNode.right == currNode:
                    parentNode.right = currNode.left if currNode.left is not None else currNode.right

                break;
        return self

    def getMinValue(self):
        currNode = self
        while currNode.left is not None:
            currNode = currNode.left
        print("Min Data is  " , currNode.data)
        return currNode.data

def PostOrderTraverse(tree , array):
    if tree is not None:
        PostOrderTraverse(tree.left, array)
        PostOrderTraverse(tree.right, array)
        array.append(tree.data)
    return array

def PreOrderTraverse(tree , array):
    if tree is not None:
        array.append(tree.data)
        PreOrderTraverse(tree.left, array)
        PreOrderTraverse(tree.right, array)
    return array

def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.data)
        inOrderTraverse(tree.right, array)
    return array

# Time Complexity: O(N)
# Space Complexity: O(N) + O(h) for stack sp
def levelHelper(root):
    array = []
    levelOrderTraverse(root , array , 0)
    return array
def levelOrderTraverse(tree , array,level):
    if tree is None:
        return;
    if len(array)<=level:
        array.append([])

    array[level].append(tree.data)
    levelOrderTraverse(tree.left , array , level+1)
    levelOrderTraverse(tree.right , array , level+1)

# space O(N)  and time O(N)
def levelOrder(root , array):
    """
    use que
    """
    from collections import deque
    q = deque()
    if root:
        q.append(root)
    while len(q):
        for i in range(len(q)):
            x = q.popleft()
            array.append(x.data)
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)

    return array

# TEST
test = (
    BST(10)
    .insert(5)
    .insert(15)
    .insert(22)
    .insert(17)
    .insert(34)
    .insert(7)
    .insert(2)
    .insert(5)
    .insert(1)
    .insert(35)
    .insert(27)
    .insert(16)
    .insert(30)
    .delete(17)
    .delete(22)
)
print("PostOrderTraverse  " ,PostOrderTraverse(test ,[]))
print("Pre order Transversal  " , PreOrderTraverse(test ,[]))
print("In order Transversal" , inOrderTraverse(test ,[]))
print("Level order Transversal" , levelHelper(test))
print("Level order Transversal using q" , levelOrder(test , []))
# print([1, 2, 5, 5, 7, 10, 15, 16, 27, 30, 34, 35])
