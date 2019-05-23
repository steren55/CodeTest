'''
DAY 5
'''
import time
import math

# Homework
# 1.
# 找出100~999之间的所有水仙花数
# 水仙花数是各位立方和等于这个数本身的数
# 如: 153 = 1**3 + 5**3 + 3**3
for x in range(100, 1000):
    a = x // 100
    b = x // 10 % 10
    c = x % 10
    if (x == a*a*a+b*b*b+c*c*c):
        print(x, end='\t')
print()
print()

# 2.
# 找出1~9999之间的所有完美数
# 完美数是除自身外其他所有因子的和正好等于这个数本身的数
# 例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
# start = time.process_time()
# for x in range(1, 10000):
#     sum = 0
#     for xx in range(1, x):
#         if (x % xx == 0):
#             sum += xx
#     if (x == sum):
#         print(x, end=' ')
# end = time.process_time()
# print("-> Time:", (end - start), "s")
# print()


start = time.process_time()
for num in range(1, 10000):
    sum = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            sum += factor
            if factor > 1 and num / factor != factor:
                sum += num / factor
    if sum == num:
        print(num, end=' ')
end = time.process_time()
print("-> Time:", (end - start), "s")
print()

# 3.
# 求解《百钱百鸡》问题
# 1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
# 问公鸡 母鸡 小鸡各有多少只
total = 100
for x in range(0, total // 5 + 1):
    for y in range(0, total // 3 + 1):
        z = total - x- y
        if (x * 5 * 3 + y * 3 * 3 + z * 1) == total * 3:
            print(x, y, z)
print()


# 4.
# 输出斐波那契数列的前20个数
# 1 1 2 3 5 8 13 21 ...
a = 0
b = 1
for i in range(0, 20):
    if i is 0:
        print(i, end=' ')
    else:
        (a , b) = (b , a + b)
        print(a, end=' ')
print()
print()

# 5.
# Craps赌博游戏
# 玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
# 如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
# 玩家再次要色子 如果摇出7点 庄家胜
# 如果摇出第一次摇的点数 玩家胜
# 否则游戏继续 玩家继续摇色子
# 玩家进入游戏时有1000元的赌注 全部输光游戏结束
from random import randint

money = int(1000)
print("Your money:", money)
while money > 0:
    bet = money
    print("Bet:", bet)
    while bet > 0:
        pt = randint(2, 12)
        print("First Dice:", pt)
        if (pt == 7) or (pt == 11):
            money += bet
            print("Win:", bet, "-> Total:", money)
            break
        elif (pt == 2) or (pt == 3) or (pt == 12):
            money -= bet
            print("Lose:", bet, "-> Total:", money)
            break
        else:
            while True:
                new_pt = randint(2, 12)
                print("Dice:", new_pt)
                if (new_pt == 7):
                    money -= bet
                    print("Lose:", bet, "-> Total:", money)
                    bet = 0
                    break
                elif (new_pt == pt):
                    money += bet
                    print("Win:", bet, "-> Total:", money)
                    bet = 0
                    break
print("Game Over!")

    


