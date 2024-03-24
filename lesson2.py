# task 2.1
def is_alive(ch_health):
    return ch_health > 0


health = int(input('Insert the number of the character\'s hitpoints: '))
print(is_alive(health))
print("_" * 30)


# task 2.2
def is_even(num):
    print('Четное') if num % 2 == 0 else print('Нечетное')


number = int(input('Insert any number: '))
is_even(number)
print("_" * 30)


# task 2.3

def check_year(year):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        print(f'Year {year} is not bissextile')
    else:
        print(f'Year {year} is bissextile')


year_in = int(input('Insert a year: '))
check_year(year_in)
print("_" * 30)

# task 2.4

s = input('Insert the text you want to be printed: ')
number = int(input('Insert how many times you want the text to be repeated: '))
for i in range(number):
    print(f'{i + 1} - {s}')
print("_" * 30)


# task 2.5


def calculate(num1, num2, operator):
    match operator:
        case '-':
            print(f'{num1} {operator} {num2} = {num1 - num2}')
        case '+':
            print(f'{num1} {operator} {num2} = {num1 + num2}')
        case '*':
            print(f'{num1} {operator} {num2} = {num1 * num2}')
        case '/':
            print(f'{num1} {operator} {num2} = {num1 / num2}')
        case '//':
            print(f'{num1} {operator} {num2} = {num1 // num2}')
        case '**':
            print(f'{num1} {operator} {num2} = {num1 ** num2}')
        case '%':
            print(f'{num1} {operator} {num2} = {num1 % num2}')


n1 = int(input('Insert the first number: '))
n2 = int(input('Insert the second number: '))
op = input('Choose one of the operators (-, +, *, /, //, %, **): ')
calculate(n1, n2, op)
print("_" * 30)
