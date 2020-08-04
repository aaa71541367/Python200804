import random
A=random.randint(1,10)
while True:
    B=input('猜數字1~10 :')
    B=int(B)
    if A==B:
        print('right')
    elif B>10 or B<1 :
        print('輸入錯誤')
    else:
        print('你猜錯了')
        