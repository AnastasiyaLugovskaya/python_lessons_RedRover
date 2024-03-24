# task 3.1
my_list = ['a', 'b', [1, 2, 3], 'd']
print(*my_list[2])
print("_" * 30)

# task 3.2
list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
total = 0
for i in list_1:
    if isinstance(i, (int, float)):
        total += i
    elif isinstance(i, str):
        if 'a' in i:
            print(i)
print(total)
print("_" * 30)

# task 3.3
print(tuple(['cat', 'dog', 'horse', 'cow']))
print("_" * 30)


# task 3.4
def compare_fams(fam1, fam2):
    print('Family 1 is larger') if len(fam1) > len(fam2) else (print('Family 2 is larger') if len(fam1) < len(fam2) else
                                                               print("Families are equal"))


f1 = list(input('Enumerate all members of a family 1 separating by comma: ').split(', '))
f2 = list(input('Enumerate all members of a family 2 separating by comma: ').split(', '))
compare_fams(f1, f2)
print("_" * 30)

# task 3.5
film = {'title': 'Inglourious Basterds', 'director': 'Quentin Tarantino', 'year': 2009, 'budget': '$70 000 000',
        'main_actor': 'Brad Pitt'}
print(*film.keys())
print(*film.values())
print(*film.items())
print("_" * 30)

# task 3.6
my_dict = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
print(sum(my_dict.values()))
print("_" * 30)

# task 3.7
lst = [1, 2, 3, 4, 5, 3, 2, 1]
lst = list(set(lst))
print(lst)
print("_" * 30)

# task 3.8
set1 = {'a', 'z', 1, 5, 9, 12, 100, '1', 785}
set2 = {5, 'z', 1, 8, 9, 21, 100, '1', 785}
print(f'{set1 & set2} - these elements are in both sets')
print(f'{set1 ^ set2} - these elements only appear in one of the sets')
print(f'Is set1 a subset of set2? - {set1.issubset(set2)}')
print(f'Is set2 a subset of set1? - {set2.issubset(set1)}')
