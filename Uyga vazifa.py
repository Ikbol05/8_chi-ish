# 1 chi masala / map()
'''''
def daraja(number):
    return number ** 2

n = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

daraja2 = map(daraja, range(1,11))

print(list(daraja2))
'''''

# 2 chi masala / filter()
'''''

I = ["A", "a", "B", "b", "C", "c", "D", "d"]

I2 = filter(str.isupper,I)

print(list(I2))

'''''

# 4 chi masala Katta harflarga ugirib berish
'''''

def katta(n: str):
    k = n.capitalize()
    return k

names = ["alfred", "tabitha", "william", "arla"]

natija = map(katta, names)

print(list(natija))

'''''

# 5 chi masala 75 dan katta larni olish
'''''

def  number(n: int):
    i = 0

    if n < 75:
        n = i + n
    else:
        return "Katta son yuq"

    return i

scores = [66, 90, 68, 59, 76, 60, 88, 73, 81, 65]

natija = filter(number,scores)

print(list(natija))

'''''

# 6 chi masala filterda palindrom
'''''
def katta(i):
    if i.lower() == i[::-1].lower():
        print("Yes")
    else:
        print("No")


words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']

natija = filter(katta,words)

print(list(natija))

'''''

# 7 chi masala
'''''

word = ['apple', 'banana', 'cherry']

natija = list(map(lambda x: len(x), word))

print(natija)
'''''
# 8 chi masala

'''''
a = ['apple', 'banana', 'cherry']
b = ['orange', 'lemon', 'pineaple']

natija = a + b
print(natija)
'''''

# 9 chi masala
'''''

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

natija = reduce(lambda a, b: a + b, numbers)
print(natija)
'''''

# 10 chi masala
'''''

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

natija = reduce(lambda a, b: a * b, numbers)
print(natija)

'''''
# 11 chi masala

'''''
words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']

natija1 = (words[:])
natija2 = (words[::])
natija3 = (words[::-1])

print(list(natija1))
print(list(natija2))
print(list(natija3))

'''''

# 12 chi masala

'''''
group1 = ['Anna', 'Alla', 'Kazak', 'Dom']
group2 = ['Sobir', 'Bakir', 'Jalil']

new_group = group1 + group2

print(list(new_group))
'''''

# 13 chi masala
'''''
def H(lst, element):
    return lst.count(element)


words = ['apple', 'banana', 'cherry', 'banana', 'orange']

element_to_count = 'banana'

result = H(words, element_to_count)

print(f"Takrorlanishlar soni: {result}")
'''''

# 14 chi masala
'''''

r = ['Sobir', 'Bakir', 'Toxir', 'Akmal', 'Aziz']

new = (r[::-1])

print(list(new))

'''''
# 15 chi masala
'''''

I1 = ['1', '1', '2', '3', '5', '8', '13', '21', '34', '55', '89']
I2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']

I3 = set(I1 + I2)

print(list(I3))
'''''

# 16 chi masala

'''''

programming_languages = ['Python', 'C', 'C++', 'C#', 'Java', 'Basic', 'Kotlin', 'Pascal', 'JavaScript', 'Go', 'Dart', 'Assambler', 'Ruby', 'Rust', 'Mojo', 'Swift', 'Php']

odd_indexed_languages = programming_languages[1::2]

for natija in odd_indexed_languages:
    print(natija)
'''''

# 17 chi masala

'''''

programming_languages = ['Python', 'C', 'C++', 'C#', 'Java', 'Basic', 'Kotlin', 'Pascal', 'JavaScript', 'Go', 'Dart', 'Assambler', 'Ruby', 'Rust', 'Mojo', 'Swift', 'Php']

natija = programming_languages[5::]

print(list(natija))

'''''

# 18 chi masala

'''''

programming_languages = ['Python', 'C', 'C++', 'C#', 'Java', 'Basic','Kotlin', 'Pascal', 'JavaScript', 'Go', 'Dart', 'Assambler', 'Ruby', 'Rust','Mojo', 'Swift', 'Php']

natija = programming_languages[:12:]

print(list(natija))

'''''

# 19 masala

'''''

programming_languages = ['Python', 'C', 'C++', 'C#', 'Java', 'Basic', 'Kotlin', 'Pascal', 'JavaScript', 'Go', 'Dart', 'Assambler', 'Ruby', 'Rust', 'Mojo', 'Swift', 'Php']

natija = [A.lower() for A in programming_languages]

print(natija)

'''''

# 20 chi masala
'''''

programming_languages = ['Python', 'C', 'C++', 'C#', 'Java', 'Basic', 'Kotlin', 'Pascal', 'JavaScript', 'Go', 'Dart', 'Assambler', 'Ruby', 'Rust', 'Mojo', 'Swift', 'Php']

natija = [B.upper() for B in programming_languages]

print(natija)
'''''

















