
# import random
#
# def caculate(i, listx, listy, listway, result):
#     listx[i] = x = random.randint(1, 10)
#     listy[i] = y = random.randint(1, 10)
#     listway[i] = way = random.randint(1,4)
#     if way == 1:
#         result[i] = int(input(f"第{i}题：{x} + {y} ="))
#     elif way == 2:
#         result[i] = int(input(f"第{i}题：{x} - {y} ="))
#     elif way == 3:
#         result[i] = int(input(f"第{i}题：{x} * {y} ="))
#     elif way == 4:
#         result[i] = int(input(f"第{i}题：{x} / {y} ="))
#
#
#
# print("欢迎使用算数自测程序，测试开始：")
# listx = [0] * 10
# listy = [0] * 10
# listway = [0] * 10
# result = [0] * 10
#
# for i in range(0,10):
#     caculate(i, listx, listy, listway, result)

print("")

import random
def caculate(i, dict):
    dict["a"] = random.randint(1, 10)
    dict["b"] = random.randint(1, 10)
    dict["way"] = random.randint(1,4)
    if dict["way"] == 1:
        dict["result"] = int(input(f"第{i + 1}题：{dict["a"]} + {dict["b"]} ="))
    elif dict["way"] == 2:
        dict["result"] = int(input(f"第{i + 1}题：{dict["a"]} - {dict["b"]} ="))
    elif dict["way"] == 3:
        dict["result"] = int(input(f"第{i + 1}题：{dict["a"]} * {dict["b"]} ="))
    elif dict["way"] == 4:
        dict["result"] = float(input(f"第{i + 1}题：{dict["a"]} / {dict["b"]} ="))
        dict["result"] = "%.2f" % dict["result"]
def result(i, dict):
    if dict["way"] == 1:
        if dict["a"] + dict["b"] == dict["result"]:
            print(f"第{i + 1}题：{dict["a"]} + {dict["b"]} = {dict["result"]} √")
            return True
        else:
            print(f"第{i + 1}题：{dict["a"]} + {dict["b"]} = {dict["result"]} × 正确答案为 {dict["a"] + dict["b"]}")
            return False
    elif dict["way"] == 2:
        if dict["a"] - dict["b"] == dict["result"]:
            print(f"第{i + 1}题：{dict["a"]} - {dict["b"]} = {dict["result"]} √")
            return True
        else:
            print(f"第{i + 1}题：{dict["a"]} - {dict["b"]} = {dict["result"]} × 正确答案为 {dict["a"] - dict["b"]}")
            return False
    elif dict["way"] == 3:
        if dict["a"] * dict["b"] == dict["result"]:
            print(f"第{i + 1}题：{dict["a"]} * {dict["b"]} = {dict["result"]} √")
            return True
        else:
            print(f"第{i + 1}题：{dict["a"]} * {dict["b"]} = {dict["result"]} × 正确答案为 {dict["a"] * dict["b"]}")
            return False
    elif dict["way"] == 4:
        if "%.2f" % (dict["a"] / dict["b"]) == dict["result"]:
            print(f"第{i + 1}题：{dict["a"]} / {dict["b"]} = {dict["result"]} √")
            return True
        else:
            print(f"第{i + 1}题：{dict["a"]} / {dict["b"]} = {dict["result"]} × 正确答案为 {"%.2f" % (dict["a"] / dict["b"])}")
            return False

print("欢迎使用算数自测程序，测试开始：")

list = [{"a": 0, "b": 0, "way": 0, "result": 0} for i in range(10)]

for i in range(0, 10):
    caculate(i, list[i])

print("答题结束，您的答题结果为：")
count = 0
for i in range(0, 10):
    if result(i, list[i]):
        count = count + 10

print(f"您本次测试最终得分为{count}分！")
