
# keo bua bao
# 1    2   3
import random

print("Trò chơi: keo - bua - bao")
me = input("Ban ra cai gi?: ")
robot = random.randint(1,3)
if (robot == 1):
    you = "keo"
    if (me == you):
        kq = "Hoa"
    elif (me == "bua"):
        kq = "Ban Thang"
    else: 
        kq = "Ban Thua"
elif (robot == 2):
    you = "bua"
    if (me == you):
        kq = "Hoa"
    elif (me == "bao"):
        kq = "Ban Thang"
    else: 
        kq = "Ban Thua"
else :
    you = "bao"
    if (me == you):
        kq = "Hoa"
    elif (me == "keo"):
        kq = "Ban Thang"
    else: 
        kq = "Ban Thua"

print("Ban chon:",me, " May chon:",you)
print("=>",kq)