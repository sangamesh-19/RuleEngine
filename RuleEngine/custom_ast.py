class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # "operator" or "operand"
        self.left = left       # left child Node
        self.right = right     # right child Node
        self.value = value     # optional value for operand nodes
