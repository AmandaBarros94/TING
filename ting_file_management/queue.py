class Queue:
    def __init__(self):
        self.line = list()

    def __len__(self):
        row = len(self.line)
        return row

    def enqueue(self, value):
        enqueue_in_row = self.line.append(value)
        return enqueue_in_row

    def dequeue(self):
        dequeue_in_row = self.line.pop(0)
        return dequeue_in_row

    def search(self, index):
        row = len(self.line)
        if index < 0 or index > row:
            raise IndexError
        return self.line[index]