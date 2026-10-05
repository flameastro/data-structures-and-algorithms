class Stack:
    def __init__(self, stack):
        self.stack = stack
        self.top = None if not stack else self.stack[-1]

    def show(self):
        print(self.stack)

    def pop(self):
        if not self.stack[1:]:
            self.top = None
        elif len(self.stack) == 1:
            self.top = self.stack[-1]
        else:
            self.top = self.stack[-2]

        self.stack = self.stack[:-1]
        return self.stack

    def push(self, element):
        self.top = element
        self.stack = self.stack + [element]
        return self.stack

    def top(self):
        return self.top

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0


stack = Stack([])
stack.push(4)
stack.pop()
stack.push(2)
stack.show()
