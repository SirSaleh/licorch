import random
from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class RandomTreeGenerator:
    def __init__(self, node_count, value_range):
        self.node_count = node_count
        self.value_range = value_range
    
    def generate_random_tree(self):
        if self.node_count == 0:
            return None
        
        # Generate random values for the nodes
        values = random.sample(range(*self.value_range), self.node_count)
        nodes = [Node(val) for val in values]
        
        # Randomly assign left and right children
        for node in nodes:
            if random.choice([True, False]):
                potential_left = [n for n in nodes if n is not node and n.left is None and n.right is None]
                if potential_left:
                    node.left = random.choice(potential_left)
                    nodes.remove(node.left)
            if random.choice([True, False]):
                potential_right = [n for n in nodes if n is not node and n.left is None and n.right is None]
                if potential_right:
                    node.right = random.choice(potential_right)
                    nodes.remove(node.right)
        
        return nodes[0]  # Return the root node

# Example usage
if __name__ == "__main__":
    tree_generator = RandomTreeGenerator(node_count=4, value_range=(1, 1000))
    root = tree_generator.generate_random_tree()

    print(root)
    
    # BFS to print the tree structure
    def bfs_print(root):
        if not root:
            return
        nodes_queue = deque([root])
        while nodes_queue:
            current_node = nodes_queue.popleft()
            print(current_node.val, end=' -> ')
            if current_node.left:
                print(f"L:{current_node.left.val}", end=' ')
                nodes_queue.append(current_node.left)
            if current_node.right:
                print(f"R:{current_node.right.val}", end=' ')
                nodes_queue.append(current_node.right)
            print()

    bfs_print(root)
