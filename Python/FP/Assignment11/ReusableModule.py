class IterableStructure:
    def __init__(self):
        self._entities = []
        self._index = -1

    def __iter__(self):
        return iter(self._entities)

    def __next__(self):
        if self._index > len(self._entities) - 1:
            raise StopIteration
        else:
            self._index += 1
        return self._entities[self._index]

    def __len__(self):
        return len(self._entities)

    def __setitem__(self, key, value):
        self._entities[key] = value

    def __getitem__(self, key):
        return self._entities[key]

    def append(self, elem):
        self._entities.append(elem)

    def __delitem__(self, key):
        del self._entities[key]

    def pop(self, key):
        self._entities.pop(key - 1)

    def clear(self):
        self._entities.clear()


class ShellSort:
    def __init__(self, array):
        self.__array = array

    def shellSort(self):
        n = len(self.__array)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = self.__array[i]
                j = i
                while j >= gap and self.__array[j - gap] > temp:
                    self.__array[j] = self.__array[j - gap]
                    j -= gap
                self.__array[j] = temp
            gap //= 2


class Filter:
    def __init__(self, array, function):
        self.__array = array
        self.__function = function
        self.__result = []

    def filter(self):
        for element in self.__array:
            if self.__function(element):
                self.__result.append(element)

    def get_result(self):
        return self.__result
