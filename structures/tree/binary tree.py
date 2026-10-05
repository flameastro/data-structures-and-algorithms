from colorama import Fore, Style, init

init()

RED = Fore.RED
BLUE = Fore.BLUE

# Left - Blue
# Right - Red


class Node:
	def __init__(self, value, right = None, left = None):
		self.value = value
		self.right = right
		self.left = left


D = Node("D")
W = Node("W")
F = Node("F")
G = Node("G")
E = Node("E", None, W)
B = Node("B", D, E)
C = Node("C", F, G)
A = Node("A", B, C)


class BinaryTree:
	def __init__(self, root):
		self.root = root

	def visualize(self, father = None, i = 0, strside = None):
		if not father:
			father = self.root

		if strside == "right":
			print(f"{" " * i}{RED + father.value}{Style.RESET_ALL}")
		elif strside == "left":
			print(f"{" " * i}{BLUE + father.value}{Style.RESET_ALL}")
		else:
			# Root
			print(f"{" " * i}{father.value}")

		if father.right:
			self.visualize(father.right, i + 2, "right")

		if father.left:
			self.visualize(father.left, i + 2, "left")

	def is_empty(self):
		return not self.root

	def add(self, father_node, node, father = None):
		if not father:
			father = self.root
			if father.value == father_node:
				new_node = Node(node)
				if not father.right:
					father.right = new_node
				elif not father.left:
					father.left = new_node
				else:
					print("Already have two children")

		def mould(father_node, node, side):
			if side:
				if side.value == father_node:
					new_node = Node(node)

					if not side.right:
						side.right = new_node
					elif not side.left:
						side.left = new_node
					else:
						print("Already have two children")

				self.add(father_node, node, side)

		mould(father_node, node, father.right)
		mould(father_node, node, father.left)

	def leafs(self, father = None):
		if not father:
			father = self.root

		if not father.right and not father.left:
			print(father.value)

		if father.right:
			self.leafs(father.right)

		if father.left:
			self.leafs(father.left)

	def remove(self, node, father = None):
		if not father:
			father = self.root

			if father.value == node:
				father.right = None
				father.left = None

		if father.right:
			if father.right.value == node:
				father.right = None

		if father.left:
			if father.left.value == node:
				father.left = None

		if father.right:
			self.remove(node, father.right)

		if father.left:
			self.remove(node, father.left)


tree = BinaryTree(A)
