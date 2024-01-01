# 数值类型
# 整数类型
# print( )
# print(10/3)# 除法
# print(10%3)# 取余
# print(10//3)# 整除
# print(-10/3)
# print(-10%3)# -2
# print(-10//3)# 得到-4，python整除规则是：完成除法后，输出小于除法结果的最小整数，此处为小于-333...5的最大整数-4

# a=3
# b=10
# c=12.0
# d=5.0
# print( )
# print(b**a+c)#10**3+12.0 = 1012.0
# print(c%d+b//d-a)# 12.0%5.0+10//5.0-3 = 2+2-3 = 1.0

# 浮点数类型
# print( )
# print(8.125 - 6.125 == 2)# ==判等操作符，当判等成立，返回ture
# print(3.4 - 1.22 )


# 随机数类型

# import random
# def caishu():
#     i = 0
#     key = random.randint(1,10)
#     while i < 5:
#         guss = int(input("enter:"))
#         if key == guss:
#             print("good guess!")
#             break
#         elif guss > key:
#             print("guss>key try again")
#         else:
#             print("guss<key try again")
#         i += 1
#     else:
#         print("game over")
#         print("The key is:", key)
# caishu()

# import random
# rol = random.randint(1,9)
# col = random.randint(1,12)
# print( )
# print("这个学生是:", rol,"排" ,col,"列")
#
# import random
# student = random.randint(1,50)
# print( )
# print("这个学生是",student,"号")

# 布尔类型
# print( )
#
# x = 3
# b = 6
# if x % 2 == 0:
#     print(x,"是偶数")
# else:
#     print(x,"是奇数")
#
# if b % 2 == 0:
#     print(b,"是偶数")
# else:
#     print(b,"是奇数")

# print(3 and 4)  # 两者都为true，输出后一位
# print(4 and 3)
# print(0 and 4)  # 0为false，and为与，有0则0，直接输出0（短路）
# print(0 or 4)   # 0为false，or为或，有1则1，输出4
# print(2 or 3)   # 2已经为true，or为或，有1则1，直接输出2（短路）
# print(11 & 12)  # 按位与，转化为二进制后，每位进行与运算

# print(-10%3)# 2

print( )

y = 10
print("这是没有单引号的y，输出y的值")
print(y)
print("这是有单引号的y，输出y字母")
print('y')


