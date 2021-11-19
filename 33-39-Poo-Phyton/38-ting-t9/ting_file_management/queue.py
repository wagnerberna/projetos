# Fila
class Queue:
    FIRST_ELEMENT = 0

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    # enfileirar
    def enqueue(self, value):
        return self.data.append(value)

    # desenfileirar
    def dequeue(self):
        return self.data.pop(self.FIRST_ELEMENT)

    def search(self, index):
        if index < 0:
            raise IndexError
        return self.data[index]


if __name__ == "__main__":
    teste_fila = Queue()
    # add elementos
    teste_fila.enqueue("Wagner")
    teste_fila.enqueue("Aline")
    teste_fila.enqueue("Cris")
    print(teste_fila.dequeue())
    print(teste_fila.__len__())
    print(teste_fila.search(1))
    # print(teste_fila.search(5))
