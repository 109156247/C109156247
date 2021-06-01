a,b=map(int, input("請輸入考試次數及學生數:").split())
c=map(float, input("每次考試所佔的比率:").split())
c1=list(c)
d=[]
s=0
for i in range(b):
    d1=map(int, input("").split())
    d.append(list(d1))
for j in range(a):
    for i in range(b):
        s+=d[i][j]*c1[j]
print("全班的總平均值為:%.2f"%(s/b))
        