#val is the value in the graph
#

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    if not node:
        return None

    cloned = {}  

    def dfs(curr):
        if curr in cloned:
            return cloned[curr]

        # Clone the current node
        copy = Node(curr.val)
        cloned[curr] = copy

        # Recursively clone all the neighbors
        for neighbor in curr.neighbors:
            copy.neighbors.append(dfs(neighbor))

        return copy

    return dfs(node)

# leetcode builds the graph but for vscode practice, here is the build manually
adjList = [[2,4],[1,3],[2,4],[1,3]]

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

cloned = cloneGraph(node1)

