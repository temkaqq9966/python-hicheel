# 1

# numbers = [8, 12, 6, 9, 14, 21]

# for i in range(len(numbers)):
#     if numbers[i] % 2 != 0:
#         print(i)
#         break


# # 2

# numbers = [3, 7, 5, 12, 8, 4]

# found = False

# for num in numbers:
#     if num > 10:
#         found = True
#         break

# if found:
#     print("Oldloo")
# else:
#     print("Oldsongui")


# # 3

# numbers = [5, 8, 3, 0, 7, 2]

# for i in range(len(numbers)):
#     if numbers[i] == 0:
#         print(i)
#         break


# # 4

# numbers = [3, 8, 2, 10, 5, 7]

# for num in numbers:
#     if num > 5:
#         print(num)
#         break


# # 5

# numbers = [5, -2, 8, -7, -3, 10, 4]

# count = 0

# for num in numbers:
#     if num < 0:
#         count += 1

# print(count)


# # 6

# numbers = [15, 20, 8, 25, 10, 30]

# target = int(input("Target too: "))

# for num in numbers:
#     if num < target:
#         print(num)
#         break


# # 7

# numbers = [3, 7, 11, 15, 18, 21, 24]

# for num in numbers:
#     if num % 2 == 0:
#         print(num)
#         break


# # 8

# numbers = [12, 5, 17, 8, 23, 4, 19]

# for i in range(len(numbers)):
#     if numbers[i] > 15 and numbers[i] % 2 != 0:
#         print(i)
#         break


# # 9

# students = [
#     ["Bat", 65],
#     ["Saraa", 82],
#     ["Bold", 74],
#     ["Anu", 91],
#     ["Temuulen", 78]
# ]

# for student in students:
#     if student[1] > 80:
#         print(student[0])
#         break


# # 10

# numbers = [4, 7, 10, 13, 8, 21, 6]

# last_index = -1

# for i in range(len(numbers)):
#     if numbers[i] % 2 != 0:
#         last_index = i

# print(last_index)


# # 11

# numbers = [4, 7, 4, 9, 4, 2, 4]

# target = int(input("Haih too: "))

# for i in range(len(numbers)):
#     if numbers[i] == target:
#         print("Index:", i)


# # 12

# students = [
#     ["Bat", 65],
#     ["Saraa", 82],
#     ["Bold", 74],
#     ["Anu", 91],
#     ["Temuulen", 78]
# ]

# name = input("Suragchiin ner: ")

# found = False

# for student in students:
#     if student[0] == name:
#         found = True

#         if student[1] >= 60:
#             print("Tentsen")
#         else:
#             print("Tentseegui")

#         break

# if not found:
#     print("Oldsongui")