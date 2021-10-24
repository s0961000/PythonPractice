class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        """
              |
            |   |
          |  |    |
        |
        """


from queue import Queue


def maxDepth(root: TreeNode) -> int:
    if root == None:
        return 0

    queue = Queue()
    queue.put(root)
    height = 0
    added_to_queue = 1

    while not queue.empty():
        num_children = 0
        while added_to_queue != 0:
            current_node = queue.get()
            added_to_queue -= 1
            if current_node.left is not None:
                queue.put(current_node.left)
                num_children += 1
            if current_node.right is not None:
                queue.put(current_node.right)
                num_children += 1
        added_to_queue = num_children
        height += 1

    return height
