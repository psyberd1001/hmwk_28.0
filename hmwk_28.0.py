class StepValueError(ValueError):
    pass


class Iterator:

    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.step > 0:
            self.pointer += self.step
            if self.pointer - self.step > self.stop:
                raise StopIteration()
            return self.pointer - self.step
        if self.step < 0:
            self.pointer += self.step
            if self.pointer - self.step < self.stop:
                raise StopIteration()
            return self.pointer - self.step


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for pointer in iter2:
    print(pointer, end=' ')
print()

for pointer in iter3:
    print(pointer, end=' ')
print()

for pointer in iter4:
    print(pointer, end=' ')
print()

for pointer in iter5:
    print(pointer, end=' ')
print()
