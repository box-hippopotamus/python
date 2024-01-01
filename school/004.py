print("")

# dict1 = {"zhangsan": 169, "lisi": 177, "wanglaowu": 188}
# print(dict1["zhangsan"])
# dict1 ["laoliu"] = 175
# print(dict1["laoliu"])
# dict1.pop("laoliu")
# print(dict1)
#
# L= L1 =[1,2,3]
# L = L + [4]
# print(L)
# print(L1)

# print("Excellent",end=" ")
# print("good")

#
# num = int(input("输入年份："))
#
# if (num % 400 == 0) or ((num % 100 != 0) and (num % 4 == 0)):
#     print(f"{num} 年是一个闰年")
# else:
#     print(f"{num} 年是一个平年")
#


# import random
# rol = random.randint(1,10)
# col = random.randint(1,5)
# direction = random.randint(1,2)
#
# if direction == 1:
#     print(f"请左侧第{rol}排第{col}列的同学回答问题")
# else:
#     print(f"请右侧第{rol}排第{col}列的同学回答问题")

# i = 3
# while i < 101:
#     print(i)
#     i += 1

# arr = [1, 2, 3, 4, 5]
#
# for i in arr:
#     print(i, end=" ")
#
# print()
# for i in range(1, 6):
#     print(i, end=" ")

for i in range(100, 1000):
    x = i
    count1 = x % 10
    x = x // 10
    count2 = x % 10
    x = x // 10
    count3 = x % 10
    if i == (count1**3 + count2**3 + count3**3):
        print(i, end=" ")