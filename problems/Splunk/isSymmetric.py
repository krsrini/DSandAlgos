'''
101. Symmetric Tree
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object): 
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def isMirror(t1, t2):
            if t1 is None and t1 is None:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val) and (isMirror(t1.left, t2.right)) and (isMirror(t1.right, t2.left))

        return isMirror(root.left, root.right)

# Create the binary tree from the list representation
def create_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        current = queue.pop(0)
        if nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    return root

#root = [1,2,2,3,4,4,3]
root = [1,2,2,None,3,None,3]
root_node = create_tree(root)
Solution_instance = Solution()
print(Solution_instance.isSymmetric(root_node))