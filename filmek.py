lst = []
with open("filmek.txt", "r", encoding="utf-8") as file :
    for line in file:
        lst.append(line.strip())
print("2. feladat")
print(len(lst))
print("3. feladat")
db = 0
for i in range(0,len(lst), 1) :
    szokoz = True
    index = 0
    while szokoz:
        if lst[i][index] == " ":
            db += 1
            szokoz = False
        index += 1
        if index > len(lst[i])-1:
            szokoz = False
print(db)
print("4. feladat")
for i in range(0,len(lst),1):
    index = lst[i].upper().find("HÁROM")
    if index != -1:
        print(lst[i])
print("4/b")
for i in range(0,len(lst),1):
    index = lst[i].upper().find(" HÁROM ")
    if lst[i].upper().startswith("HÁROM "):
        print(lst[i])
    if lst[i].upper().endswith(" HÁROM"):
        print(lst[i])
    if index != -1:
        print(lst[i])
print("4/c")
szobe = input("Adj meg egy szót! : ")
for i in range(0,len(lst),1):
    index = lst[i].upper().find(szobe.upper())
    if index != -1:
        print(lst[i])
print("5. feladat")
betu = input("Adj meg egy betűt! : ")
fajl = open(f"{betu}.txt", "w", encoding="utf-8")
for i in range(0, len(lst), 1):
    if lst[i].upper().startswith(betu.upper()):
        fajl.write(f"{lst[i]}\n")
    