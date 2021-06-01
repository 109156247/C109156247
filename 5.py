M = int(input("請輸入階乘數M:"))
total = int(1)
N = int(1)
while (total <= M):
    N = N +1
    total = total * N
print("超過M為%s的最小階層為N值為:%s"%(M,N)) 