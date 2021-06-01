f = {'蘋果':'紅色','香蕉':'黃色','葡萄':'紫色','藍莓':'藍色','橘子':'橘色'}
print(f.keys())
flu = str(input())
if(f.get(flu) != None):
    print(flu + "為" + str(f.get(flu)))
else:
    print("字典中沒有" + flu) 