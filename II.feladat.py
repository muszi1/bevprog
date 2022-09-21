a=int(input("Adjon meg egy a-t: "))
b=int(input("Adjon meg egy b-t: "))
c=int(input("Adjon meg egy c-t: "))
d=(b*b-4*a*c)
if d==0:
    print("Az egyenletnek egy megoldása van.")
elif d<0:
    print("Az egyenletnek nincs megoldása.")
elif d>0:
    x1=(-b)+d**0.5/(2*a)
    x2=(-b)-d**0.5/(2*a)
    print("Az egyenletnek két megoldása van.")
    print("x1="+str(x1)+" "+"x2="+str(x2))