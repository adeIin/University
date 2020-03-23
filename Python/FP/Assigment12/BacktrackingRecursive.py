
class Problem10:
    def __init__(self):
        self.__array = []
        self.__result = []
        self.__aux = []
        self.__n = None

    def read(self):
        n = int(input("Please give n:\n>>>"))
        self.__n = n + 1
        self.set_array_result_aux()
        for i in range(2, self.__n):
            self.__array[i][i - 1] = 1
            self.__array[i - 1][i] = 1

    def set_array_result_aux(self):
        for i in range(self.__n):
            self.__array.append([])
            for j in range(self.__n):
                self.__array[i].append(0)
        for i in range(self.__n):
            self.__result.append(0)
            self.__aux.append(0)

    def display(self):
        print(self.__result[1:])

    def good(self, k):
        if self.__array[self.__result[k]][self.__result[k - 1]] == 1:
            return False
        return True

    def backtraking(self, k):
        for i in range(1, self.__n):
            if not self.__aux[i]:
                self.__result[k] = i
                self.__aux[i] = 1
                if self.good(k) is True:
                    if k == self.__n - 1:
                        self.display()
                    else:
                        self.backtraking(k + 1)
                self.__aux[i] = 0


x = Problem10()
x.read()
x.backtraking(1)
