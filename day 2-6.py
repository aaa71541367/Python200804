人數=input('有幾個人 :')
人數=int(人數)
成績表=[]
總分=0
for 第幾個 in range (人數):
    分數=input('輸入分數 :') 
    分數=float(分數)
    成績表.append(分數)
for 分數 in 成績表:
    總分=總分+分數    
print(總分)    
    