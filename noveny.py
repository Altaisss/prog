class Noveny:
    def __init__(self, be):
           self.nev = be

lst = []
with open("noveny.txt", "r", encoding="utf-8") as file :
    for line in file:
        lst.append(line.strip())

length = len(lst[0])
lengthin = 0
lengthmax = 0
for i in range(0,len(lst),1):
    if len(lst[i]) < length:
        lengthin = i
        length=len(lst[i])
    if len(lst[i]) > lengthmax:
        lengthmax=len(lst[i])
vanspace = True
j = 0
print(lst[lengthin])
print("2. Feladat\n")
for i in range(0,len(lst),1) :
    vanspace = True
    j = 0
    while vanspace:
        if lst[i][j] == " ":
            print(lst[i])
            vanspace = False
        else : 
            if j == len(lst[i])-1 :
                vanspace = False
        j += 1
print("3. feladar\n")
for i in range(0,len(lst),1) :
    index = lst[i].find("sás")
    if index != -1:
        print(lst[i])
        
print("4. Feladat\n")
betu = "e"
for i in range(0,len(lst),1):
    if lst[i][0].lower() == betu.lower() :
        print(lst[i])
print("5. feladat\n")
for i in range(0,len(lst),1):
    if lst[i][len(lst[i])-1].lower() == betu.lower() :
        print(lst[i])
print("6. feladat\n")
for i in range(0,len(lst),1):
    if lst[i][0].lower() == betu.lower() and lst[i][len(lst[i])-1].lower() == betu.lower():
        print(lst[i])
print("7. feladat")
for i in range(0,len(lst),1):
    valami = True
    j = 0
    while valami:     
        if lst[i][j].lower() == betu.lower() :
            print(lst[i])
            valami = False
        j +=1
        if j == len(lst[i]):
            valami = False
print("8.feladat\n")
be = input("Adj meg egy betűt: ")
for i in range(0,len(lst),1):
    valami = True
    j = 0
    while valami:     
        if lst[i][j].lower() == be.lower() :
            print(lst[i])
            valami = False
        j +=1
        if j == len(lst[i]):
            valami = False
print("9. feladat\n")
for i in range(0,len(lst),1):
    for j in range(0,lengthmax-len(lst[i]),1):
        print(" ", end="")
    print(lst[i])

print("10.-11. feladat") 
kisbetu = open("kisbetus.txt","w", encoding="utf-8")
nagybetu = open("nagybetus.txt", "w", encoding="utf-8")
for i in range(0,len(lst),1):
    kisbetu.write(f"{lst[i].lower()}\n")
    nagybetu.write(f"{lst[i].upper()}\n")

kisbetu.close()
nagybetu.close()
print("12. feladat")
szam = int(input("Adj meg egy számot:"))
szam = szam-1
if szam > len(lst) :
    print("Nincs ennyi növény a listán.")
else :
    if len(lst[szam]) > 10:
        print(lst[szam][:2], end="")
        for i in range(2,len(lst[szam])-2,1):
            if lst[szam][i] == " ":
                print(" ", end="")
            else:
                print(".", end ="")   
        print(lst[szam][len(lst[szam])-2:])
    else:
        print(lst[szam][:1], end="")
        for i in range(1,len(lst[szam])-1,1):
            if lst[szam][i] == " ":
                print(" ", end="")
            else:
                print(".", end = "")   
        print(lst[szam][len(lst[szam])-1:])
tipp = input("Találd ki! : ")
tippmax = len(lst[szam])//2
szamlalo = 1
kitalalt = True
while kitalalt:
    if tipp.upper() == lst[szam].upper():
        print("Eltaláltad!")
        kitalalt = False
    else:
        tipp = input("Próbáld újra! :")
        szamlalo += 1
    if szamlalo > tippmax :
        kitalalt = False
        print("Nem tudtad kitalalni.")
file.close()