class BST:
    """
    BST DATASTRUCTURE IMPLIMENTATION
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values, i=0):
        # print("ENtered into the function")
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            # print(curr.ent.value)
            if current.left is None:
                current.left = BST(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BST(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


# # O(n) time | O(n) space - where n is the number of nodes in the Binary Tree
def branchBSTSums(root):
    sums = []
    FindRunningSumOfBst(root, 0, sums)
    return sums
def FindRunningSumOfBst(root  , prevSum , sums=[]):
    """
    Write a function that takes in a Binary Tree and returns a
    list of its branch sums (ordered from leftmost branch sum to
    rightmost branch sum). A branch sum is the sum of all values in a
    Binary Tree branch. A Binary Tree branch is a path of nodes in a
    tree that starts at the root node and ends at any leaf node.
    Each Binary Tree node has a value stored in a property
    called "value" and two children nodes stored in properties
    called "left" and "right," respectively. Children nodes
    can either be Binary Tree nodes themselves or the None (null) value.
    """
    if root is None:
        return sums
    currSum = root.value + prevSum
    if root.right is None and root.left is None:
        sums.append(currSum)
        return;
    # move right and left recursively
    FindRunningSumOfBst(root.left ,  currSum , sums )
    FindRunningSumOfBst(root.right , currSum ,sums )



ss = BST(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
res = branchBSTSums(ss)

print(res)
