class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def see(self):
        elements_list = []

        aux = self.head
        while aux:
            print(aux.value)
            elements_list.append(aux.value)
            aux = aux.next

        print(elements_list)

    def push(self, value):
        new_element = Node(value)

        if not self.head:
            self.head = new_element
        else:
            aux = self.head
            while aux.next:
                aux = aux.next

            aux.next = new_element

    def pop(self):
        if not self.head:
            return

        if not self.head.next:
            self.head = None
        else:
            aux = self.head
            while aux:
                if not aux.next.next:
                    aux.next = None
                    break

                aux = aux.next


linked_list = LinkedList()
linked_list.push(3)
linked_list.push(5)
linked_list.push(9)
linked_list.pop()
linked_list.see()
