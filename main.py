#ітератор
lst = [1,2,3,4,5,6]
print(iter(lst))

class myiterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.data):
            raise stopiteration
        value = self.data[self.index]
        self.index += 1
        return value
for num in myiterator(lst):
    print(num)

def mygenerator(data):
    for item in data:
        yield item

for num mygenerator(lst):
    print(num)

def tor():
    def plus(a,b):
        return a + b
    def sub (a,b):
        return a - b
    def mnoz(a,b):
        return a * b
    def dil(a,b):
        if b != 0:
            return a / b
        else:
            raise ValueError("pomilka!, delish na nol bratishka")
    return add, sub, mnoz, dil
add, sub, mnoz, dil = tor()
print(dil(3, 0))