#1 hariu O1

#2 hariu O (n)

#3 hariu O1

#4hariu O (n)

#5 hariu O (n)

#6 hariu O (n**)

#7 hariu O (n**)

#8 hariu O (n**)

#9 hariu O (n)

#10 hariu dawtaltan dotorh dawtal bish 

#11 hariu O (log n)

#12 hariu n toog huwaaj shalgaj bn

#13 hariu 2

#14 hariu 1

#15 hariu 1

#16 O1 O(log n ) O(n) O(n**) 

#17 A) O1 B) O(n) C) O(n**) D) O(log n)

# import time

#############Big O-iin hugatsaa zartsuulaltiig shalgah n##############

# # O(1)
# print("----- O(1) -----")

# for n in [10000]:

#     start = time.perf_counter()

#     x = n

#     end = time.perf_counter()

#     print(f"n = {n:<10} | time = {(end - start) * 1000:.2f} ms")


# # O(n)
# print("\n----- O(n) -----")

# for n in [10000]:

#     start = time.perf_counter()

#     total = 0

#     for i in range(n):
#         total += i

#     end = time.perf_counter()

#     print(f"n = {n:<10} | time = {(end - start) * 1000:.2f} ms")


# # O(n²)
# print("\n----- O(n²) -----")

# for n in [10000]:

#     start = time.perf_counter()

#     count = 0

#     for i in range(n):
#         for j in range(n):
#             count += 1

#     end = time.perf_counter()

#     print(f"n = {n:<10} | time = {(end - start) * 1000:.2f} ms")


# # O(log n)
# print("\n----- O(log n) -----")

# for n in [10000]:

#     start = time.perf_counter()

#     x = n

#     while x > 1:
#         x //= 2

#     end = time.perf_counter()

#     print(f"n = {n:<10} | time = {(end - start) * 1000:.2f} ms")