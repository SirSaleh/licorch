

class DFS:

    def __init__(self):
        self.visited = []

    def solveDFS(self, node, hook=lambda x: None):
        if not node:
            return 

        hook(node)

        if node not in self.visited:
            self.visited.append(node)

            self.solveDFS(node.left)
            self.solveDFS(node.right)
        
    def solve(self, root, hook=lambda x: None):
        self.solveDFS(root, hook)

        return self.visited
        


if __name__=="__main__":
    import sys
    import os

    current_dir = os.path.dirname(os.path.abspath(__file__))
    utils_dir = os.path.abspath(os.path.join(current_dir, '..', 'utils'))
    sys.path.append(utils_dir)

    from tree_generator import RandomTreeGenerator

    tree_gen = RandomTreeGenerator(7, [0, 10])
    root = tree_gen.generate_random_tree()

    dfs = DFS()

    solved_dfs = dfs.solve(root=root)
    assert solved_dfs.__len__() == 7
    print("solved DFS length of traversal was", solved_dfs.__len__())

