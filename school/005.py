print()


# 判断一个数是不是质数
# def prime(a,b):
#     b = 8
#     a = b // 2
#     while a > 1:
#         if b % a == 0:
#           print("b is prime")
#           break
#         a = a - 1
#     else:
#         print("b is not prime")
#

# # for与range函数
# for i in range(10):
#     print(i)
#
# for i in range(1, 51):
#     print(i, end=" ")
#
# for i in range(-10, -100, -30):
#     print(i, end=" ")

# arr = [1, 2, 3, 4, 5, 6, 7]
# tmp = arr[0]
# for i in range(0, len(arr) - 1):
#     arr[i] = arr[i + 1]
# arr[len(arr) - 1] = tmp
# print(arr)
#
# # 求这是2023的第几天
# data = input("请输入日期:\n").split("/")
# month = int(data[0])
# day = int(data[1])
# daysum = 0
# list_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
# for i in range(0, month - 1):
#     daysum = daysum + list_month[i]
# daysum = daysum + day
#
# print(f"这是2023年的第{daysum}天")

#
# for i in range(4):
#     for j in range(5):
#         print("*", end=" ")
#     print()


# for i in range(4):
#     for j in range(i):
#         print("*", end=" ")
#     print()

for i in range(1, 10):
    for j in range(i):
        print(f"{i} * {j + 1} = {i*(j+1)} ", end=" ")
    print()