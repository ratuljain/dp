import collections


class BinaryTree():
    i = 0

    def __init__(self, rootid):
        self.left = None
        self.right = None
        self.rootid = rootid


class Codec:
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
    nodes = [None if val == 'null' else BinaryTree(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

def hasPathSum(self, root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    if root == None:
        return False
    if root.val == sum and (root.left == None and root.right == None):
        return True

    return hasPathSum(root.left, sum - root.val) or hasPathSum(root.right, sum - root.val)


class Node(object):
    def __init__(self, root_id, left=None, right=None):
        self.root_id = root_id
        self.left = left
        self.right = right

    def isleaf(self):
        if self.left or self.right:
            return False
        return True


def binaryTreePaths1(self, root):
    if not root:
        return []
    res, stack = [], [(root, "")]
    while stack:
        node, ls = stack.pop()
        if not node.left and not node.right:
            res.append(ls + str(node.val))
        if node.right:
            stack.append((node.right, ls + str(node.val) + "->"))
        if node.left:
            stack.append((node.left, ls + str(node.val) + "->"))
    return res


# bfs + queue
def binaryTreePaths2(self, root):
    if not root:
        return []
    res, queue = [], collections.deque([(root, "")])
    while queue:
        node, ls = queue.popleft()
        if not node.left and not node.right:
            res.append(ls + str(node.val))
        if node.left:
            queue.append((node.left, ls + str(node.val) + "->"))
        if node.right:
            queue.append((node.right, ls + str(node.val) + "->"))
    return res


# dfs recursively
def binaryTreePaths(self, root):
    if not root:
        return []
    res = []
    self.dfs(root, "", res)
    return res


def dfs(self, root, ls, res):
    if not root.left and not root.right:
        res.append(ls + str(root.val))
    if root.left:
        self.dfs(root.left, ls + str(root.val) + "->", res)
    if root.right:
        self.dfs(root.right, ls + str(root.val) + "->", res)


tree = Node(0, Node(1, Node(2), Node(3, right=Node(4))), Node(5, Node(6)))


def path(node):
    if node.isLeaf():
        return [[node.root_id]]
    left_paths = [[node.root_id] + p for p in path(node.left)] if node.left else []
    right_paths = [[node.root_id] + p for p in path(node.right)] if node.right else []
    return left_paths + right_paths




def zigzagLevelOrder(self, root):
    queue = collections.deque([root])
    res = []
    while queue:
        r = []
        for _ in range(len(queue)):
            q = queue.popleft()
            if q:
                r.append(q.val)
                queue.append(q.left)
                queue.append(q.right)
        r = r[::-1] if len(res) % 2 else r
        if r:
            res.append(r)
    return res


a = path(tree)  # => [[0, 1, 2], [0, 1, 3, 4], [0, 5, 6]]
