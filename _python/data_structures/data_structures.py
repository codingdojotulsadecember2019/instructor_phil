class SLList(object):
    def __init__(self):
        self.head = None
    
    def add_to_front(self, value):
        new_node = SLNode(value)
        new_node.next = self.head
        self.head = new_node
        return self

    def print_node_values(self):
        runner = self.head
        while runner != None:
            print(runner)
            runner = runner.next


class SLNode(object):
    def __init__(self, value):
        self.val = value
        self.next = None

    def __repr__(self):
        return f'Node object with a value of {self.val}'


my_list = SLList()
# print(my_list.head)
my_list.add_to_front(1).add_to_front(2).add_to_front(3).add_to_front(4)
# print(my_list.head)
my_list.add_to_front(2)
# print(my_list.head)
my_list.add_to_front(3)
# print(my_list.head)
my_list.add_to_front(4)
# print(my_list.head)
my_list.print_node_values()
# my_node1 = SLNode(1)
# my_node2 = SLNode(2)
# my_node3 = SLNode(3)
# my_node4 = SLNode(4)

# my_node1.next = my_node2
# my_node2.next = my_node3
# my_node3.next = my_node4

# print(my_node1.val)
# print(my_node1.next)
# print(my_node2.val)
# print(my_node3.val)
# print(my_node4.val)