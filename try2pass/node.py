class Node:
    def __init__(self, token, value=None, ntype=None, children=None):
            self.token = token
            self.value = value
            self.ntype = ntype
            if children:
                self.children = children
            else:
                self.children = []

    def get_values(self):
        return str(self.token)

    def print_node(self):
        if self.children:
            for child in self.children:
                print(self.get_values(), '->', child.get_values())
                child.print_node()
