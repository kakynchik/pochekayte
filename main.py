def multiply_by(n):
    def closure(x):
        return x * n
    return closure
multiply_by_5 = multiply_by(5)
result = multiply_by_5(10)
print(result)