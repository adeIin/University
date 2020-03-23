from errors.exceptions import RepositoryError, UndoRedoError
import pickle
from infrastructure.IterableStructure import IterableStructure


class RepositoryUniqueElements(object):

    def __init__(self):
        self._entities = IterableStructure()

    def size(self):
        return len(self._entities)

    def search(self, key):
        if key not in self._entities:
            raise RepositoryError("Id not found!\n")
        for x in self._entities:
            if x == key:
                return x

    def update(self, key, element):
        if key not in self._entities:
            raise RepositoryError("Id not found!\n")
        for i in range(len(self._entities)):
            if self._entities[i] == key:
                self._entities[i] = element
                return

    def remove(self, key):
        if key not in self._entities:
            raise RepositoryError("Id not found!\n")
        for i in range(len(self._entities)):
            if self._entities[i] == key:
                del self._entities[i]
                return

    def add(self, element):
        if element in self._entities:
            raise RepositoryError("Id already exists!\n")
        self._entities.append(element)

    def get_all(self):
        return self._entities[:]


class RepositoryMultipleElements(object):

    def __init__(self):
        self._entities = IterableStructure()

    def size(self):
        return len(self._entities)

    def search(self, key):
        if key not in self._entities:
            raise RepositoryError("Id not found!\n")
        for x in self._entities:
            if x == key:
                return x

    def update(self, key):
        if key not in self._entities:
            raise RepositoryError("Id not found!\n")
        for i in range(len(self._entities)):
            if self._entities[i] == key:
                self._entities[i] = key
                return

    def remove(self, key):
        if key not in self._entities:
            raise RepositoryError("Id not found!\n")
        for i in range(len(self._entities)):
            if self._entities[i] == key:
                del self._entities[i]
                return

    def add(self, element):
        self._entities.append(element)

    def get_all(self):
        return self._entities[:]


class FileRepositoryUniqueElements(RepositoryUniqueElements):

    def __init__(self, filename, read_object, write_object):
        self.__filename = filename
        self.__read_object = read_object
        self.__write_object = write_object
        RepositoryUniqueElements.__init__(self)

    def __read_all_from_file(self):
        self._entities = IterableStructure()
        with open(self.__filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    obj = self.__read_object(line)
                    self._entities.append(obj)

    def __write_all_to_file(self):
        with open(self.__filename, "w") as f:
            for obj in self._entities:
                line = self.__write_object(obj)
                f.write(line + "\n")

    def add(self, element):
        self.__read_all_from_file()
        RepositoryUniqueElements.add(self, element)
        self.__write_all_to_file()

    def update(self, key, element):
        self.__read_all_from_file()
        RepositoryUniqueElements.update(self, key, element)
        self.__write_all_to_file()

    def remove(self, key):
        self.__read_all_from_file()
        RepositoryUniqueElements.remove(self, key)
        self.__write_all_to_file()

    def get_all(self):
        self.__read_all_from_file()
        return RepositoryUniqueElements.get_all(self)

    def search(self, key):
        self.__read_all_from_file()
        return RepositoryUniqueElements.search(self, key)


class FileRepositoryMultipleElements(RepositoryMultipleElements):

    def __init__(self, filename, read_object, write_object):
        self.__filename = filename
        self.__read_object = read_object
        self.__write_object = write_object
        RepositoryMultipleElements.__init__(self)

    def __read_all_from_file(self):
        self._entities = IterableStructure()
        with open(self.__filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    obj = self.__read_object(line)
                    self._entities.append(obj)

    def __write_all_to_file(self):
        with open(self.__filename, "w") as f:
            for obj in self._entities:
                line = self.__write_object(obj)
                f.write(line + "\n")

    def add(self, element):
        self.__read_all_from_file()
        RepositoryMultipleElements.add(self, element)
        self.__write_all_to_file()

    def update(self, key):
        self.__read_all_from_file()
        RepositoryMultipleElements.update(self, key)
        self.__write_all_to_file()

    def remove(self, key):
        self.__read_all_from_file()
        RepositoryMultipleElements.remove(self, key)
        self.__write_all_to_file()

    def get_all(self):
        self.__read_all_from_file()
        return RepositoryMultipleElements.get_all(self)

    def search(self, key):
        self.__read_all_from_file()
        return RepositoryMultipleElements.search(self, key)


class BinaryFileRepositoryUniqueElements(RepositoryUniqueElements):

    def __init__(self, filename, read_object, write_object):
        self.__filename = filename
        self.__read_object = read_object
        self.__write_object = write_object
        RepositoryUniqueElements.__init__(self)

    def __read_all_from_file(self):
        self._entities = IterableStructure()
        result = []
        try:
            f = open(self.__filename, 'rb')
            result = pickle.load(f)
        except EOFError:
            result = []
        except IOError as err:
            raise RepositoryError(err)
        if len(result) == 0:
            return []
        for i in range(len(result)):
            result[i] = result[i].strip()
            obj = self.__read_object(result[i])
            self._entities.append(obj)
        f.close()

    def __write_all_to_file(self):
        text = []
        with open(self.__filename, "wb") as f:
            for obj in self._entities:
                text.append(self.__write_object(obj) + "\n")
            pickle.dump(text, f)

    def add(self, element):
        self.__read_all_from_file()
        RepositoryUniqueElements.add(self, element)
        self.__write_all_to_file()

    def update(self, key, element):
        self.__read_all_from_file()
        RepositoryUniqueElements.update(self, key, element)
        self.__write_all_to_file()

    def remove(self, key):
        self.__read_all_from_file()
        RepositoryUniqueElements.remove(self, key)
        self.__write_all_to_file()

    def get_all(self):
        self.__read_all_from_file()
        return RepositoryUniqueElements.get_all(self)

    def search(self, key):
        self.__read_all_from_file()
        return RepositoryUniqueElements.search(self, key)


class BinaryFileRepositoryMultipleElements(RepositoryMultipleElements):

    def __init__(self, filename, read_object, write_object):
        self.__filename = filename
        self.__read_object = read_object
        self.__write_object = write_object
        RepositoryMultipleElements.__init__(self)

    def __read_all_from_file(self):
        self._entities = IterableStructure()
        result = []
        try:
            f = open(self.__filename, 'rb')
            result = pickle.load(f)
        except EOFError:
            result = []
        except IOError as err:
            raise RepositoryError(err)
        if len(result) == 0:
            return []
        for i in range(len(result)):
            result[i] = result[i].strip()
            obj = self.__read_object(result[i])
            self._entities.append(obj)
        f.close()

    def __write_all_to_file(self):
        text = []
        with open(self.__filename, "wb") as f:
            for obj in self._entities:
                text.append(self.__write_object(obj) + "\n")
            pickle.dump(text, f)

    def add(self, element):
        self.__read_all_from_file()
        RepositoryMultipleElements.add(self, element)
        self.__write_all_to_file()

    def update(self, key):
        self.__read_all_from_file()
        RepositoryMultipleElements.update(self, key)
        self.__write_all_to_file()

    def remove(self, key):
        self.__read_all_from_file()
        RepositoryMultipleElements.remove(self, key)
        self.__write_all_to_file()

    def get_all(self):
        self.__read_all_from_file()
        return RepositoryMultipleElements.get_all(self)

    def search(self, key):
        self.__read_all_from_file()
        return RepositoryMultipleElements.search(self, key)


class UndoRedoStack(object):

    def __init__(self):
        self.__undoRedoActions = []

    def push(self, action):
        self.__undoRedoActions.append(action)

    def pop(self):
        if len(self.__undoRedoActions) == 0:
            raise UndoRedoError("No more actions!\n")
        return self.__undoRedoActions.pop()

    def clear(self):
        self.__undoRedoActions = []
