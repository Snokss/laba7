class StrArr:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        return self.array[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        self.array[index] = value

    def concat(self, other):
        if self.size != other.size:
            raise ValueError("Arrays must be of the same size")
        result = StrArr(self.size)
        for i in range(self.size):
            result[i] = self[i] + other[i]
        return result

    def merge(self, other):
        result = StrArr(self.size + other.size)
        for i in range(self.size):
            result[i] = self[i]
        for i in range(other.size):
            if other[i] not in self.array:
                result[self.size + i] = other[i]
        return result

    def print_elem(self, index):
        print(self[index])

    def print_masive(self):
        for i in range(self.size):
            print(self[i])

if __name__=="__main__":
    
    # создание массива
    arr1 = StrArr(3)
    arr1[0] = "focus"
    arr1[1] = "school"
    arr1[2] = "house"

    # обращение к элементу массива
    print(arr1[1])

    print("\n\n") # для увеличения читабельности кода

    # выполнение операции поэлементного сцепления
    arr2 = StrArr(3)
    arr2[0] = "say"
    arr2[1] = "everyday"
    arr2[2] = "street"
    arr3 = arr1.concat(arr2)
    arr3.print_masive()

    print("\n\n")# для увеличения читабельности кода

    # выполнение операции слияния
    arr4 = StrArr(3)
    arr4[0] = "eggs"
    arr4[1] = "school"
    arr4[2] = "water"
    arr5 = arr1.merge(arr4)

    print(arr5[2])
    print("\n") # для увеличения читабельности кода
    arr5.print_masive()