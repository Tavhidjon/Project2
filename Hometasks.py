# 1)
# def idi():
#     date = input()
#     year, month, day = date.split('/')
#     if month == '10' and day == '31':
#         return "Bonfire toffee"
#     else:
#         return "toffee"
# print(idi())

# 2)
# def azSOLasr():
#     year = int(input())
#     century = (year + 99) // 100
#     return century
# print(azSOLasr())


# 3)
# def after_N_Months():
#     year = input()
#     months = input() 
#     if not year:
#         return
#     if not months:
#         return 
#     year = int(year)
#     months = int(months)
#     b = months // 12
#     c = year + b
#     return c
# print(after_N_Months())



# 4)

# from datetime import datetime
# def ruziivazshavanda():
#     a = input().strip()
#     b = datetime.strptime(a, "%Y%m%d")
#     c = b.strftime("%m/%d/%Y")
#     return c
# print(ruziivazshavanda())





# 5)
# from datetime import datetime
# def timeForMilkAndCookies():
#     a = input().strip()
#     b = datetime.strptime(a, "%Y,%m,%d")
#     return b.month == 12 and b.day == 24
# print(timeForMilkAndCookies())










# 6)
# from datetime import datetime
# def HAfta():
#     a = input().strip()
#     b = datetime.strptime(a, "%m/%d/%Y")
#     Ruzoi_hafta = b.strftime("%A")
#     return Ruzoi_hafta
# print(HAfta())





























