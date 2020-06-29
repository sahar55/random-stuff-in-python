# Class for node generations
class Node(object):
    def __init__(self):
        self.data = ""
        self.left = 0
        self.right = 0

    def get_data(self):
        return self.data


class BinaryTree(object):
    def __init__(self):
        self.root = False

    # Inesrt new nodes to the tree, assigns the first node as a root node
    def insert(self, data) -> None:
        new_node = Node()
        new_node.data = data
        if not self.root:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                parent_node = current_node
                if new_node.data < current_node.data:
                    current_node = current_node.left
                    if current_node == 0:
                        parent_node.left = new_node
                        break
                else:
                    current_node = current_node.right
                    if current_node == 0:
                        parent_node.right = new_node
                        break
    
    
    def _get_root(self) -> Node:
        if self.root:
            return self.root

    # Checks a given value existence in the tree
    def search_tree(self, searchme):
        current_node = self.root
        while current_node.data != searchme:
            if current_node.data > searchme:
                current_node = current_node.left
            else:
                current_node = current_node.right
            if not current_node:
                return 'Nothing'

        return current_node.data

    # Traversing all root nodes first
    def _pre_order(self, current_node):
        res = []
        print('Starting with root node...')
        if current_node:
            res.append(str(current_node.data))
            print('Current Node: {node}'.format(node=str(current_node.data)))
            print('<- Left')
            res += self._pre_order(current_node.left)
            print('Right ->')
            res += self._pre_order(current_node.right)
        else:
            print('Terminal Node')
        return res

    # Traversing all Terminal nodes first
    def _post_order(self, current_node):
        res = []
        if current_node:
            res += self._post_order(current_node.left)
            res += self._post_order(current_node.right)
            res.append(current_node.data)
        return res

    # Traversing the tree in its inherent sequence 
    def _in_order(self, current_node):
        res = []
        if current_node:
            res += self._in_order(current_node.left)
            res.append(current_node.data)
            res += self._in_order(current_node.right)
        return res

    # Activates all three traversing methods and returns 3 lists
    def search(self):
        root = self._get_root()
        return self._pre_order(root), self._post_order(root), self._in_order(root)
