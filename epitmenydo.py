class Utca():
    def __init__(self,be): 
        adat = be.split(" ")
        self.adoszam = int(adat[0])
        self.utca = adat[1]
        self.hazszam = adat[2]
        self.sav = adat[3]
        self.ter = int(adat[4])
        
def ado(terulet, adosav):
    if adosav == "A":
        if terulet * 800 < 10000:
            return 0
        else:
            return terulet * 800 
    elif adosav == "B":
         if terulet * 600 < 10000:
            return 0
         else:
            return terulet * 600 
    else:
         if terulet * 100 < 10000:
            return 0
         else:
            return terulet * 100 
        
            
    

lst = []
savertek = []
file = open("utca.txt", "r")
savertek = file.readline().strip().split(" ")
with file:
    for line in file:
        lst.append(Utca(line.strip()))
print("2. feladat")
print(f"A mintában {len(lst)} telek szerepel")
print("3. feladat")
be = int(input("Adjon meg egy adószámot: "))
nincs = True
for i in range(0, len(lst), 1):
    if be == lst[i].adoszam:
        print(f"{lst[i].utca} utca {lst[i].hazszam}")
        nincs = False
if nincs:
    print("Nem szerepel az adatállományban")
    
print("4. feladat")
darab = [0,0,0]
osszeg = [0,0,0]
for i in range(0,len(lst),1):
    if lst[i].sav == "A":
        osszeg[0] += ado(lst[i].ter, lst[i].sav)
        darab[0] += 1
    if lst[i].sav == "B":
        osszeg[1] += ado(lst[i].ter, lst[i].sav)
        darab[1] += 1
    if lst[i].sav == "C":
        osszeg[2] += ado(lst[i].ter, lst[i].sav)
        darab[2] += 1
print(f"Az A sávba {darab[0]} telek esik, az adó {osszeg[0]} Ft")
print(f"Az B sávba {darab[1]} telek esik, az adó {osszeg[1]} Ft")
print(f"Az C sávba {darab[2]} telek esik, az adó {osszeg[2]} Ft")
print("5. feladat")
utcak = []
utcak.append(lst[0].utca)
for i in range(1, len(lst), 1):
    nincsbenne = True
    for j in range(0,len(utcak), 1):
        if lst[i].utca == utcak[j]:
            nincsbenne = False
    if nincsbenne:
        utcak.append(lst[i].utca)

for i in range(0,len(utcak), 1):
    sav = ""
    for j in range(0,len(lst), 1):
        if utcak[i] == lst[j].utca:
            if sav == "":
                sav = lst[j].sav
            elif sav != lst[j].sav:
                print(utcak[i])
                break
            
print("7. feladat")
irok = open("fizetendo.txt", "w")
adoszamok = []
adoszamok.append(lst[0].adoszam)
for i in range(1, len(lst), 1):
    nincsbenne = True
    for j in range(0,len(adoszamok), 1):
        if lst[i].adoszam == adoszamok[j]:
            nincsbenne = False
    if nincsbenne:
        adoszamok.append(lst[i].adoszam)
adoszamok.sort()
for i in range(0, len(adoszamok), 1):
    osszeg = 0
    for j in range(0, len(lst), 1):
        if adoszamok[i] == lst[j].adoszam:
            osszeg =+ ado(lst[j].ter, lst[j].sav)
    irok.write(f"{adoszamok[i]} {osszeg}\n")
            