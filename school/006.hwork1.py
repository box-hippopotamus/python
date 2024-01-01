
# # 鸡兔同笼
# arr = input("请输入鸡和兔子的总头数和总脚数，用空格隔开：").split(" ")
# head = int(arr[0])
# foot = int(arr[1])
#
# rabbit = int((foot - head * 2) / (4 - 2))
# chicken = head - rabbit
#
# print(f"兔子个数：{rabbit}，鸡的个数:{chicken}")

# # 回文数判断
# str = list(input("请输入数字："))
# flag = 1 # 假设是回文数
#
# for i in range(0,len(str) // 2):
#     if str[i] == str[len(str) - 1 - i]:
#         continue
#     else:
#         flag = 0 # 执行此语句说明不是回文数
#         break
#
# if flag: # 最终判断是不是回文数
#     print("是回文数")
# else:
#     print("不是回文数")

# # 放鞭炮
# num = int(input("请输入鞭炮数量："))
# count = 0
# arr = [0] * (num * 3)
# # 刘备放鞭炮
# for i in range(0, num, 1):
#     arr[i] = 1
# # 张飞放鞭炮
# for i in range(0, 2 * num, 2):
#     arr[i] = 1
# # 关羽放鞭炮
# for i in range(0, 3 * num, 3):
#     count = count + 1
#     arr[i] = 1
# print(f"响声共{sum(arr)}声,燃放时间为{count * 3 - 2}")


a = b = c = answer = s = x = y = [i for i in range(1, 10)]

