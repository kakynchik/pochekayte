class ListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.lst):
            raise StopIteration
        else:
            result = self.lst[self.index]
            self.index += 1
            return result