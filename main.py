class mystack:
    def __init__(self):
        self.data = []

    # Len of stack
    def length(self):
        return len(self.data)

    # check if stack is empty
    def is_full(self):
        if self.length() == 10:
            return True
        else:
            return False

    def push(self, element):
        if len(self.data) < 10:
            self.data.append(element)
        else:
            return "overflow"

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        else:
            return "underflow"


a = mystack()
a.push(10)
a.push(20)
a.push(60)
a.push(70)
a.push(80)
print(a.length())
print(a.is_full())
print(a.data)
print(a.push(20))
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
