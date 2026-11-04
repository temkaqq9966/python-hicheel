# task 1
# numbers = list(map(int, input("Too oruul: ").split()))
# n = len(numbers)
#
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#
# print(numbers)


# task 2
# numbers = list(map(int, input("Toonuudaa oruul: ").split()))
# n = len(numbers)
#
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if numbers[j] < numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#
# print(numbers)


# task 3
# numbers = list(map(int, input("Eyreg bolon sorog too oruul: ").split()))
# n = len(numbers)
#
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#
# print(numbers)


# task 4
# numbers = list(map(int, input("Davhardsan toonuud oruul: ").split()))
# n = len(numbers)
#
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#
# print(numbers)


# task 5
# values = list(map(int, input("Jagsaaltiin utguud: ").split()))
# n = len(values)
#
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if values[j] > values[j + 1]:
#             values[j], values[j + 1] = values[j + 1], values[j]
#
# print(values)


# task 6
# names = input("Humuusiin neriig oruul: ").split()
# n = len(names)
#
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if names[j] > names[j + 1]:
#             names[j], names[j + 1] = names[j + 1], names[j]
#
# print(names)


# task 7
# scores = list(map(int, input("Suragchdiin onoo: ").split()))
# n = len(scores)
#
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if scores[j] > scores[j + 1]:
#             scores[j], scores[j + 1] = scores[j + 1], scores[j]
#
# print(scores)


# task 8
# numbers = list(map(int, input("Toonuudaa oruul: ").split()))
#
# for j in range(len(numbers) - 1):
#     if numbers[j] > numbers[j + 1]:
#         numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#
# print(numbers)


# task 9
# numbers = list(map(int, input("Toonuudaa oruul: ").split()))
# n = len(numbers)
# round_count = 0
#
# for i in range(n - 1):
#     round_count += 1
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#
# print("Toirog:", round_count)
# print(numbers)


# task 10
# numbers = list(map(int, input("Toonuudaa oruul: ").split()))
# n = len(numbers)
# swap_count = 0
#
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#             swap_count += 1
#
# print(numbers)
# print("Soliltsoonii too:", swap_count)


# task 11
# numbers = list(map(int, input("Toonuudaa oruul: ").split()))
# n = len(numbers)
#
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if numbers[j] < numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#
# print("Hoyordahi ih too:", numbers[1])


# task 12
# numbers = list(map(int, input("Toonuudaa oruul: ").split()))
# n = len(numbers)
#
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#
# print(numbers)


# task 13
# numbers = list(map(int, input("Toonuudaa oruul: ").split()))
# n = len(numbers)
#
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#
#     print(i + 1, "-r toirog:", numbers)


# task 14
# numbers = list(map(int, input("Toonuudaa oruul: ").split()))
# n = len(numbers)
#
# for i in range(n - 1):
#     swapped = False
#
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#             swapped = True
#
#     if not swapped:
#         print("Jagsaalt ali hediin eremblegdsen baina")
#         break
#
# print(numbers)


# task 15
# numbers = list(map(int, input("Toonuudaa oruul: ").split()))
# n = len(numbers)
# round_count = 0
#
# for i in range(n - 1):
#     round_count += 1
#     swapped = False
#
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#             swapped = True
#
#     if not swapped:
#         break
#
# correct = True
#
# for i in range(n - 1):
#     if numbers[i] > numbers[i + 1]:
#         correct = False
#         break
#
# print(numbers)
# if correct:
#     print("Zuv erembelegdsen")
# else:
#     print("Buruu erembelegdsen")
#
# print("Ajillasan toirog:", round_count)


# task 16
# n = int(input("Oyutnii too: "))
# students = []
#
# for i in range(n):
#     name, score = input(f"{i + 1}-r oyutan (ner onoo): ").split()
#     students.append([name, int(score)])
#
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if students[j][1] > students[j + 1][1]:
#             students[j], students[j + 1] = students[j + 1], students[j]
#
# print(students)


# task 17
# n = int(input("Heden hun oruulah ve: "))
# people = []
#
# for i in range(n):
#     name, age = input(f"{i + 1}-r hun (ner nas): ").split()
#     people.append([name, int(age)])
#
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if people[j][1] > people[j + 1][1]:
#             people[j], people[j + 1] = people[j + 1], people[j]
#
# print(people)
# print("Hamgiin zaluu:", people[0][0])
# print("Hamgiin ahmad:", people[-1][0])


# task 18
# numbers = list(map(int, input("Toonuudaa oruul: ").split()))
# target = int(input("Ali toog tooloh ve: "))
# n = len(numbers)
#
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#
# count = 0
#
# for num in numbers:
#     if num == target:
#         count += 1
#
# print(numbers)
# print(target, "too", count, "udaa baina.")


# task 19
# n = int(input("Baraanii too: "))
# products = []
#
# for i in range(n):
#     name, price = input(f"{i + 1}-r baraa (ner une): ").split()
#     products.append([name, int(price)])
#
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if products[j][1] < products[j + 1][1]:
#             products[j], products[j + 1] = products[j + 1], products[j]
#
# print("Unetei 3 baraa:")
# for i in range(min(3, n)):
#     print(products[i][0], "-", products[i][1])


# task 20
# numbers = list(map(int, input("Toonuudaa oruul: ").split()))
# n = len(numbers)
# compare_count = 0
# swap_count = 0
# round_count = 0
#
# for i in range(n - 1):
#     round_count += 1
#     swapped = False
#
#     for j in range(n - 1 - i):
#         compare_count += 1
#
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#             swap_count += 1
#             swapped = True
#
#     if not swapped:
#         break
#
# print("Haritsuulalt:", compare_count)
# print("Soliltsoo:", swap_count)
# print("Toirog:", round_count)
# print(numbers)


# task 21
# values = list(map(int, input("Jagsaaltiin utguud: ").split()))
# n = len(values)
#
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if values[j] > values[j + 1]:
#             values[j], values[j + 1] = values[j + 1], values[j]
#
# print(values)


# task 22
# words = input("Ugnuudee oruul: ").split()
# n = len(words)
#
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if len(words[j]) > len(words[j + 1]):
#             words[j], words[j + 1] = words[j + 1], words[j]
#
# print(words)


# task 23
# numbers = list(map(int, input("Toonuudaa oruul: ").split()))
#
# for j in range(len(numbers) - 1, 0, -1):
#     if numbers[j] < numbers[j - 1]:
#         numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
#
# print(numbers)


# task 24
# numbers = list(map(int, input("Toonuudaa oruul: ").split()))
# n = len(numbers)
#
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if numbers[j] % 2 == 1 and numbers[j + 1] % 2 == 0:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#
# print(numbers)


# task 25
# a = list(map(int, input("Ehnii jagsaalt: ").split()))
# b = list(map(int, input("Hoyordahi jagsaalt: ").split()))
#
# numbers = a + b
# n = len(numbers)
#
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#
# print(numbers)


# task 26
# numbers = list(map(int, input("Toonuudaa oruul: ").split()))
# n = len(numbers)
# total_swaps = 0
#
# for i in range(n - 1):
#     round_swaps = 0
#
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#             round_swaps += 1
#
#     total_swaps += round_swaps
#     print(i + 1, "-r toirog:", round_swaps, "soliltsoo")
#
# print("Niit soliltsoo:", total_swaps)


# task 27
# numbers = list(map(int, input("Toonuudaa oruul: ").split()))
# n = len(numbers)
#
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#
# if n >= 3:
#     print("Gurav dahi baga too:", numbers[2])
# else:
#     print("Dor hayaj 3 too oruulna uu")


# task 28
# n = int(input("Suragchdiin too: "))
# students = []
#
# for i in range(n):
#     name, score = input(f"{i + 1}-r suragch (ner onoo): ").split()
#     students.append([name, int(score)])
#
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if students[j][1] < students[j + 1][1]:
#             students[j], students[j + 1] = students[j + 1], students[j]
#
# print(students)


# task 29
# numbers = list(map(int, input("Toonuudaa oruul: ").split()))
# n = len(numbers)
# compare_count = 0
# swap_count = 0
# no_swap_round = 0
#
# for i in range(n - 1):
#     swapped = False
#
#     for j in range(n - 1 - i):
#         compare_count += 1
#
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#             swap_count += 1
#             swapped = True
#
#     if not swapped:
#         no_swap_round = i + 1
#         break
#
# print("Niit haritsuulalt:", compare_count)
# print("Niit soliltsoo:", swap_count)
#
# if no_swap_round != 0:
#     print("Soliltsoo hiigdeegui toirog:", no_swap_round)
# else:
#     print("Soliltsoogui toirog baihgui")
#
# print(numbers)


# task 30
# n = int(input("Baraanii too: "))
# products = []
#
# for i in range(n):
#     name, price, stock = input(
#         f"{i + 1}-r baraa (ner une uldegdel): "
#     ).split()
#
#     products.append([name, int(price), int(stock)])
#
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#
#         if products[j][1] < products[j + 1][1]:
#             products[j], products[j + 1] = products[j + 1], products[j]
#
#         elif products[j][1] == products[j + 1][1]:
#             if products[j][2] > products[j + 1][2]:
#                 products[j], products[j + 1] = products[j + 1], products[j]
#
# for p in products:
#     print(p)
