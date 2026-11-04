# task 1
# for i in range(1, 11):
#     print(i)


# task 2
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)


# task 3
# for i in range(1, 21):
#     if i % 2 == 1:
#         print(i)


# task 4
# for i in range(1, 11):
#     print("5 x", i, "=", 5 * i)


# task 5
# n = int(input("N too: "))
#
# for i in range(1, n + 1):
#     print(i)


# task 6
# n = int(input("N too: "))
#
# for i in range(n, 0, -1):
#     print(i)


# task 7
# for i in range(1, 51):
#     if i % 3 == 0:
#         print(i)


# task 8
# for i in range(1, 31):
#     if i % 5 != 0:
#         print(i)


# task 9
# count = 0
#
# for i in range(1, 101):
#     if i % 2 == 0:
#         count += 1
#
# print(count)


# task 10
# count = 0
#
# for i in range(1, 101):
#     if i % 7 == 0:
#         count += 1
#
# print(count)


# task 11
# total = 0
#
# for i in range(1, 101):
#     total += i
#
# print(total)


# task 12
# total = 0
#
# for i in range(1, 51):
#     if i % 2 == 0:
#         total += i
#
# print(total)


# task 13
# i = 1
#
# while i <= 10:
#     print(i)
#     i += 1


# task 14
# i = 10
#
# while i >= 1:
#     print(i)
#     i -= 1


# task 15
# i = 2
#
# while i <= 20:
#     print(i)
#     i += 2


# task 16
# n = int(input("N too: "))
# i = 1
# total = 0
#
# while i <= n:
#     total += i
#     i += 1
#
# print(total)


# task 17
# n = int(input("Eyreg buhel too: "))
# count = 0
#
# while n > 0:
#     n //= 10
#     count += 1
#
# print(count)


# task 18
# n = int(input("Eyreg buhel too: "))
# total = 0
#
# while n > 0:
#     digit = n % 10
#     total += digit
#     n //= 10
#
# print(total)


# task 19
# for i in range(1, 21):
#     if i == 5:
#         break
#     print(i)


# task 20
# for i in range(10, 101):
#     if i % 7 == 0:
#         print(i)
#         break


# task 21
# secret = 8
#
# while True:
#     n = int(input("Too: "))
#
#     if n == secret:
#         print("Zuv taalaa")
#         break


# task 22
# while True:
#     n = int(input("Too: "))
#
#     if n == 0:
#         break
#
#     print(n)


# task 23
# total = 0
#
# while True:
#     n = int(input("Too: "))
#
#     if n == 0:
#         break
#
#     total += n
#
# print(total)


# task 24
# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)


# task 25
# for i in range(1, 21):
#     if i % 2 == 0:
#         continue
#     print(i)


# task 26
# for i in range(1, 31):
#     if i % 3 == 0:
#         continue
#     print(i)


# task 27
# total = 0
#
# for i in range(5):
#     n = int(input("Too: "))
#
#     if n < 0:
#         continue
#
#     total += n
#
# print(total)


# task 28
# i = 1
# count = 0
#
# while count < 5:
#     if i % 7 == 0:
#         print(i)
#         count += 1
#
#     i += 1


# task 29
# while True:
#     n = int(input("Too: "))
#
#     if n == 0:
#         break
#
#     if n < 0:
#         continue
#
#     if n % 2 == 1:
#         continue
#
#     print(n)


# task 30
# secret = 17
#
# while True:
#     n = int(input("Too: "))
#
#     if n < 0:
#         print("Sorog too oruulahgui")
#         continue
#
#     if n < secret:
#         print("Baga baina")
#     elif n > secret:
#         print("Ih baina")
#     else:
#         print("Zuv taalaa")
#         break