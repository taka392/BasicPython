import random                          
import math

a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO

def euclid(a,b) -> int:
    r = 1
    if a < b:
        a, b = b, a
    while r != 0:
        r = a % b
        a, b = b, r
    return a

result3 = euclid(int(a),int(b))
print(f"最大公約数は{result3}です。")


def is_euclid(a: int, b: int) -> bool: # 互いに素である(coprime)か判定。返り値がboolより、is~と命名
    gcm = euclid(a, b)                 # 問3の関数を使用。
    if gcm == 1:
        return True
    else:
        return False

result4 = euclid(a, b)
print(result4)
