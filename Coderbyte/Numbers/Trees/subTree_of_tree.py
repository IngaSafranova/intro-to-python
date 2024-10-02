# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

class Solution(object):
    def isSubtree(self, root, subRoot):
        #  create fc to validate that is the same tree first
        def same(p,q):
            if not p and not q:
                return True
            if (p and not q) or (q and not p):
                return False
            if p.val != q.val:
                return False
            return same(p.left,q.left) and same(p.right,q.right)  

# validate that root has same tree inside
        def has_subTree(root):
            if not root:
                return False
            if same(root,subRoot):
                return True
            return has_subTree(root.left) or has_subTree(root.right)
        return has_subTree(root)              