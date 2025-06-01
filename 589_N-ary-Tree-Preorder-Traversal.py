

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        return RecursiveSolution().preorder(root)
        # return IterativeSolution().preorder(root)

class RecursiveSolution:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(node):
            if not node:
                return
            yield node.val
            for child in node.children:
                yield from dfs(child)
        return list(dfs(root))

class IterativeSolution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            for child in reversed(node.children):
                stack.append(child)
        return result

def build_test_tree():
    class Node:
        def __init__(self, val=None, children=None):
            self.val = val
            self.children = children if children is not None else []
    node5 = Node(5)
    node6 = Node(6)
    node3 = Node(3, [node5, node6])
    node2 = Node(2)
    node4 = Node(4)
    root = Node(1, [node3, node2, node4])
    return root

if __name__ == "__main__":
    root = build_test_tree()
    sol1 = RecursiveSolution()
    sol2 = IterativeSolution()
    print(sol1.preorder(root))
    print(sol2.preorder(root))
    import timeit
    print(timeit.timeit(lambda: sol1.preorder(root), number=100))
    print(timeit.timeit(lambda: sol2.preorder(root), number=100))
