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
            hook(current_node)
        
        return visited


if __name__ == "__main__":
    import sys
    import os

    current_dir = os.path.dirname(os.path.abspath(__file__))
    utils_dir = os.path.abspath(os.path.join(current_dir, '..', 'utils'))
    sys.path.append(utils_dir)

    from tree_generator import RandomTreeGenerator
    
    tree_gen = RandomTreeGenerator(7, [0, 10])
    root = tree_gen.generate_random_tree()

    bfs = BFS()

    solved_bfs = bfs.solve(root=root)
    assert solved_bfs.__len__() == 7
    print("solved bfs length of traversal was", solved_bfs.__len__())