a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO




def eulid(a,b):
    r = 1
    if a < b:
        a, b = b, a
    while r != 0:
        r = a % b
        a, b = b, r
    return int(a)
    
result = eulid(int(a),int(b))
print(f"最大公約数は{result}です。")