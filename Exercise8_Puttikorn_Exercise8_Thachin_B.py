print("Welcome to IT12345 ")
userIn = input("Please enter your User Name : ")
passWd = input("Please enter your Password : ")
pingpong = "puttikorn"

if userIn == itadmin and passWd == "it1234567":
    print("----Welcome to it12345 restuarant---")
    print("   Please selected the food you like")
    print("")
    print(" 1 ปลาทับทิมทอดทั้งตัว  115 บาท")
    print(" 2 มันฝรั่งทอดทั้งเปลือก  45 บาท")
    print(" 3 สลัดผักซอสทาร์ทาร์   60 บาท")
    print(" 4 เปปซี่             20 บาท")
    print("")
    menu1 = int(input("รายการที่ 1 >"))
    if menu1 == 1:
        a = 115
    elif menu1 == 2:
        a = 45
        print(menu1)
    elif menu1 == 3:
        a = 60
    elif menu1 == 4:
        a = 20
    menu2 = int(input("รายการที่ 2 >"))
    if menu2 == 1:
        b = 115
    elif menu2 == 2:
        b = 45
    elif menu2 == 3:
        b = 60
    elif menu2 == 4:
        b = 20
    menu3 = int(input("รายการที่ 3 >"))
    if menu3 == 1:
        c = 115
    elif menu3 == 2:
        c = 45
    elif menu3 == 3:
        c = 60
    elif menu3 == 4:
        c = 20

    toTal = a + b + c
    print("")
    print("=== Total ===", toTal, "บาท")
    print("/////ขอบคุณมากนะครับ//////")
