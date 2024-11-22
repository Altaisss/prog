class Noveny:
    def __init__(self, be):
           self.nev = be

lst = []
with open("noveny.txt", "r", encoding="utf-8") as file :
    for line in file:
        lst.append(line.strip())

length = len(lst[0])
lengthin = 0
for i in range(0,len(lst),1):
    if len(lst[i]) < length:
        lengthin = i
        length=len(lst[i])
vanspace = True
j = 0
print(lst[lengthin])
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
