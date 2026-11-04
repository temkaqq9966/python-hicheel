# # task 1
# def greet(name):
#     print(f"Sain uu, {name}!")

# name = input()
# greet(name)


# # task 2
# def add(a, b):
#     print(a + b)

# a = int(input())
# b = int(input())
# add(a, b)


# # task 3
# def total_price(price):
#     print("Niit une: " + str(price * 2))

# price = float(input())
# total_price(price)


# # task 4
# def show_type(value):
#     print(type(value))
#     value = int(value)
#     print(type(value))

# x = input()
# show_type(x)


# # task 5
# def count_characters(text):
#     print(len(text))

# text = input()
# count_characters(text)


# # task 6
# def show_first_last(word):
#     print(word[0])
#     print(word[-1])

# word = input()
# show_first_last(word)


# # task 7
# def print_numbers(n):
#     for i in range(1, n + 1):
#         print(i)

# n = int(input())
# print_numbers(n)


# # task 8
# def sum_numbers(numbers):
#     nums = []

#     for num in numbers:
#         nums.append(int(num))

#     print(sum(nums))

# numbers = input().split()
# sum_numbers(numbers)


# # task 9
# def find_min_max(numbers):
#     nums = []

#     for num in numbers:
#         nums.append(int(num))

#     print(min(nums), max(nums))

# numbers = input().split()
# find_min_max(numbers)


# # task 10
# def average_score(numbers):
#     nums = []

#     for num in numbers:
#         nums.append(int(num))

#     average = round(sum(nums) / len(nums), 2)
#     print(average)

# numbers = input().split()
# average_score(numbers)


# # task 11
# def add_animal(animals, new_animal):
#     animals.append(new_animal)
#     print(animals)

# animals = input().split()
# new_animal = input()
# add_animal(animals, new_animal)


# # task 12
# def insert_name(names, new_name):
#     names.insert(1, new_name)
#     print(names)

# names = input().split()
# new_name = input()
# insert_name(names, new_name)


# # task 13
# def remove_fruit(fruits, target):
#     fruits.remove(target)
#     print(fruits)

# fruits = input().split()
# target = input()
# remove_fruit(fruits, target)


# # task 14
# def remove_by_index(names, index):
#     removed_name = names.pop(index)
#     print(removed_name)
#     print(",".join(names))

# names = input().split()
# index = int(input())
# remove_by_index(names, index)


# # task 15
# def sort_numbers(numbers):
#     nums = []

#     for num in numbers:
#         nums.append(int(num))

#     nums.sort()
#     print(nums)

#     nums.sort(reverse=True)
#     print(nums)

# numbers = input().split()
# sort_numbers(numbers)


# # task 16
# def reverse_list(numbers):
#     nums = []

#     for num in numbers:
#         nums.append(int(num))

#     nums.reverse()
#     print(nums)

# numbers = input().split()
# reverse_list(numbers)


# # task 17
# def remove_spaces():
#     x = "  hello  "

#     print("[" + x.strip() + "]")
#     print("[" + x.lstrip() + "]")
#     print("[" + x.rstrip() + "]")

# remove_spaces()


# # task 18
# def count_words(sentence):
#     words = sentence.split()
#     print(len(words))

# sentence = input()
# count_words(sentence)


# # task 19
# def count_letter(text, letter):
#     text = text.lower()
#     letter = letter.lower()

#     print(text.count(letter))

# text = input()
# letter = input()
# count_letter(text, letter)


# # task 20
# def find_text(text, target):
#     position = text.find(target)
#     print(position)

#     if position != -1:
#         print(text.index(target))
#     else:
#         print("Oldsongui")

# text = input()
# target = input()
# find_text(text, target)


# # task 21
# def find_pdf(files):
#     found = False

#     for file in files:
#         if file.startswith("report") and file.endswith(".pdf"):
#             print(file)
#             found = True

#     if not found:
#         print("Oldsongui")

# files = input().split()
# find_pdf(files)


# # task 22
# def replace_word(sentence, old_word, new_word):
#     print(sentence.replace(old_word, new_word))

# sentence = input()
# old_word = input()
# new_word = input()
# replace_word(sentence, old_word, new_word)


# # task 23
# def find_name(names, target):
#     names = names.lower().split()
#     target = target.lower()

#     if target in names:
#         print("YES")
#     else:
#         print("NO")

# names = input()
# target = input()
# find_name(names, target)


# # task 24
# def show_word_ends(word):
#     print(word[:3])
#     print(word[-3:])

# word = input()
# show_word_ends(word)


# # task 25
# def check_palindrome(word):
#     word = word.strip().lower()

#     if word == word[::-1]:
#         print("YES")
#     else:
#         print("NO")

# word = input()
# check_palindrome(word)


# # task 26
# def find_longest_word(words):
#     longest = words[0]

#     for word in words:
#         if len(word) > len(longest):
#             longest = word

#     print(longest)

# words = input().split()
# find_longest_word(words)


# # task 27
# def process_record(data):
#     parts = data.split(",")

#     name = parts[0].strip()
#     age = int(parts[1].strip())
#     city = parts[2].strip()

#     print(name + " | Irekh jil: " + str(age + 1) + " | " + city)

# data = input()
# process_record(data)


# # task 28
# def unique_words(words):
#     words = words.lower().split()
#     unique = []

#     for word in words:
#         if word not in unique:
#             unique.append(word)

#     unique.sort()
#     print(" ".join(unique))

# words = input()
# unique_words(words)


# # task 29
# def second_largest(numbers):
#     nums = []

#     for num in numbers:
#         num = int(num)

#         if num not in nums:
#             nums.append(num)

#     nums.sort()
#     print(nums[-2])

# numbers = input().split()
# second_largest(numbers)


# # task 30
# def class_report(n):
#     names = []
#     scores = []

#     for i in range(n):
#         data = input().split(",")

#         name = data[0].strip()
#         score = int(data[1].strip())

#         names.append(name)
#         scores.append(score)

#     average = round(sum(scores) / len(scores), 2)

#     highest_score = max(scores)
#     highest_index = scores.index(highest_score)
#     highest_name = names[highest_index]

#     names.sort()

#     print("Dundaj: " + str(average))
#     print("Khamgiin undur: " + highest_name + " " + str(highest_score))
#     print("Ners: " + ", ".join(names))

# n = int(input())
# class_report(n)