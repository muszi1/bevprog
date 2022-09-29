#1.feladat
import math

korterulete=int(input("Adja meg a kör sugarát:"))
t=korterulete*korterulete*math.pi
print(t)
a_oldal=int(input("Adja meg a téglalap a oldalát:"))
b_oldal=int(input("Adja meg a téglalap b oldalát:"))
t2=a_oldal*b_oldal
print(t2)
gúlav=(t*a_oldal)/3
print(gúlav)



#2.feladat
def fibonacci(n):
    return n if n<2 else fibonacci(n-2)+fibonacci(n-1)

print (fibonacci(8))




#3.feladat
"""def distance(p1, p2):
    AB=math.sqrt((p1(0)-p2(0))**2+(p1(1)-p2(1))**2)
    return AB


p1 = (1, 2)
p2 = (6, 5)
print('A ket pont kozti tavolsag:', distance(p1, p2))"""

#4.feladt
szam = input('Irjon be egy tetszoleges szamot')
szam_visszafele = ""
vissza = []

for i in szam:
    vissza.append(i)

for i in range(len(vissza)-1,-1,-1):
    szam_visszafele += vissza[i]

if int(szam_visszafele) == int(szam):
    print('Tukorkepe')
else:
    print('Nem tukorkepe')
