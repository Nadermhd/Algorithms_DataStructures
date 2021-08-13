class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        prefix = ' ' * self.get_level() * 2
        prefix = prefix + '|-> ' if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level


def build_tree():
    root = TreeNode("Electronics")
    
    laptop = TreeNode("laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Samsung"))

    cellphone = TreeNode("Cellphones")
    cellphone.add_child(TreeNode("Iphone"))
    cellphone.add_child(TreeNode("Poco"))

    root.add_child(laptop)
    root.add_child(cellphone)

    root.print_tree()
    return root

root = build_tree()

root.print_tree()