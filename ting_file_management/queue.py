from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        return self._data.pop(0)

    def search(self, index):
        if index < 0:
            raise IndexError("Índice Inválido ou Inexistente")
        try:
            return self._data[index]
        except IndexError:
            raise IndexError("Índice Inválido ou Inexistente")
