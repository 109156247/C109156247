one=input("檢測的字串(end結束):")
while one!="end":
    one1=list(one)
    two=input("檢測的單一字元:")  
    if one!="end":
        a=one1.count(two)
        print("字元",two,"出現次數為:",a)
    one=input("檢測的字串(end結束):")
    if one=="end":
        print("檢測結束")