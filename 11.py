m,d=map(int,input("輸入月及日為：").split())
one=m*100+d
if one<121 or one>1221:
    print("星座為：Capricorn")
elif 219>one>121:
    print("星座為：Aquarius")
elif 321>one>218:
    print("星座為：Pisces")
elif 421>one>320:
    print("星座為：Aries")
elif 522>one>420:
    print("星座為：Taurus")
elif 622>one>521:
    print("星座為：Gemini")
elif 723>one>621:
    print("星座為：Cencer")
elif 824>one>722:
    print("星座為：Leo")
elif 924>one>823:
    print("星座為：Virgo")
elif 1024>one>923:
    print("星座為：Libra")
elif 1123>one>1023:
    print("星座為：Scorpio")
elif 1222>one>1122:
    print("星座為：Sagittarius")
