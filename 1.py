# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
f = open('001.txt','r', encoding = 'utf8')
word = []
for line in f:
    word.append(line)
z1 =word[0].split(",")
z2 =word[1].split(",")
z3 =word[2].split(",")
z4 =word[3].split(",")

class business:
    def __init__(self,number,classification,name,price,discount):
        self.number=number
        self.classification=classification
        self.name=name
        self.price=price
        self.discount=discount
        
a =  business(z1[0],z1[1],z1[2],z1[3],z1[4])  
b =  business(z2[0],z2[1],z2[2],z2[3],z2[4])  
c =  business(z3[0],z3[1],z3[2],z3[3],z3[4])  
d =  business(z4[0],z4[1],z4[2],z4[3],z4[4])  

print("產品編號","分類","商品名稱","單價","促銷折扣")
print(a.number,a.classification,a.name,a.price,a.discount)
print(b.number,b.classification,b.name,b.price,b.discount)
print(c.number,c.classification,c.name,c.price,c.discount)
print(d.number,d.classification,d.name,d.price,d.discount)