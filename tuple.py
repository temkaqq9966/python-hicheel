# # task 1
# colors = tuple(map(str, input("ungu oruul: ").split()))
# print(colors)

# # task 2
# amitan = tuple(map(str, input("amitan oruul: ").split()))
# print(f"{amitan[0]}\n{amitan[2]}\n{amitan[-1]}")

# # task 3
# a = tuple(input("utga oruul:"))
# print(type(a))

# # task 4
# subjects = ("Математик", "Монгол хэл", "Англи хэл", "Программчлал")
# print(f"{subjects[0]}\n{subjects[1]}\n{subjects[2]}\n{subjects[3]}")

# # task 5
# numbers = tuple(input("utguud oruul: ").split())
# for i in numbers[0:3]:
#     print(i)

# # task 6
# numbers = tuple(input("utguud oruul: ").split())
# print(numbers[-1], numbers[-2], numbers[-3])

# for i in range(len(numbers)):
#     print(numbers[i], end=" ")

# # task 7
# fruits = tuple(input("jims oruul: ").split())
# print(len(fruits))

# # task 8
# number = tuple(map(int, input("too oruul: ").split()))
# print(max(number))
# print(min(number))

# # task 9
# score = tuple(map(int, input("dun oruul: ").split()))
# print("Niit", sum(score))
# print("Dundaj", sum(score)//len(score))

# # task 10
# number = tuple(map(int, input("toonuud oruul: ").split()))
# print(sorted(number))

# # task 11
# number = tuple(map(int, input("toonuud oruul: ").split()))
# print(number.count(10))

# # task 12
# fruit = tuple(map(str, input("jimsnuud oruul: ").split()))
# print(fruit.index("alim"))

# # task 13
# animal = tuple(map(str, input("amitnii ner oruul: ").split()))
# a = input("Haih amitan: ")
# if a in animal:
#     print("Oldloo")
# else:
#     print("Oldsongui")

# # task 14
# student = tuple(map(str, input("suragchiin medeelel oruul: ").split()))
# name, age, student_class = student
# print("Name: ", name, "\n", "Age: ", age, "\n", "Class: ", student_class)

# # task 15
# coordinate = tuple(map(int, input("koordinat oruul: ").split()))
# x, y = coordinate
# print("x =", x, "\n", "y =", y)

# # task 16
# book = tuple(map(str, input("nomnii medeelel oruul: ").split()))
# nom, zohiolch, pages = book
# print("Nom: ", nom, "\n", "Zohiolch: ", zohiolch, "\n", "Huudas: ", pages)

# # task 17
# c = map(int, input("hoyor too oruul: ").split())
# a, b = c

# print("a =", b, "\n", "b =", a)

# # task 18
# number = tuple(map(int, input("utguud oruul: ").split()))
# a, *b = number
# print(f"Ehnii utga: {a}\nUldsen utguud: {b}")
# print(f"Ehnii utga {number[0]}, {number[1:]}")

# # task 19
# number = tuple(map(int, input("toonuud oruul: ").split()))
# first, *middle, last = number
# print(f"Ehnii: {first} \nDundah: {middle}\nSuulchiin: {last}")

# # task 20
# student = tuple(map(str, input("ner bolon hicheeluud oruul: ").split()))
# name, *subject = student
# print(f"Name: {name}\nHicheeluud: {subject}")

# # task 21
# product = tuple(map(str, input("baraanii medeelel oruul: ").split()))
# name, price, quantity = product
# price = int(price)
# quantity = int(quantity)
# print(f"Baraa: {name}\nNegj une: {price}\nToo shirheg: {quantity}\nNiit une: {price * quantity}")

# # task 22
# n = int(input("suragchdiin toog oruul: "))
# students = []
# for i in range(n):
#     name, score = input("ner bolon dun oruul: ").split()
#     score = int(score)
#     students.append((name, score))
# for name, score in students:
#     print(f"{name}: {score}")

# # task 23
# n = int(input("suragchdiin toog oruul: "))
# students = []
# for i in range(n):
#     name, score = input("ner bolon dun oruul: ").split()
#     score = int(score)
#     students.append((name, score))
# for name, score in students:
#     if score > 80:
#         print(f"{name}: {score}")

# # task 24
# colors = tuple(map(str, input("ungu oruul: ").split()))
# colors = list(colors)
# colors.append("ulbar shar")
# colors = tuple(colors)
# print(colors)