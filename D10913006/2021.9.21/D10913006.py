ID = input("請輸入學號=>")
name_list = input("請輸入姓名=>")
name = input("請輸入名字=>")
print("(輸出)學號：" , ID)
print("(輸出)姓名：" , name + name_list)

year = int(input ("請輸入出生年 (國民)=>"))
cm = float(input ("請輸入身高 (cm)=>"))
kg = float(input ("請輸入體重 (kg)=>"))

BMI = kg / ((cm * cm )/10000)
print("(輸出) 年齡：" , 110 - year ,"歲，")
print("(輸出)身高=" , cm ,"公分" , end = "" )
print("，(輸出)體重=" , kg ,"公斤" , end = "" )
print("，(輸出)BMI = " , BMI )

print("hello world")