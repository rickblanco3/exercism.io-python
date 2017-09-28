class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self,length):
        self._length = length
        self._internal_list = []

    def read(self):
        if not self._internal_list:
            raise BufferEmptyException
        return self._internal_list.pop(0)

    def write(self, data):
        if len(self._internal_list) == self._length:
            raise BufferFullException
        self._internal_list.append(data)

    def clear(self):
        self._internal_list = []

    def overwrite(self, data):
        if len(self._internal_list) == self._length:
            self._internal_list.pop(0)
        self._internal_list.append(data)
