a=input("請輸入值為:").split(",")
a.sort()
b=list(reversed(a))
a1=""
b2=""
for i in range(len(a)):
    a1=a1+a[i]
    b2=b2+b[i]
b=int(b2)-int(a1)

print(str(b))