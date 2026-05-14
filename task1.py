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

    def find_min(self):
        """Знаходить найменше значення у двійковому дереві пошуку."""
        if self.root is None:
            return None
        return self._find_min(self.root)

    def _find_min(self, node):
        # У BST найменший елемент знаходиться в крайньому лівому вузлі
        current = node
        while current.left is not None:
            current = current.left
        return current.key

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

    print(f"Дерево (in-order обхід): {bst.inorder()}")
    print(f"Найменше значення у дереві: {bst.find_min()}")

