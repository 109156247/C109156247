x=input("請輸入一串小寫英文:")
x1=list(x)
a1=["a","e","i","o","u"]
for i in range(len(x1)):
    if x1[i] in a1:
        x1[i]="."
print("".join(x1))