"""Implementation of BFS
"""
from collections import deque

class Node:

    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = None


class BFS:

    def solve(self, root, hook=lambda x: None):
        nodes_queue = deque([root])
        visited = []

        while nodes_queue:
            current_node = nodes_queue.popleft()

            if current_node.left:
                nodes_queue.append(current_node.left)
            if current_node.right:
                nodes_queue.append(current_node.right)

            visited.append(current_node)
        
        return visited


if __name__== "__main__":
    node_20 = Node(20, None, None)
    node_40 = Node(40, None, None)
    node_60 = Node(60, None, None)
    node_500 = Node(500, None, None)

    node_60.right = node_500
    node_20.right = node_40
    node_20.left = node_60

    bfs = BFS()
    bfs.solve(root=node_20)