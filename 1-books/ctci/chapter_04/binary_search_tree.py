class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)

        if not self.root:
            self.root = new_node
            return

        cur = self.root

        while cur:
            if cur.key > key:
                if not cur.left:
                    cur.left = new_node
                    new_node.parent = cur
                    return
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = new_node
                    new_node.parent = cur
                    return
                cur = cur.right

    def get_node(self, key):
        cur = self.root
        while cur:
            if cur.key == key:
                return cur
            if cur.key > key:
                cur = cur.left
            elif cur.key < key:
                cur = cur.right
        raise Exception("No such value in the tree")


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    bst.insert(11)
    bst.insert(14)
