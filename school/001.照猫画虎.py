# for i in range(1,5):
#     print(i)

# def F(x,y):
#     return(x*x+y*y)
# print(F(2,1))

# import random
# def caishu():
#     i=0
#     key = random.randint(1,10)
#     while i<5:
#         guess = int (input("enter"))
#         if key == guess:
#             print("good guess!")
#             break
#         elif guess>key:
#             print("guess>key try again")
#         else:
#             print("guess<key try again")
#             i += 1
#     else:
#         print("game over")
#         print("The key is:",key)
# caishu()

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

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-np.pi, np.pi, 0.01)
y = np.sin(x)
plt.plot(x, y, 'g')
plt.show()
