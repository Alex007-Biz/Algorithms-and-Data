class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Проверка, пуста ли очередь."""
        return len(self.items) == 0

    def enqueue(self, item):
        """Добавление элемента в конец очереди."""
        self.items.append(item)

    def dequeue(self):
        """Удаление элемента из начала очереди."""
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("dequeue from empty queue")

    def peek(self):
        """Возвращает первый элемент очереди, не удаляя его."""
        if not self.is_empty():
            return self.items[0]
        raise IndexError("peek at empty queue")

    def size(self):
        """Возвращает количество элементов в очереди."""
        return len(self.items)

    def __str__(self):
        return str(self.items)

# Пример использования
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Текущая очередь:", queue)
    print("Первый элемент:", queue.peek())
    print("Размер очереди:", queue.size())
    print("Удаляем элемент:", queue.dequeue())
    print("Текущая очередь после удаления:", queue)