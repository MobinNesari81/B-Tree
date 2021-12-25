'''
    Implementation of B-Tree with degree m.
'''
from math import ceil


class BNode:
    m: int  # Degree: It shows that it can stores at most m children and at most m-1 keys
    keys: list[int]
    is_leaf: bool  # A leaf node is a node without any children.
    # This is a list containing children of the node. If it's a non-leaf node it should have at most m and at least ceil(m/2) child nodes.
    tree: object # Whole tree as an object
    parrent: object # Parent of node
    children: list # Children of this node
    # Number of child nodes are greater than number of keys by one.

    def __init__(self, tree, m, parrent=None, is_leaf=True) -> None: # Initialize Node.
        self.tree = tree
        self.m = m
        self.keys = []
        self.is_leaf = is_leaf
        self.parrent = parrent
        self.children = []

    def key_insert(self, k): # Insert new key in node
        _, ind = self.binary_search(self.keys, k)
        self.keys.insert(ind+1, k)

    def child_insert(self, node): # Insert new child in node.
        _, ind = self.binary_search(self.keys, node.keys[0])
        self.children.insert(ind+1, node)

    def balance(self): # Balancing tree.
        if len(self.keys) > self.m - 1:
            min_key = ceil(self.m / 2) - 1
            promoting_key = self.keys[min_key]
            new_node = BNode(self.tree, self.m,
                             parrent=self.parrent, is_leaf=self.is_leaf)
            new_node.keys = self.keys[min_key+1:]
            new_node.children = self.children[min_key +
                                              1:] if not self.is_leaf else []
            self.keys = self.keys[:min_key]
            self.children = self.children[:min_key +
                                          1] if not self.is_leaf else []
            if self.parrent is not None:
                self.parrent.key_insert(promoting_key)
                self.parrent.child_insert(new_node)
                self.parrent.balance()
            else:
                self.parrent = BNode(self.tree, self.m, is_leaf=False)
                new_node.parrent = self.parrent
                self.tree.root = self.parrent
                self.parrent.keys = [promoting_key]
                self.parrent.children = [self, new_node]

    def insert(self, k): # Insert key into node
        _, ind = self.binary_search(self.keys, k)
        if not self.is_leaf:
            self.children[ind+1].insert(k)
        else:
            self.keys.insert(ind+1, k)
            self.balance()

    def traverse(self) -> None: # Traverse around all data in this node.
        for i, k in enumerate(self.keys):
            if not self.is_leaf:
                self.children[i].traverse()
            print(k, end=" ")
        if not self.is_leaf:
            self.children[-1].traverse()

    def search(self, k): # Search for specific key in node
        is_found, ind = self.binary_search(self.keys, k)
        if is_found:
            return self
        if self.is_leaf:
            return None
        return self.children[ind+1].search(k)

    @classmethod
    def binary_search(cls, arr, k, p=0, q=None): # Modified binary search to optimize search in node.
        if q is None:
            q = len(arr) - 1
        if q >= p:
            mid = p + (q-p) // 2
            if arr[mid] == k:
                return True, mid
            if arr[mid] >= k:
                return cls.binary_search(arr, k, p, mid-1)
            if arr[mid] <= k:
                return cls.binary_search(arr, k, mid+1, q)
        return False, q


class BTree: # Implementation of Tree.
    root: BNode
    m: int  # Degree
    min_key: int
    max_key: int
    # NOTE: Minimum number of keys in a node = ceil(m/2) - 1
    # NOTE: Maximum number of keys in a node = m - 1

    def __init__(self, m): # Initialize Tree.
        self.root = None
        self.m = m
        self.min_key = ceil(m/2) - 1
        self.max_key = m - 1

    def insert(self, k) -> None: # Insert new key into tree.
        if self.root is not None:
            self.root.insert(k)
        else:
            self.root = BNode(self, self.m, is_leaf=True)
            self.root.keys = [k]

    def delete(self, k) -> None: # Delete specific key from tree.
        pass

    def traverse(self) -> None: # Print all available data in tree.
        if self.root is not None:
            self.root.traverse()
        print()

    def search(self, k) -> BNode: # Search for a specific key among all data in tree.
        if self.root is not None:
            self.root.search(k)


bt = BTree(3)
