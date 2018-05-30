age = int(input("나이를 입력"))
height = int(input("키를 입력"))

if age>= 40:
    if height >= 170:
        print("키가 보통이상")
    else:
        print("키가 보통")
else:
    if height >= 175:
        print("키가 보통이상")
    else:
        print("키가 보통")