__author__ = 'mark'


class node:
    left = None
    right = None

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value


def swap_node(n):
    if n is not None:
        tmp = n.left
        n.left = n.right
        n.right = tmp

        swap_node(n.left)
        swap_node(n.right)
