class node:
    left = None
    right = None

    def __init__(self, value=None):
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


node1 = node(1)
node2 = node(2)
node3 = node(3)
node4 = node(4)
node5 = node(5)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
print "node 1 left %s, right is %s" % (node1.left.getValue(), node1.right.getValue())
print "node 2 left %s, right is %s" % (node2.left.getValue(), node2.right.getValue())
swap_node(node1)

print "node 1 left %s, right is %s" % (node1.left.getValue(), node1.right.getValue())
print "node 2 left %s, right is %s" % (node2.left.getValue(), node2.right.getValue())
