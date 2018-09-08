class Solution:
    # @param root, a tree node
    # @return nothing
    def res(self, father, child):
        if child is None:
            return
        if father is None:
            self.res(child, child.left)
            self.res(child, child.right)
        else:
            if father.left == child:
                self.res(child, child.left)
                child.next = father.right
                self.res(child, child.right)
            else:
                self.res(child, child.left)
                if father.next is not None:
                    child.next = father.next.left
                self.res(child, child.right)

    def connect(self, root):
        self.res(None, root)


