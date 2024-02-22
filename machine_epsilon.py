# TODO




def epsilon():
    e=1
    while (e + 1.0) > 1.0:
        e=e/2
    return 2*e
    
result = epsilon()
print(f"マシンイプシロンの結果は{result}です")