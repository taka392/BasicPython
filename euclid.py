import random                          
import math

a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO
def euclid(a,b) -> int: # ユークリッドの互除法
    r = 1
    if a < b:
        a, b = b, a
    while r != 0:
        r = a % b
        a, b = b, r
    return a

result3 = euclid(int(a),int(b))
print(f"最大公約数は{result3}です。")


def is_euclid(a: int, b: int) -> bool: # 互いに素
    gcm = euclid(a, b)                 
    if gcm == 1:
        return True
    else:
        return False

result4 = euclid(a, b)
print(result4)
