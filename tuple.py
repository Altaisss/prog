def origtav(be):
    return (int(be[0])**2 + int(be[1])**2)**(1/2)

def egymastav(be, be2):
    if origtav(be) > origtav(be2):
        return origtav(be) - origtav(be2)
    else:
         return origtav(be2) - origtav(be)

def egymastol(be, be2):
    return ((be[0]-be2[0])**2 + (be[1] - be2[1])**2)**(1/2)
    
    
print("Adj meg egy RGB kod komponenseit! ")
r= int(input("R: "))
g = int(input("G: "))
b = int(input("B: "))
rgb = r, g, b
komp = ("piros", "zold", "kek")  
print(rgb)
if rgb[1] >1:
    print("van")
else: 
    print("nincs")
    
pont = (4, 5)
ponty = (6, 7)
print(origtav(pont))
print(egymastav(pont, ponty))
print(egymastol(pont, ponty))

