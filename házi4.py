def valid(text,chars):
    for x in text:
        for y in chars:
            if x==y:
                print(x)
text=input("Írj be valalmit:")
chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
valid(text,chars)

def szavak(szó1,szó2):
    print(szó2+" "+szó1)
szó1=input("Adjon meg az első szót ")
szó2=input("Adja meg a második szót ")
szavak(szó1,szó2)


code="kwwsv=22|rxwx1eh2gTz7z<Zj[fT"
asd=[]
megfejtes=[]
for x  in code:
    asd.append(ord(x)-3)
for i in asd:
    megfejtes.append(chr(i))
print("\n".join(megfejtes),end="")
