

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
