class FIFOBufferError(Exception):
    """Класс ошибок работы с циклическим FIFO-буфером"""

class BufferIsFullError(FIFOBufferError):
    """Буфер уже заполнен"""

class BufferIsEmptyError(FIFOBufferError):
    """Буфер пуст"""


class DataItem:
    __slots__ = ('data', 'next')

    def __init__(self, data):
        self.data = data
        self.next = None


class FIFOBuffer:
    """Циклический FIFO-буфер с перезаписью данных при переполнении"""

    def __init__(self, size):
        self.__size = size
        self.__count = 0
        self.__first = None
        self.__last = None

    def __add_obj(self, obj):
        di = DataItem(obj)
        if not self.__first:
            self.__first = di
            self.__last = di
            self.__count = 1
        else:
            if self.__count == self.__size:
                self.__first = self.__first.next
            else:
                self.__count += 1
            self.__last.next = di
            self.__last = di

    def add(self, *objects):
        for obj in objects:
            self.__add_obj(obj)

    def pop(self):
        if not self.__first:
            raise BufferIsEmptyError("Буффер пуст")

        data = self.__first.data
        if self.__first.next:
            self.__first = self.__first.next
            self.__count -= 1
        else:
            self.__first = None
            self.__last = None
            self.__count = 0
        return data

    def __iter__(self):
        curr = self.__first
        while curr:
            yield curr.data
            curr = curr.next
