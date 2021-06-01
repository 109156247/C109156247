str1=input("輸入s1為:")
str2=input("輸入s2為:")
a=[]
b=[]
c=d=0
for i in str1:
    a.append(i)
for k in str2:
    b.append(k)    
print(a)
print(b)
for i in str1:
    c=b.count(i)   
    if c==1:
        d=d+1
if d==len(str1):
    print("YES")
else:
    print("NO")   