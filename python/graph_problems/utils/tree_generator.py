import random
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return "node ("+str(self.val)+")"

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
        
        # Assign children to each node to form a valid tree
        for i in range(1, len(nodes)):
            parent_index = random.randint(0, i - 1)
            if not nodes[parent_index].left:
                nodes[parent_index].left = nodes[i]
            elif not nodes[parent_index].right:
                nodes[parent_index].right = nodes[i]
            else:
                # If both child spots are taken, force assignment to the first available slot
                queue = deque([nodes[parent_index]])
                while queue:
                    current_node = queue.popleft()
                    if not current_node.left:
                        current_node.left = nodes[i]
                        break
                    elif not current_node.right:
                        current_node.right = nodes[i]
                        break
                    else:
                        queue.append(current_node.left)
                        queue.append(current_node.right)
        
        return nodes[0]  # Return the root node

# Example usage
if __name__ == "__main__":
    tree_generator = RandomTreeGenerator(node_count=7, value_range=(1, 1000))
    root = tree_generator.generate_random_tree()
    
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
