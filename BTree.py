from math import ceil


class BNode:
    m: int  # Degree: It shows that it can stores at most m children and at most m-1 keys
    keys: list[int]
    is_leaf: bool  # A leaf node is a node without any children.
    # This is a list containing childrens of the node. If it's a non-leaf node it should have at most m and at least ceil(m/2) child nodes.
    children: list
    # Number of child nodes are greater than number of keys by one.

    def __init__(self, m, is_leaf=True) -> None:
        self.m = m
        self.keys = []
        self.is_leaf = is_leaf
        self.children = []
        self.t = ceil(m/2)

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
        return self.children[ind].search(k)


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

    def __init__(self, m):
        self.root = None
        self.m = m

    def insert(sekf, k) -> None:
        pass

    def delete(self, k) -> None:
        pass

    def traverse(self) -> None:
        if self.root is not None:
            self.root.traverse()
        print()

    def search(self, k) -> BNode:
        if self.root is not None: # Haji rasman darim jomle minevisim:)))))))))))))
            self.root.search(k)



# print(BNode.binary_search([2, 4, 6, 8, 10], 1))