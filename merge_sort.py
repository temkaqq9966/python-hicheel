# def merge(left, right):
#     result = []
#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result


# # 1
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2

#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])

#     return merge(left, right)


# arr = list(map(int, input().split()))
# print(merge_sort(arr))


# # 2
# def merge_sort_desc(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2

#     left = merge_sort_desc(arr[:mid])
#     right = merge_sort_desc(arr[mid:])

#     result = []
#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] >= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result


# arr = list(map(int, input().split()))
# print(merge_sort_desc(arr))


# # 3
# arr = list(map(int, input().split()))
# print(merge_sort(arr))


# # 4. Sorog toonuudiig erembelekh

# arr = list(map(int, input().split()))
# print(merge_sort(arr))




# # 6
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# print(merge(a, b))


# # 7
# def smallest_three(arr):
#     sorted_arr = merge_sort(arr)
#     return sorted_arr[:3]


# arr = list(map(int, input().split()))
# print(smallest_three(arr))


# # 8
# def merge_sort_count(arr):
#     if len(arr) <= 1:
#         return arr, 0, 0

#     mid = len(arr) // 2

#     left, left_count, left_merge = merge_sort_count(arr[:mid])
#     right, right_count, right_merge = merge_sort_count(arr[mid:])

#     result = []
#     i = 0
#     j = 0

#     comparisons = left_count + right_count
#     merge_count = left_merge + right_merge + 1

#     while i < len(left) and j < len(right):
#         comparisons += 1

#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result, comparisons, merge_count


# arr = list(map(int, input().split()))

# result, comparisons, merge_count = merge_sort_count(arr)

# print("Эрэмбэлсэн:", result)
# print("Харьцуулалт:", comparisons)
# print("Merge:", merge_count)


# # 9
# def largest_two(arr):
#     sorted_arr = merge_sort_desc(arr)
#     return sorted_arr[:2]


# arr = list(map(int, input().split()))
# print(largest_two(arr))


# # 10
# names = input().split()
# print(merge_sort(names))


# # 11
# def sort_students(students):
#     return merge_sort_by(
#         students,
#         lambda a, b: a[1] > b[1] or
#         (a[1] == b[1] and a[0] <= b[0])
#     )


# n = int(input())
# students = []

# for i in range(n):
#     data = input().split(",")
#     name = data[0].strip()
#     score = int(data[1].strip())

#     students.append((name, score))

# print(sort_students(students))


# # 12
# def sort_words(words):
#     return merge_sort_by(
#         words,
#         lambda a, b: (len(a), a) <= (len(b), b)
#     )


# words = input().split()
# print(sort_words(words))


# # 13
# def binary_search(arr, target):
#     arr = merge_sort(arr)

#     left = 0
#     right = len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1


# arr = list(map(int, input().split()))
# target = int(input())

# print(binary_search(arr, target))


# # 14
# def is_anagram(word1, word2):
#     letters1 = merge_sort(list(word1))
#     letters2 = merge_sort(list(word2))

#     return letters1 == letters2


# word1 = input()
# word2 = input()

# print(is_anagram(word1, word2))


# # 15
# def closest_pair(arr):
#     arr = merge_sort(arr)

#     smallest_diff = abs(arr[1] - arr[0])
#     best_pair = (arr[0], arr[1])

#     for i in range(1, len(arr) - 1):
#         diff = abs(arr[i + 1] - arr[i])

#         if diff < smallest_diff:
#             smallest_diff = diff
#             best_pair = (arr[i], arr[i + 1])

#     return best_pair, smallest_diff


# arr = list(map(int, input().split()))

# pair, diff = closest_pair(arr)

# print(pair, "zuruu =", diff)