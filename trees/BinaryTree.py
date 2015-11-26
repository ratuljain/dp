__author__ = 'lol'
import collections
res = []
arr = []
rest = []
counter = 0
class BinaryTree():
    def __init__(self, rootid):
        self.left = None
        self.right = None
        self.rootid = rootid

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setNoderootidue(self, rootidue):
        self.rootid = rootidue

    def getNoderootidue(self):
        return self.rootid

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print root.rootid,
        self.inorder(root.right)

    def size(self, root):
        if root is None:
            return 0
        return 1 + self.size(root.left) + self.size(root.right)

    def help(self, p, q):
        if p == None and q == None: return True
        if p and q and p.rootid == q.rootid:
            return self.help(p.right, q.left) and self.help(p.left, q.right)
        return False

    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def mirror(self, root):
        if root is None:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.mirror(root.left)
        self.mirror(root.right)
        return root

    def leaf(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            return 1
        else:
            return self.leaf(root.left) + self.leaf(root.right)
        return count

    def printLevels(self, root, h):
        if root is None:
            return
        if h is 1:
            print root.rootid,
        else:
            self.printLevels(root.left, h-1)
            self.printLevels(root.right, h-1)

    def levelOrder(self, root):
        h = self.maxDepth(root)
        for i in range(h+1, 0, -1):
            self.printLevels(root, i)
            print ""

    def makeNone(self, root):
        if root is None or (root.left is None and root.right is None):
            return
        if root.left is None:
            root.left = BinaryTree(0)
        if root.right is None:
            root.right = BinaryTree(0)
        self.makeNone(root.left)
        self.makeNone(root.right)


    def childrenSum(self, root):
        l = r = 0
        if root.left is None and root.right is None:
            return True
        if root is None:
            return True
        else:
            if root.left is not None:
                l = root.left.rootid
            if root.right is not None:
                r = root.right.rootid
            return (root.rootid is (l + r)) and self.childrenSum(root.left) and self.childrenSum(root.right)

    def printSpiralLevels(self, root, h, ltr):
        if root is None:
            return
        if h is 1:
            print root.rootid,
        else:
            if ltr:
                self.printSpiralLevels(root.left, h-1, ltr)
                self.printSpiralLevels(root.right, h-1, ltr)
            else:
                self.printSpiralLevels(root.right, h-1, ltr)
                self.printSpiralLevels(root.left, h-1, ltr)

    def spiralLevelOrder(self, root):
        ltr = False
        h = self.maxDepth(root)
        for i in range(1, h+1):
            self.printSpiralLevels(root, i, ltr)
            print ""
            ltr = not ltr

    def diameter(self, root):
        if root is None:
            return
        if root.left is None or root .right is None:
            return
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        diameter = 1 + l + r
        return diameter

    def maxDia(self, root):
        return max(self.diameter(root.left), self.diameter(root.right))

    def checkheightBalance(self, root):
        if root is None:
            return True
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        diff = abs(l - r)
        return diff <= 1 and self.checkheightBalance(root.left) and self.checkheightBalance(root.right)

    def hasPathSum(self, root, sum):
        if root is None:
            return (sum is 0)
        else:
            ans = False
            Subsum = sum - root.rootid
            if sum is 0 and root.left is None and root.right is None:
                return True
            if root.left is not None:
                ans = ans or self.hasPathSum(root.left, Subsum)
            if root.right is not None:
                ans = ans or self.hasPathSum(root.right, Subsum)
            return ans

    def buildTree(self, inorder, preorder):
        if len(inorder) is 0 or len(preorder) is 0:
            return None
        root = BinaryTree(preorder[0])
        idx = inorder.index(preorder[0])
        preorder.pop(0)
        root.left = self.buildTree(inorder[0:idx], preorder)
        root.right = self.buildTree(inorder[idx+1:], preorder)
        return root

    def printLevelswidth(self, root, h):
        if root is None:
            return 0
        if h is 1:
            return 1
        else:
            return self.printLevelswidth(root.left, h-1)+self.printLevelswidth(root.right, h-1)

    def maxWidth(self, root):
        finMax = 0

        h = self.maxDepth(root)
        for i in range(1, h + 1):
            curMax = self.printLevelswidth(root, i)
            if curMax > finMax:
                finMax = curMax
        return finMax

    def subTree(self, tree, subtree):
        if subtree is None:
            return True
        if tree is None:
            return False
        if self.identicalTrees(tree, subtree):
            return True
        return self.subTree(tree.left, subtree) or self.subTree(tree.right, subtree)


    def serialize(self, root):
        if not root:
            return
        res = [str(root.rootid)]
        q = collections.deque([root])
        while q:
            front = q.popleft()
            if front.left:
                q.append(front.left)
            if front.right:
                q.append(front.right)
            res.append(str(front.left.rootid) if front.left else 'null')
            res.append(str(front.right.rootid) if front.right else 'null')
        while res and res[-1] == 'null':
            res.pop()
        return "[" + ",".join(res) + "]"

    def deserialize(self, string):
        if string == '{}':
            return None
        nodes = [None if val == 'null' else BinaryTree(int(val)) for val in string.strip('[]{}').split(',')]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left  = kids.pop()
                if kids: node.right = kids.pop()
        return root

    def isLeaf(self, root):
        if root.left is None and root.right is None:
            return True

    def rootleafPath(self, root):
        global arr
        if root is None:
            return
        arr.append(root.rootid)
        if self.isLeaf(root):
            print arr
        self.rootleafPath(root.left)
        self.rootleafPath(root.right)
        arr.pop()

    def path(self, node):
        if self.isLeaf(node):
            return [[node.rootid]]
        left_paths = [[node.rootid] + p for p in self.path(node.left)] if node.left else []
        right_paths = [[node.rootid] + p for p in self.path(node.right)] if node.right else []
        return left_paths + right_paths

    def countLeaf(self, root):
        global counter
        if not root:
            return 0
        if self.isLeaf(root):
            counter += 1
        self.countLeaf(root.left)
        self.countLeaf(root.right)
        return counter

    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)

    def countNodes(self, root):
        if not root:
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        print(leftDepth)
        print(rightDepth)

    def sumNumbers(self, root, Sm):
        if root is None:
            return 0
        res, queue = [], collections.deque([(root, "", 0)])
        while queue:
            print queue
            node, ls, s = queue.popleft()
            if node.left is None and node.right is None and s + node.rootid == Sm:
                res.append(ls+str(node.rootid))
            if node.left:
                queue.append((node.left, ls + str(node.rootid) + " ", s + node.rootid))
            if node.right:
                queue.append((node.right, ls + str(node.rootid) + " ", s + node.rootid))
        return res

    def toLinkedList(self, root):
        stack = []
        p = root
        while stack:
            if p.right:
                stack.append(p.right)
                print stack
            if p.left:
                p.right = p.left
                p.left = None
            while stack:
                x = stack.pop()
                p.right = x
            p = p.right
        return p

    def perOrderIterative(self, root):
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.right)
                stack.append(node.left)
                res.append(node.rootid)
        return res


root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
# root.left.left.left = BinaryTree(6)
# root.left.left.right = BinaryTree(7)


# root1 = BinaryTree(2)
# root1.left = BinaryTree(4)
# L.left = BinaryTree(4)
# root1.right = BinaryTree(1)
# # root1.left.left = BinaryTree(4)
# # root1.left.right = BinaryTree(5)
# # # root1.right.left = BinaryTree(2)
# # root1.right.right = BinaryTree(4)
#
# root2 = BinaryTree(20)
# root2.right = BinaryTree(8)
# root2.right.right = BinaryTree(10)
# root2.right.right.right = BinaryTree(5)



#################################################test blocks

# root.inorder(root)
# print ""
# print root.size(root)
# print root.identicalTrees(root, root1)
# print root.maxDepth(root1)
# print root.serialize(root.mirror(root))
# print root.serialize(root)
# count = 0
# print root.leaf(root)
# root.levelOrder(root)
# root.makeNone(root1)
# root.inorder(root1)
#
#
# print root.childrenSum(root1)
# root.spiralLevelOrder(root1)
# print root.maxDia(root)
# print root.checkheightBalance(root)
# print abs(-2)
# print root.hasPathSum(root1, 21)
# inorder = ["D", "B", "E", "A", "F", "C"]
# preorder = ["A", "B", "D", "E", "C", "F"]
# tree2 = root.buildTree(inorder, preorder)
# print tree2.right.rootid
# print root.subTree(root, root1)
# s = (root.serialize(root))
# print s
# p=(root.deserialize("[18, 15, 30, 40, 50, 100, 40, 8, 7, 9,null]"))
# h = root.maxDepth(p)
# print root.sumNumbers(root, 8)
x = root.toLinkedList(root)
print x.right.rootid
# print(root.serialize(p))
print root.perOrderIterative(root)
# print (s)[:1]
# print s.next()
# print s.next()
# print s.next()
# root.deserialize(s)
# print root.inorder(root.deserialize(s))
# root.rootleafPath(root)
# a = root.rootleafPath(root)
