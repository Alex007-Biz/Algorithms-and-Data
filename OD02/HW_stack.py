class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Проверка, пуст ли стек."""
        return len(self.items) == 0

    def push(self, item):
        """Добавление элемента на верх стека."""
        self.items.append(item)

    def pop(self):
        """Удаление элемента с верхушки стека."""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        """Возвращает верхний элемент стека, не удаляя его."""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek at empty stack")

    def size(self):
        """Возвращает количество элементов в стеке."""
        return len(self.items)

    def __str__(self):
        return str(self.items)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Текущий стек:", stack)
print("Верхний элемент:", stack.peek())
print("Размер стека:", stack.size())
print("Удаляем элемент:", stack.pop())
print("Текущий стек после удаления:", stack)