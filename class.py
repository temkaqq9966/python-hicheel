
# # TASK 1
# class Hun:
#     def __init__(self, ner, nas):
#         self.ner = ner
#         self.nas = nas

#     def medeelel_haruulah(self):
#         print("Minii ner", self.ner)
#         print("Nas:", self.nas)

# hun1 = Hun("Анужин", 19)
# hun2 = Hun("Мөнх", 21)

# print("\n--- Task 1 ---")
# hun1.medeelel_haruulah()
# hun2.medeelel_haruulah()


# # TASK 2
# class Suragch2:
#     def __init__(self, ner, nas):
#         self.ner = ner
#         self.nas = nas

# print("\n--- Task 2 ---")
# ner1 = input("1-r suragchiin ner: ")
# nas1 = int(input("1-r suragchiin nas: "))
# ner2 = input("2-r suragchiin ner: ")
# nas2 = int(input("2-r suragchiin nas: "))

# s1 = Suragch2(ner1, nas1)
# s2 = Suragch2(ner2, nas2)

# print(s1.ner, s1.nas)
# print(s2.ner, s2.nas)


# # TASK 3
# class Suragch3:
#     def __init__(self, ner, nas):
#         self.ner = ner
#         self.nas = nas

# print("\n--- Task 3 ---")
# suragchid3 = []

# while True:
#     ner = input("Suragchiin ner (duusgah bol Enter): ")
#     if ner == "":
#         break

#     nas = int(input("Nas: "))
#     suragchid3.append(Suragch3(ner, nas))

# for s in suragchid3:
#     print("Ner:", s.ner)
#     print("Nas:", s.nas)


# # TASK 4
# class Suragch4:
#     def __init__(self, ner, nas, angi):
#         self.ner = ner
#         self.nas = nas
#         self.angi = angi

#     def medeelel(self):
#         print(f"Ner: {self.ner}")
#         print(f"Nas: {self.nas}")
#         print(f"Angi: {self.angi}")

# print("\n--- Task 4 ---")
# suragchid4 = []

# while True:
#     ner = input("Ner: ")
#     if ner == "":
#         break

#     nas = int(input("Nas: "))
#     angi = input("Angi: ")
#     suragchid4.append(Suragch4(ner, nas, angi))

# for s in suragchid4:
#     s.medeelel()


# # TASK 5
# class Suragch5:
#     def __init__(self, ner, dun):
#         self.ner = ner
#         self.dun = dun

# print("\n--- Task 5 ---")
# suragchid5 = []

# while True:
#     ner = input("Suragchiin ner: ")
#     if ner == "":
#         break

#     dun = int(input("Avsan dun: "))
#     suragchid5.append(Suragch5(ner, dun))

# for s in suragchid5:
#     print(s.ner, "-", s.dun, "onoo")


# # TASK 6
# class Suragch6:
#     def __init__(self, ner, dun):
#         self.ner = ner
#         self.dun = dun

#     def onoo_nemeh(self):
#         self.dun += 10

# print("\n--- Task 6 ---")
# suragchid6 = []

# while True:
#     ner = input("Ner: ")
#     if ner == "":
#         break

#     dun = int(input("Dun: "))
#     suragchid6.append(Suragch6(ner, dun))

# for s in suragchid6:
#     s.onoo_nemeh()
#     print(s.ner, "shine dun:", s.dun)


# # TASK 7
# class Suragch7:
#     def __init__(self, ner, dun):
#         self.ner = ner
#         self.dun = dun

#     def shalgah(self):
#         if self.dun >= 70:
#             print(self.ner, "- Tentssen")
#         else:
#             print(self.ner, "- Tentseegui")

# print("\n--- Task 7 ---")
# suragchid7 = []

# while True:
#     ner = input("Ner: ")
#     if ner == "":
#         break

#     dun = int(input("Dun: "))
#     suragchid7.append(Suragch7(ner, dun))

# for s in suragchid7:
#     s.shalgah()


# # TASK 8
# class Suragch8:
#     def __init__(self, ner, nas):
#         self.ner = ner
#         self.nas = nas

#     def nas_nemeh(self):
#         self.nas += 1

# print("\n--- Task 8 ---")
# suragchid8 = []

# while True:
#     ner = input("Ner: ")
#     if ner == "":
#         break

#     nas = int(input("Nas: "))
#     suragchid8.append(Suragch8(ner, nas))

# for s in suragchid8:
#     s.nas_nemeh()
#     print(s.ner, "shine nas:", s.nas)


# # TASK 9
# class Suragch9:
#     def __init__(self, ner, dun):
#         self.ner = ner
#         self.dun = dun

#     def dun_shalgah(self):
#         if self.dun < 0 or self.dun > 100:
#             print("Buruu dun")
#         elif self.dun >= 90:
#             print("A")
#         elif self.dun >= 80:
#             print("B")
#         elif self.dun >= 70:
#             print("C")
#         elif self.dun >= 60:
#             print("D")
#         else:
#             print("F")

# print("\n--- Task 9 ---")
# suragchid9 = []

# while True:
#     ner = input("Ner: ")
#     if ner == "":
#         break

#     dun = int(input("Dun: "))
#     suragchid9.append(Suragch9(ner, dun))

# for s in suragchid9:
#     print(s.ner, end=": ")
#     s.dun_shalgah()


# # TASK 10
# class Suragch10:
#     def __init__(self, ner):
#         self.ner = ner
#         self.irts = 0

#     def irts_burtgeh(self):
#         self.irts += 1

#     def haruulah(self):
#         print(self.ner, "- irts:", self.irts)

# print("\n--- Task 10 ---")
# suragchid10 = []

# while True:
#     ner = input("Ner: ")
#     if ner == "":
#         break

#     suragchid10.append(Suragch10(ner))

# for s in suragchid10:
#     too = int(input(s.ner + " heden udaa irsen be: "))

#     for i in range(too):
#         s.irts_burtgeh()

# for s in suragchid10:
#     s.haruulah()


# # TASK 11
# class Suragch11:
#     def __init__(self, ner, dun, irts):
#         self.ner = ner
#         self.dun = dun
#         self.irts = irts

# print("\n--- Task 11 ---")
# suragchid11 = []

# while True:
#     ner = input("Ner: ")
#     if ner == "":
#         break

#     dun = int(input("Dun: "))
#     irts = int(input("Irtsiin huvi: "))
#     suragchid11.append(Suragch11(ner, dun, irts))

# for s in suragchid11:
#     if s.dun >= 70 and s.irts >= 80:
#         print(s.ner, "- Tentssen")
#     else:
#         print(s.ner, "- Tentseegui")


# # TASK 12
# class Suragch12:
#     def __init__(self, ner, onoonuud):
#         self.ner = ner
#         self.onoonuud = onoonuud

#     def haruulah(self):
#         print(self.ner, "- Onoo:", self.onoonuud)

#     def onoo_nemeh(self, dun):
#         self.onoonuud.append(dun)

#     def dundaj(self):
#         if len(self.onoonuud) == 0:
#             return 0

#         return round(sum(self.onoonuud) / len(self.onoonuud), 2)

# print("\n--- Task 12 ---")
# suragchid12 = []

# while True:
#     ner = input("Ner: ")
#     if ner == "":
#         break

#     onoonuud = list(map(int, input("Onoonuud: ").split()))
#     s = Suragch12(ner, onoonuud)

#     nemelt = int(input("Nemeh onoo: "))
#     s.onoo_nemeh(nemelt)

#     suragchid12.append(s)

# for s in suragchid12:
#     s.haruulah()
#     print("Dundaj:", s.dundaj())


# # TASK 13
# class Suragch13:
#     def __init__(self, ner, angi):
#         self.ner = ner
#         self.angi = angi

#     def medeelel(self):
#         print("Ner:", self.ner)
#         print("Angi:", self.angi)

#     def ner_solih(self, shine_ner):
#         self.ner = shine_ner

#     def angi_solih(self, shine_angi):
#         self.angi = shine_angi

# print("\n--- Task 13 ---")
# suragchid13 = []

# while True:
#     ner = input("Ner: ")
#     if ner == "":
#         break

#     angi = input("Angi: ")
#     suragchid13.append(Suragch13(ner, angi))

# for s in suragchid13:
#     print("Huuchin medeelel:")
#     s.medeelel()

#     shine_ner = input("Shine ner: ")
#     shine_angi = input("Shine angi: ")

#     s.ner_solih(shine_ner)
#     s.angi_solih(shine_angi)

#     print("Shine medeelel:")
#     s.medeelel()


# # TASK 14
# class Suragch14:
#     def __init__(self, ner, nas, angi):
#         self.ner = ner
#         self.nas = nas
#         self.angi = angi

#     def nas_nemeh(self):
#         self.nas += 1

#     def medeelel(self):
#         print("Ner:", self.ner)
#         print("Nas:", self.nas)
#         print("Angi:", self.angi)

# print("\n--- Task 14 ---")
# suragchid14 = []

# while True:
#     ner = input("Ner: ")
#     if ner == "":
#         break

#     nas = int(input("Nas: "))
#     angi = input("Angi: ")
#     suragchid14.append(Suragch14(ner, nas, angi))

# for s in suragchid14:
#     s.nas_nemeh()
#     s.medeelel()


# # TASK 15
# class Suragch15:
#     def __init__(self, ner, angi):
#         self.ner = ner
#         self.angi = angi
#         self.onoonuud = []

#     def medeelel(self):
#         print(f"Ner: {self.ner}")
#         print(f"Angi: {self.angi}")
#         print(f"Onoonuud: {self.onoonuud}")

#     def onoo_nemeh(self, dun):
#         self.onoonuud.append(dun)

#     def dundaj(self):
#         if len(self.onoonuud) == 0:
#             return 0

#         return round(sum(self.onoonuud) / len(self.onoonuud), 2)

#     def dun_shalgah(self):
#         if self.dundaj() >= 70:
#             print(self.ner, "- Tentssen")
#         else:
#             print(self.ner, "- Tentseegui")

# print("\n--- Task 15 ---")
# suragchid15 = []

# while True:
#     ner = input("Suragchiin ner (duusgah bol Enter): ")

#     if ner == "":
#         break

#     angi = input("Angi: ")
#     s = Suragch15(ner, angi)

#     onoonuud = input("Avsan onoonuudaa zaigaar tusgaarla: ").split()

#     for dun in onoonuud:
#         s.onoo_nemeh(int(dun))

#     suragchid15.append(s)

# for s in suragchid15:
#     s.medeelel()
#     print("Dundaj dun:", s.dundaj())
#     s.dun_shalgah()
