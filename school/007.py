print()
# def big(ls):
#     m = 0
#     for i in range(0, len(ls)):
#         if ls[i] > ls[m]:
#             m = i
#     ls[m], ls[0] = ls[0], ls[m]
#     print(ls)
#
# ls = [4, 5, 1, 2, 0]
# big(ls)

def bubblesort(ls):
    for i in range(0, (len(ls) - 1)):
        for j in range(0, (len(ls) -i - 1)):
            if ls[j+1] < ls[j]:
                ls[j+1], ls[j] = ls[j], ls[j + 1]

# ls = [9 , 8 ,66, 8, 0,  5 , 1 ,2 ,7, 5, 4, 12, 12, 2, 9, 10]
ls = [9,8,7,6,5,4,3,2,1]
bubblesort(ls)
print(ls)


# def sum(n):
#     if n > 1:
#         return n + sum(n-1)
#     else:
#         return 1
#
# n = int(input("请输入数字："))
# num = sum(n)
# print(num)


# s = list(input("请输入数字"))
# y = s
# y = y.reverse()
#
# if s == y:
#     print("是回文数")
# else:
#     print("不是回文数")

#
# s = input("请输入数字")
# y = s
# y = str(y.reverse())
#
# if s == y:
#     print("是回文数")
# else:
#     print("不是回文数")


