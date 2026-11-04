# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# numbers = [8, 3, 1, 7, 0, 10, 2]
# print(quick_sort(numbers))


# # task 1
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# numbers = list(map(int, input("utguud oruulna uu: ").split()))
# print(quick_sort(numbers))


# # task 2
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# numbers = list(map(int, input("toonuudiin daraalal: ").split()))
# print(quick_sort(numbers))


# # task 3
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# numbers = list(map(int, input("jagsaaltiin utguud: ").split()))
# print(quick_sort(numbers))


# # task 4
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# numbers = list(map(int, input("too oruulna uu: ").split()))
# print(quick_sort(numbers))


# # task 5
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# numbers = list(map(int, input("jagsaaltiin toonuud: ").split()))
# print(quick_sort(numbers)[:3])


# # task 6
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# numbers = list(map(int, input("utguud oruul: ").split()))
# print(quick_sort(numbers)[::-1][:2])


# # task 7
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2][1]

#     left = []
#     middle = []
#     right = []

#     for student in arr:
#         if student[1] < pivot:
#             left.append(student)
#         elif student[1] == pivot:
#             middle.append(student)
#         else:
#             right.append(student)

#     return quick_sort(left) + middle + quick_sort(right)


# n = int(input("suragchdiin too: "))
# students = []

# for i in range(n):
#     name, score = input("ner bolon onoo oruul: ").split()
#     students.append((name, int(score)))

# print(quick_sort(students))


# # task 8
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     right = []
#     middle = []

#     for num in arr:
#         if len(num) < len(pivot):
#             left.append(num)
#         elif len(num) == len(pivot):
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# words = list(map(str, input("ugsiin jagsaalt: ").split()))
# print(quick_sort(words))


