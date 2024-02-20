from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------


from math import sin
import math    # 円周率を使うためのimport
# --example--
# print(sin(0))
# >>> 0
# -----------

S = 0               
N = 100             
a = 0               
b = 0.5*(math.pi) 

h = (b-a)/N

for i in range(1,N+1): 
    S += h / 2 * (sin(a + (i - 1) * h) + sin(a + i * h))
print(f'sin関数の[{a},{b}]における積分値は、{S}です。')