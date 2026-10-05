class Node:
    def __init__(self, value, children = []):
        self.value = value
        self.children = children


D = Node("D")
F = Node("F")
E = Node("E")
H = Node("H")
B = Node("B", [H])
C = Node("C", [E, F])
A = Node("A", [B, C, D])


class Tree:
    def __init__(self, root):
        self.root = root

    def visualize(self, father = None, i = 0, deepth = 2):
        if not father:
            father = self.root

        if not i:
            print(father.value)

        for child in father.children:
            print(f"{' ' * deepth}{child.value}")
            self.visualize(child, i + 1, deepth + 2)

    def buscar(self, value, father = None, element = None):
        if not father:
            father = self.root

            if value == father.value:
                return father

        for child in father.children:
            if child.value == value:
                return child

            result = self.buscar(value, child, element)

            if result:
                return result

    def deepth(self, value, father = None, i = 0):
        if not father:
            father = self.root

            if father.value == value:
                return i
            else:
                i += 1

        for child in father.children:
            if child.value == value:
                return i

            result = self.deepth(value, child, i + 1)

            if result:
                return result

    def add(self, father_node, node, father = None):
        if not father:
            father = self.root

            if father.value == father_node:
                new_node = Node(node)
                father.children.append(new_node)

        for child in father.children:
            if father_node == child.value:
                new_node = Node(node)

                if not child.children:
                    child.children = [Node(node)]
                else:
                    child.children.append(new_node)
                return child

            result = self.add(father_node, node, child)
            if result:
                return result

    def remove(self, node, father = None):
        if not father:
            father = self.root

            if node == father.value:
                father.children.clear()
                return father

        for child in father.children:
            if child.value == node:
                father.children.remove(child)
                return father

            result = self.remove(node, child)
            if result:
                return result

    def is_empty(self):
        return not self.root.children

    def highest(self, highest_value = None, father = None):
        if father is None:
            father = self.root

        if highest_value is None:
            highest_value = father.value

        for child in father.children:
            if child.value > highest_value:
                highest_value = child.value

            highest_value = self.highest(highest_value, child)

        return highest_value

    def smallest(self, smallest_value = None, father = None):
        if father is None:
            father = self.root

        if smallest_value is None:
            smallest_value = father.value

        for child in father.children:
            if child.value < smallest_value:
                smallest_value = child.value

            smallest_value = self.smallest(smallest_value, child)

        return smallest_value


tree = Tree(A)
