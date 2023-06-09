class Node:
    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p
    def __str__(self):
        return "(" + str(self.data) + ")"
    
class LinkedList:
    def __init__(self, r=None):
        self.root=r
        self.size=0

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def find(self ,d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node=this_node.next_node
        return None
    
    def remove(self, d):
        this_node = self.root
        prev_node = None

        while this_node is not None:
            if this_node.data == d:
                prev_node.next_node == this_node.next_node #data is non-root
            else:
                self.root = this_node.next_node #data is root
            self.size -=1
            return True
        
    def print_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end="=>")
        print(None)

