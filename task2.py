class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def sum_all(self):
        """Знаходить суму всіх значень у двійковому дереві пошуку."""
        return self._sum_all(self.root)

    def _sum_all(self, node):
        if node is None:
            return 0
        # Сума поточного вузла + сума лівого піддерева + сума правого піддерева
        return node.key + self._sum_all(node.left) + self._sum_all(node.right)

    def inorder(self):
        """Обхід дерева in-order (для перевірки)."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)


if __name__ == "__main__":
    bst = BST()

    values = [10, 5, 15, 3, 7, 12, 20, 1, 4]
    print(f"Вставляємо значення: {values}")
    for val in values:
        bst.insert(val)

    inorder = bst.inorder()
    print(f"Дерево (in-order обхід): {inorder}")
    print(f"Сума вручну (для перевірки): {sum(inorder)}")
    print(f"Сума всіх значень у дереві: {bst.sum_all()}")

