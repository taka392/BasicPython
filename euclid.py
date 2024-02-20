a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO



def eulid(a,b):
    if a < b:
        a, b = b, a
    while b != 0:
        q = a // b
        r = a % b
        a = b
        b = r
    
result = eulid(int(a),int(b))
print("最大公約数は{}です。".format(a))