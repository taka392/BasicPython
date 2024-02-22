a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO

def is_prime_num(number):
    is_prime = True
    if number == 1:
        is_prime = False
    else:
        for i in range(2,int(number**0.5+1)):
            if number % i == 0:
                is_prime = False
                break
    return print_number(is_prime,number)

def print_number(is_prime,number):
    if is_prime == True:
        print(f"{number}は素数です")
    else:
        print(f"{number}は素数ではありません")


is_prime_num(int(a))
is_prime_num(int(b))

