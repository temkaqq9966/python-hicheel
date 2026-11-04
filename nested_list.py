# # task 1
# numbers = []
# count = int(input("jagsaaltiin too: "))

# for i in range(count):
#     values = list(map(int, input("utguud oruul: ").split()))
#     numbers.append(values)

# print(numbers[-1][-1])


# # task 2
# students = [
#     ["bat", 18],
#     ["sara", 19],
#     ["bold", 20]
# ]
# print(students[2][0])


# # task 3
# numbers = [
#     [10, 20],
#     [30, 40],
#     [50, 60]
# ]
# print(numbers[2])


# # task 4
# numbers = [
#     [5, 10],
#     [15, 20]
# ]
# print(numbers[0][0])


# # task 5
# numbers = []
# count = int(input("mornii too: "))

# for i in range(count):
#     values = list(map(int, input("toonuud oruul: ").split()))
#     numbers.append(values)

# print(numbers[-1][-1])


# # task 6
# numbers = []
# count = int(input("mornii too: "))

# for i in range(count):
#     values = list(map(int, input("utguud oruul: ").split()))
#     numbers.append(values)

# for row in range(len(numbers)):
#     print(numbers[row])
# print()


# # task 8
# numbers = []
# count = int(input("jagsaaltiin too: "))

# for i in range(count):
#     values = list(map(int, input("toonuud oruul: ").split()))
#     numbers.append(values)

# for row in range(len(numbers)):
#     for value in numbers[row]:
#         print(value)


# # task 9
# numbers = []
# count = int(input("mornii too: "))

# for i in range(count):
#     values = list(map(int, input("utga oruul: ").split()))
#     numbers.append(values)

# for row in range(len(numbers)):
#     for value in numbers[row]:
#         print(value, end=" ")


# # task 10
# numbers = []
# count = int(input("jagsaaltiin too: "))

# for i in range(count):
#     values = list(map(int, input("toonuud oruul: ").split()))
#     numbers.append(values)

# for row in range(len(numbers)):
#     for value in numbers[row]:
#         if value > 10:
#             print(value, end=" ")

# # task 11
# numbers = []
# flat = []
# count = int(input("mornii too: "))

# for i in range(count):
#     values = list(map(int, input("utguud oruul: ").split()))
#     numbers.append(values)

# for row in range(len(numbers)):
#     for value in numbers[row]:
#         flat.append(value)

# print(len(flat))


# # task 12
# numbers = []
# flat = []
# count = int(input("jagsaaltiin too: "))

# for i in range(count):
#     values = list(map(int, input("toonuud oruul: ").split()))
#     numbers.append(values)

# for row in range(len(numbers)):
#     for value in numbers[row]:
#         flat.append(value)

# print(sum(flat))


# # task 13
# numbers = []
# count = int(input("mornii too: "))

# for i in range(count):
#     values = list(map(int, input("utguud oruul: ").split()))
#     numbers.append(values)

# for row in range(len(numbers)):
#     for value in numbers[row]:
#         if value % 2 == 0:
#             print(value, end=" ")


# # task 14
# numbers = []
# odd_numbers = []
# count = int(input("mornii too: "))

# for i in range(count):
#     values = list(map(int, input("toonuud oruul: ").split()))
#     numbers.append(values)

# for row in range(len(numbers)):
#     for value in numbers[row]:
#         if value % 2 == 1:
#             odd_numbers.append(value)
#         print(len(odd_numbers), end=" ")


# # task 15
# numbers = []
# even_numbers = []
# count = int(input("jagsaaltiin too: "))

# for i in range(count):
#     values = list(map(int, input("utguud oruul: ").split()))
#     numbers.append(values)

# for row in range(len(numbers)):
#     for value in numbers[row]:
#         if value % 2 == 0:
#             even_numbers.append(value)
#         print(sum(even_numbers))


# # task 16
# numbers = []
# positive = []
# count = int(input("mornii too: "))

# for i in range(count):
#     values = list(map(int, input("toonuud oruul: ").split()))
#     numbers.append(values)

# for row in range(len(numbers)):
#     for value in numbers[row]:
#         if value > 0:
#             positive.append(value)

# print(len(positive))


# # task 17
# numbers = []
# negative = []
# count = int(input("jagsaaltiin too: "))

# for i in range(count):
#     values = list(map(int, input("utguud oruul: ").split()))
#     numbers.append(values)

# for row in range(len(numbers)):
#     for value in numbers[row]:
#         if value < 0:
#             negative.append(value)
#     print(sum(negative))


# # task 18
# numbers = []
# largest = 0
# count = int(input("mornii too: "))

# for i in range(count):
#     values = list(map(int, input("toonuud oruul: ").split()))
#     numbers.append(values)

# for row in range(len(numbers)):
#     for value in numbers[row]:
#         if value > largest:
#             largest = value
#     print(largest)


# # task 19
# numbers = []
# smallest = 1000000000000
# count = int(input("jagsaaltiin too: "))

# for i in range(count):
#     values = list(map(int, input("utguud oruul: ").split()))
#     numbers.append(values)

# for row in range(len(numbers)):
#     for value in numbers[row]:
#         if value < smallest:
#             smallest = value

# print(smallest)


# # task 20
# numbers = []
# count = int(input("mornii too: "))

# for i in range(count):
#     values = list(map(int, input("toonuud oruul: ").split()))
#     numbers.append(values)

# for row in numbers:
#     print(sum(row))