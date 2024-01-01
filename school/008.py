# def bubble_sort(ls):
#     for i in range(0, (len(ls)-1)):
#         flag = 1
#         for j in range(0, (len(ls)-i-1)):
#             if ls[j+1] < ls[j]:
#                 ls[j+1], ls[j] = ls[j], ls[j+1]
#                 flag = 0
#         if flag:
#             break
#
# ls = input("请输入一个列表：").split(" ")
# bubble_sort(ls)
# print(ls)

# def bubblesort(ls):
#     for i in range(0, len(ls) - 1):
#         flag = 1
#         for j in range(0, len(ls) - i - 1):
#             if ls[j + 1] > ls[j]:
#                 ls[j + 1], ls[j] = ls[j], ls[j + 1]
#         if flag:
#             break
#
# ls = input("请输入一个列表：").split(" ")
# bubblesort(ls)
# print(ls)

# def exchange():
#      num = int(input(""))
#      s = " "
#      while num:
#          s = str(num % 2) + s
#          num = num // 2
#      print(s)
#
# exchange()

# def F(a):
#     if len(a) == 1:
#         return a[0]
#     else:
#         return F(a[1:]) + a[0]
#

