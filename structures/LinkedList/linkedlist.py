class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, element):
        if self.head is None:
            self.head = Node(element)
        else:
            aux = self.head
            while aux.next != None:
                aux = aux.next  

            aux.next = Node(element)

    def prepend(self, element):
        new_head = Node(element)
        new_head.next = self.head

        self.head = new_head

    def remove(self, element):
        if self.head.value == element:
            self.head = self.head.next
        else:
            aux = self.head

            while aux.next != None:
                if aux.next.value == element:
                    aux.next = aux.next.next
                    break
                aux = aux.next

    def insert(self, index, element):
        aux = self.head

        if index == 0:
            new_node = Node(element)
            new_node.next = aux
            self.head = new_node
        else:
            count = 0
            while aux.next != None:
                if count == index-1:
                    break
                aux = aux.next
                count += 1

            new_node = Node(element)
            new_node.next = aux.next
            aux.next = new_node

    def search(self, element):
        aux = self.head

        while aux != None and aux.value != element:
            aux = aux.next

        if aux:
            return aux.value

        return "Not found"

    def length(self):
        aux = self.head
        count = 0

        while aux != None:
            count += 1
            aux = aux.next

        return count

    def show(self):
        aux = self.head
        array = []

        while aux != None:
            array.append(aux.value)
            aux = aux.next

        return array


linked_list = LinkedList()
