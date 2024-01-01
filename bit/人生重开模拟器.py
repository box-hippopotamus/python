# 人生重开模拟器
print(" ")
print("+------------------------------------------+")
print("|            花有重开日，人无再少年            |")
print("|            欢迎来到人生重开模拟器            |")
print("+------------------------------------------+")

# 设置初始属性
# 颜值，体力，家境，智力总和为20
print("你共可以支配20个点数至颜值，体质，智力，家境四个属性")
print("每个属性的点数范围在1-10")
while True:
    sum = 20
    face = int(input("请设置颜值属性："))
    if face < 1 or face > 10:
        print("颜值设置有误，请重新设置")
        continue
    sum -= face
    print(f"你还可以支配{sum}个点数")

    strong = int(input("请设置体质属性："))
    if strong < 1 or strong > 10:
        print("体质设置有误，请重新设置")
        continue
    sum -= strong
    print(f"你还可以支配{sum}个点数")

    iq = int(input("请设置智力属性："))
    if iq < 1 or iq > 10:
        print("智力设置有误，请重新设置")
        continue
    sum -= iq
    print(f"你还可以支配{sum}个点数")

    home = int(input("请设置家境属性："))
    if home < 1 or home > 10:
        print("家境设置有误，请重新设置")
        continue
    sum -= home

    if sum != 0:
        print(f"总点数分配为{20-sum}，请重新分配")
        continue
    break

# 生成角色性别
import random
gender = random.randint(1,2)
if gender == 1:
    gender = "boy"
    print("你出生了，你是个男孩")
else:
    gender = "girl"
    print("你出生了，你是个女孩")

# 设定出生点
point = random.randint(1,3)
if home == 10:
    print("你出生在国家首都，父母是高官政要")
    home += 1
    iq += 1
    face += 1
    strong += 1
elif 7 <= home <= 9:
    if point == 1:
        print("你出生在城市，父母是公务员")
        face += 2
    elif point == 2:
        print("你出生在城市，父母是企业家")
        home += 2
    elif point == 3:
        print("你出生在城市，父母是教授")
        iq += 2
elif 4 <= home <= 6:
    if point == 1:
        print("你出生三线城市，父母是医生")
        strong += 1
    elif point == 2:
        print("你出生在镇上，父母是中学老师")
        iq += 1
    elif point == 3:
        print("你出生在镇上，父母是个体户")
        home +=1
else:
    if point == 1:
        print("你出生在农村，父母是农民")
        strong += 1
        face -= 2
    elif point == 2:
        print("你出生在贫穷区，父母是无业游民")
        home -= 1
    elif point == 3:
        print("你出生在镇上，父母感情不和")
        strong -= 1
print(f"你当前的属性为：颜值：{face}  体质：{strong}  智力：{iq}  家境：{home}")
