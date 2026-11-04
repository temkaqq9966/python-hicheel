 # 1

# numbers = list(map(int, input("Jagsaaltiin toonuud: ").split()))
# target = int(input("Haih too: "))

# left = 0
# right = len(numbers) - 1
# found = False

# while left <= right:
#     mid = (left + right) // 2

#     if numbers[mid] == target:
#         found = True
#         break
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# if found:
#     print("Oldloo")
# else:
#     print("Oldsongui")


# # 2

# numbers = list(map(int, input("Jagsaaltiin toonuud: ").split()))
# target = int(input("Haih too: "))

# left = 0
# right = len(numbers) - 1
# result = -1

# while left <= right:
#     mid = (left + right) // 2

#     if numbers[mid] == target:
#         result = mid
#         break
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# print(result)


# # 3

# numbers = list(map(int, input("Jagsaaltiin toonuud: ").split()))
# target = int(input("Haih too: "))

# left = 0
# right = len(numbers) - 1
# result = -1

# while left <= right:
#     mid = (left + right) // 2

#     if numbers[mid] == target:
#         result = mid
#         break
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# print(result)


# # 4

# numbers = list(map(int, input("Jagsaaltiin toonuud: ").split()))
# target = int(input("Haih too: "))

# left = 0
# right = len(numbers) - 1
# result = -1

# while left <= right:
#     mid = (left + right) // 2

#     if numbers[mid] == target:
#         result = mid
#         break
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# print(result)


# # 5

# numbers = list(map(int, input("Jagsaaltiin toonuud: ").split()))
# target = int(input("Haih too: "))

# left = 0
# right = len(numbers) - 1
# found = False

# while left <= right:
#     mid = (left + right) // 2

#     if numbers[mid] == target:
#         found = True
#         break
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# if found:
#     print("Oldloo")
# else:
#     print("Haij bui too baihgui")


# # 6

# numbers = list(map(int, input("Jagsaaltiin toonuud: ").split()))
# target = int(input("Haih too: "))

# left = 0
# right = len(numbers) - 1
# count = 0

# while left <= right:
#     mid = (left + right) // 2
#     count += 1

#     if numbers[mid] == target:
#         break
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# print("Alham:", count)


# # 7

# scores = list(map(int, input("Suragchdiin onoo: ").split()))
# target = int(input("Haih onoo: "))

# left = 0
# right = len(scores) - 1
# result = -1

# while left <= right:
#     mid = (left + right) // 2

#     if scores[mid] == target:
#         result = mid
#         break
#     elif scores[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# if result != -1:
#     print("Index:", result)
# else:
#     print("Oldsongui")


# # 8

# codes = list(map(int, input("Baraanii koduud: ").split()))
# target = int(input("Baraanii kod: "))

# left = 0
# right = len(codes) - 1
# found = False

# while left <= right:
#     mid = (left + right) // 2

#     if codes[mid] == target:
#         found = True
#         break
#     elif codes[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# if found:
#     print("Baraa burtgeltei")
# else:
#     print("Baraa burtgelgui")


# # 9

# book_ids = list(map(int, input("Nomiin dugaaryyd: ").split()))
# target = int(input("Nomiin dugaar: "))

# left = 0
# right = len(book_ids) - 1
# result = -1

# while left <= right:
#     mid = (left + right) // 2

#     if book_ids[mid] == target:
#         result = mid
#         break
#     elif book_ids[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# print(result)


# # 10

# numbers = list(map(int, input("Jagsaaltiin toonuud: ").split()))
# target = int(input("Haih too: "))

# left = 0
# right = len(numbers) - 1
# found = False

# while left <= right:
#     mid = (left + right) // 2

#     print("Left:", left, "Right:", right, "Mid:", mid)

#     if numbers[mid] == target:
#         print("Index:", mid)
#         found = True
#         break
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# if not found:
#     print("Oldsongui")


# # 11

# numbers = list(map(int, input("Jagsaaltiin toonuud: ").split()))
# target = int(input("Haih too: "))

# left = 0
# right = len(numbers) - 1
# result = -1

# while left <= right:
#     mid = (left + right) // 2

#     if numbers[mid] == target:
#         result = mid
#         right = mid - 1
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# print(result)


# # 12

# numbers = list(map(int, input("Jagsaaltiin toonuud: ").split()))
# target = int(input("Haih too: "))

# left = 0
# right = len(numbers) - 1
# result = -1

# while left <= right:
#     mid = (left + right) // 2

#     if numbers[mid] == target:
#         result = mid
#         left = mid + 1
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# print(result)


# # 13

# numbers = list(map(int, input("Jagsaaltiin toonuud: ").split()))
# target = int(input("Oruulah too: "))

# left = 0
# right = len(numbers)

# while left < right:
#     mid = (left + right) // 2

#     if numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid

# print("Index:", left)


# # 14

# numbers = list(map(int, input("Jagsaaltiin toonuud: ").split()))
# target = int(input("Haih too: "))

# left = 0
# right = len(numbers) - 1
# result = -1

# while left <= right:
#     mid = (left + right) // 2

#     if numbers[mid] < target:
#         result = numbers[mid]
#         left = mid + 1
#     else:
#         right = mid - 1

# if result != -1:
#     print(result)
# else:
#     print("Baihgui")


# # 15

# numbers = list(map(int, input("Jagsaaltiin toonuud: ").split()))
# target = int(input("Haih too: "))

# left = 0
# right = len(numbers) - 1
# result = -1

# while left <= right:
#     mid = (left + right) // 2

#     if numbers[mid] > target:
#         result = numbers[mid]
#         right = mid - 1
#     else:
#         left = mid + 1

# if result != -1:
#     print(result)
# else:
#     print("Baihgui")


# # 16

# numbers = list(map(int, input("Jagsaaltiin toonuud: ").split()))

# a = int(input("Ehnii too: "))
# b = int(input("Hoyor dahi too: "))

# for target in [a, b]:
#     left = 0
#     right = len(numbers) - 1
#     result = -1

#     while left <= right:
#         mid = (left + right) // 2

#         if numbers[mid] == target:
#             result = mid
#             break
#         elif numbers[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     print(result)


# # 17

# numbers = list(map(int, input("Jagsaaltiin toonuud: ").split()))
# target = int(input("Haih too: "))

# left = 0
# right = len(numbers) - 1
# result = -1

# while left <= right:
#     mid = (left + right) // 2

#     if numbers[mid] == target:
#         result = mid
#         break
#     elif numbers[mid] > target:
#         left = mid + 1
#     else:
#         right = mid - 1

# print(result)


# # 18

# def binary_search(numbers, target):
#     left = 0
#     right = len(numbers) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if numbers[mid] == target:
#             return mid
#         elif numbers[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1


# numbers = list(map(int, input("Jagsaaltiin toonuud: ").split()))
# target = int(input("Haih too: "))

# print(binary_search(numbers, target))


# # 19

# numbers = list(map(int, input("Jagsaaltiin toonuud: ").split()))
# target = int(input("Haih too: "))

# left = 0
# right = len(numbers) - 1
# first = -1

# while left <= right:
#     mid = (left + right) // 2

#     if numbers[mid] == target:
#         first = mid
#         right = mid - 1
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# left = 0
# right = len(numbers) - 1
# last = -1

# while left <= right:
#     mid = (left + right) // 2

#     if numbers[mid] == target:
#         last = mid
#         left = mid + 1
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# if first != -1:
#     print("Too:", last - first + 1)
# else:
#     print("Too: 0")


