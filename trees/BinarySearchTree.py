__author__ = 'lol'
import collections

i = 3
class BST:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def inorder(self, root, res):
        if root is None:
            return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)
        return res

    def postorder(self, root, res):
        if root is None:
            return
        self.postorder(root.left, res)
        self.postorder(root.right, res)
        res.append(root.val)
        return res

    def serialize(self, root):
        if not root:
            return
        res = [str(root.val)]
        q = collections.deque([root])
        while q:
            front = q.popleft()
            if front.left:
                q.append(front.left)
            if front.right:
                q.append(front.right)
            res.append(str(front.left.val) if front.left else 'null')
            res.append(str(front.right.val) if front.right else 'null')
        while res and res[-1] == 'null':
            res.pop()
        return "[" + ",".join(res) + "]"

    def deserialize(self, string):
        if string == '{}':
            return None
        nodes = [None if val == 'null' else BST(int(val)) for val in string.strip('[]{}').split(',')]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    def insert(self, root, value):
        node = BST(value)
        if root is None:
            root = node

        if node.val <= root.val:
            if root.left is None:
                root.left = node
            else:
                self.insert(root.left, value)
        else:
            if root.right is None:
                root.right = node
            else:
                self.insert(root.right, value)

    def search(self, root, value):
        if root is None or root.val == value:
            return root
        if value <= root.val:
            return self.search(root.left, value)
        else:
            return self.search(root.right, value)

    def inorderSuccessor(self, root, val):
        succ = None
        curr = root
        if not root:
            return

        while curr and curr.val != val:
            if val < curr.val:
                succ = curr
                curr = curr.left
            if val > curr.val:
                curr = curr.right

        if curr.right:
            curr = curr.right
            while curr.left:
                curr = curr.left
            succ = curr

        return succ

    def preorderSuccessor(self, root, val):
        succ = None
        curr = root
        if not root:
            return

        while curr and curr.val != val:
            if val < curr.val:
                curr = curr.left
            if val > curr.val:
                succ = curr
                curr = curr.right

        if curr.left:
            curr = curr.left
            while curr.left:
                curr = curr.right
            succ = curr

        return succ

    def LCA(self, root, node1, node2):
        i = self.inorder(root, [])
        p = self.postorder(root, [])

        s = i.index(node1.val)
        f = i.index(node2.val)
        valsBtinorder = i[s:f+1]
        res = []
        for i in valsBtinorder:
            res.append(p.index(i))
        return p[max(res)]

    def nthLowest(self, root):
        if root is None:
            return
        global i
        self.nthLowest(root.left)
        if i > 0:
            i = i - 1
        else:
            return root.val

    def inorderIterative(self, root):
        k = 0
        stack = []
        curr = root
        while len(stack) != 0 or curr is not None:
            if(curr):
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                print curr.val
                curr = curr.right

    def revIn(self, root):
        stack = []
        curr = root
        while len(stack) != 0 or curr is not None:
            if(curr):
                stack.append(curr)
                curr = curr.right
            else:
                curr = stack.pop()
                print curr.val
                curr = curr.left


root = BST(20)
root.insert(root, 8)
root.insert(root, 22)
root.insert(root, 4)
root.insert(root, 12)
root.insert(root, 10)
root.insert(root, 14)

root.revIn(root)
