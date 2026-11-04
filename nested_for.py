# 1

# N = int(input("Suragchdiin too: "))
# M = int(input("Shalgaltin too: "))

# for i in range(N):
#     total = 0

#     for j in range(M):
#         score = int(input("Onoo oruul: "))
#         total += score

#     average = total / M

#     print(f"{i+1}-r suragch: niit {total}, dundaj {average}")

#     if average >= 60:
#         print("Tentsen")
#     else:
#         print("Tentseegui")


# # 2

# N = int(input("Hudaldan avagchiin too: "))

# for i in range(N):
#     M = int(input("Baraanii turliin too: "))
#     total = 0

#     for j in range(M):
#         price = int(input("Negj une: "))
#         quantity = int(input("Shirheg: "))

#         total += price * quantity

#     money = int(input("Ugsun mungu: "))

#     print(f"{i+1}-r hunii tuluh dun: {total}")

#     if money >= total:
#         print("Hariult:", money - total)
#     else:
#         print("Dutuu mungu:", total - money)


# # 3

# N = int(input("Ajilchdiin too: "))

# for i in range(N):
#     salary = 0

#     for j in range(5):
#         hours = int(input("Ajillasan tsag: "))

#         if hours <= 8:
#             salary += hours * 5000
#         else:
#             salary += 8 * 5000 + (hours - 8) * 7500

#     print(f"{i+1}-r ajilchnii niit tsalin: {salary}")


# # 4

# N = int(input("Huni too: "))
# M = int(input("Sariin too: "))

# for i in range(N):
#     debt = int(input("Anhnii ur: "))
#     total = 0

#     for j in range(M):
#         payment = int(input("Sariin tulult: "))

#         debt -= payment
#         total += payment

#         print(f"{i+1}-r hun, {j+1}-r sariin daraah uldegdel: {debt}")

#     print("Niit tulson:", total)


# # 5

# N = int(input("Udriin too: "))
# M = int(input("Uildverleliin udaa: "))

# for i in range(N):
#     total = 0

#     for j in range(M):
#         product = int(input("Buteegdehuunii too: "))
#         total += product

#     boxes = total // 12
#     remainder = total % 12

#     print(f"{i+1}-r udur: niit {total}, buten hairtsag {boxes}, uldegdel {remainder}")


# # 6

# N = int(input("Ayalliin too: "))
# M = int(input("Buuudliin too: "))

# for i in range(N):
#     passengers = 0
#     total_boarded = 0

#     for j in range(M):
#         off = int(input("Buusan hun: "))
#         on = int(input("Suusan hun: "))

#         passengers = passengers - off + on
#         total_boarded += on

#         print(f"{j+1}-r buudliin daraa: {passengers} hun")

#     income = total_boarded * 1000

#     print(f"{i+1}-r ayalald niit suusan: {total_boarded}")
#     print("Ayalliin orlogo:", income)


# # 7

# N = int(input("N too: "))

# for i in range(1, N + 1):
#     count = 0
#     total = 0

#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
#             total += j

#     print(f"{i}: {count} huvaagchtai, niilber {total}")


# # 8

# N = int(input("N too: "))

# count = 0

# for i in range(1, N + 1):
#     for j in range(i, N + 1):
#         if i + j == N:
#             print(f"{i} + {j} = {N}")
#             count += 1

# print("Niit:", count, "hos")


# # 9

# N = int(input("Tuluh mungu: "))

# count = 0

# for i in range(N // 1000 + 1):
#     for j in range(N // 2000 + 1):
#         if i * 1000 + j * 2000 == N:
#             print(f"1000T: {i} shirheg, 2000T: {j} shirheg")
#             count += 1

# print("Niit:", count, "huvilbar")


# # 10

# N = int(input("N too: "))

# count = 0

# for i in range(1, N + 1):
#     for j in range(i, N + 1):
#         if i * j == N:
#             difference = j - i

#             print(f"{i} x {j} = {N}, yalгavar {difference}")
#             count += 1

# print("Niit:", count, "hos")