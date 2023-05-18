class OddIterator:
    def __init__(self, n):
        if not isinstance(n, int) or n <= 0:
            raise ValueError("treba n cile naturalne chislo")
        self.n = n
        self.current = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        else:
            result = self.current
            self.current +=2
            return result
try:
    for num in OddIterator(9):
        print(num)
except ValueError as e:
    print(e)