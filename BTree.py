from math import ceil


class BNode:
    m: int  # Degree: It shows that it can stores at most m children and at most m-1 keys
    keys: list[int]
    is_leaf: bool  # A leaf node is a node without any children.
    # This is a list containing childrens of the node. If it's a non-leaf node it should have at most m and at least ceil(m/2) child nodes.
    parrent: object
    children: list
    # Number of child nodes are greater than number of keys by one.

    def __init__(self, m, parrent=None, is_leaf=True) -> None:
        self.m = m
        self.keys = []
        self.is_leaf = is_leaf
        self.parrent = parrent
        self.children = []

    def just_insert(self, k):
        _, ind = self.binary_search(self.keys, k)
        self.keys.insert(ind+1, k)

    def child_insert(self, node):
        _, ind = self.binary_search(self.keys, node.keys[0])
        self.children.insert(ind+1, node)

    # TODO: complete this.
    def balance(self):
        if len(self.keys) > self.m - 1:
            min_key = ceil(self.m / 2) - 1
            self.parrent.just_insert(self.keys[min_key])
            k2 = self.keys[min_key+1:]
            c2 = self.children[min_key+1:] if not self.is_leaf else []
            self.keys = self.keys[:min_key]
            self.children = self.children[:min_key+1] if not self.is_leaf else []
            new_node = BNode(self.m, parrent=self.parrent, is_leaf=self.is_leaf)
            new_node.keys = k2
            new_node.children = c2
            self.parrent.child_insert(new_node)
            self.parrent.balance()

    def insert(self, k):
        _, ind = self.binary_search(self.keys, k)
        if not self.is_leaf:
            self.children[ind+1].insert(k)
        else:
            self.keys.insert(ind+1, k)
            self.balance()

    def traverse(self) -> None:
        for i, k in enumerate(self.keys):
            if not self.is_leaf:
                self.children[i].traverse()
            print(k, end=" ")
        if not self.is_leaf:
            self.children[-1].traverse()

    def search(self, k):
        is_finded, ind = self.binary_search(self.keys, k)
        if is_finded:
            return self
        if self.is_leaf:
            return None
        return self.children[ind+1].search(k)

    @classmethod
    def binary_search(cls, arr, k, p=0, q=None):
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


class BTree:
    root: BNode
    m: int  # Degree
    min_key: int
    max_key: int
    # NOTE: Minimum number of keys in a node = ceil(m/2) - 1
    # NOTE: Maximum number of keys in a node = m - 1

    def __init__(self, m):
        self.root = None
        self.m = m
        self.min_key = ceil(m/2) - 1
        self.max_key = m - 1

    def insert(self, k) -> None:
        if self.root is not None:
            self.root.insert(k)

    def delete(self, k) -> None:
        pass

    def traverse(self) -> None:
        if self.root is not None:
            self.root.traverse()
        print()

    def search(self, k) -> BNode:
        if self.root is not None:
            self.root.search(k)
