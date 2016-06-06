import weakref

class Tree(object):

    def __init__(self, item, parent=None):
        self.item = item
        #lets use weakref to prevent memory leaks
        self._parent = weakref.ref(parent) if parent else None
        self.children = []

    def add_child(self, item):
        child = Tree(item, parent=self)
        self.children.append(child)
        return child

    @property
    def parent(self):
        if self._parent:
            return self._parent()

    def traversal(self):
        l = [self]
        for child in self.children:
            l += child.traversal()
        return l

def add_to_tree(tree, s1, e1, T):
    count = 0
    for node in tree.traversal():
        if node.item == s1:
            child = node.add_child(e1)
            break
    aux = child
    while aux.parent is not None:
        if abs(aux.parent.item - child.item) <= T:
            count += 1
        aux = aux.parent
    return count

def parse_input(inp):
    s1, e1 = inp.split(" ")
    return int(s1), int(e1)

if __name__ == "__main__":
    n, T = raw_input().split(" ")
    n, T = int(n) - 1, int(T)
    if n <= 0:
        print 0
        exit()
    count = 0
    s1, e1 = parse_input(raw_input())
    tree = Tree(s1)
    count += add_to_tree(tree, s1, e1, T)
    for i in range(n - 1):
        s1, e1 = parse_input(raw_input()) 
        count += add_to_tree(tree, s1, e1, T)
    print count
