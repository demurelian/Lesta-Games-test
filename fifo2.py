class BufferIsEmptyError(Exception):
    """Буфер пуст"""


class FIFOBuffer:
    def __init__(self, size):
        self.__size = size
        self.__buffer = [None] * size
        self.__add_pos = 0
        self.__count = 0
        self.__pop_pos = 0

    def add(self, obj):
        self.__buffer[self.__add_pos % self.__size] = obj
        self.__add_pos += 1
        if self.__count < self.__size:
            self.__count += 1
        else:
            self.__pop_pos += 1

    def pop(self):
        if self.__count == 0:
            raise BufferIsEmptyError("Буфер пуст")

        data = self.__buffer[self.__pop_pos % self.__size]
        self.__buffer[self.__pop_pos % self.__size] = None
        self.__pop_pos += 1
        self.__count -= 1
        return data
