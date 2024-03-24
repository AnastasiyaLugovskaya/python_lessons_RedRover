# task 1.1.2
print("Hello world!")
print("_" * 30)

# task 1.1.3
user_name = input("What is your name? Please type it here: ")
print(f"Hello {user_name}!")
print("_" * 30)

# task 1.1.3
d1, d2 = int(input("Type the first number: ")), int(input("Type the second number: "))
print(f"Результат = {d1 * d2}")
print("_" * 30)

# task 1.2
print("*" * 5)
print("*" + " " * 3 + "*")
print("*" + " " * 3 + "*")
print("*" + " " * 3 + "*")
print("*" * 5)
print("_" * 30)

# task 1.3
number = int(input("Type the number consists of 4 symbols: "))
print(f"""Тысячи - {number // 1000}
Сотни - {(number // 100) % 10}
Десятки - {(number // 10) % 10} 
Единицы - {number % 10}""")
print("_" * 30)

# task 1.4
n1 = int(input('Type a number: '))
n2 = int(input('Type another number: '))
print(f"""Квадрат суммы {n1} и {n2} равен {(n1 + n2) ** 2}
Сумма квадратов {n1}  и {n2} равна {n1**2 + n2**2}
""")
print("_" * 30)
