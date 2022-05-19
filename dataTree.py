class Node:
    def __init__(self, data, value):
        self.left = None
        self.right = None
        self.data = data
        self.value = value


root = Node(None, "Locked")

root.left = Node(1, "Locked")
root.right = Node(2, "Locked")
root.left.left = Node(3, "Locked")
root.left.right = Node(4, "Locked")
