try:
    num1 = int(input("Введіть перше число: "))
    num2 = int(input("Введіть друге число: "))
    result = num1 / num2
    print("Результат: ", result)
except ValueError:
    print("Введено некоректне число. Будь ласка, введіть число цілочисельного формату.")
except ZeroDivisionError:
    print("Ділення на нуль неможливе. Будь ласка, введіть ненульове число для другого числа.")
except Exception as e:
    print("Сталася помилка:", str(e))