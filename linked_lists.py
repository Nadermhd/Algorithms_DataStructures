# linked_lists
# each element has a reference to the address of the next element

# Node class that represnts indivudal element
class Node:
    def __init__(self, data=None, next=None):
        # 'A node is an element that has value and pointer'
        # value
        self.data = data
        # pointer to the next element
        self.next = next 

class LinkedList:
    def __init__(self):

        # head of linkedlist
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('Linkded list is empty')
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' -> '
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)


def main():
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_end(56)
    ll.insert_at_begining(24)
    ll.print()


if __name__ == '__main__':
    main()