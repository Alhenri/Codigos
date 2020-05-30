from math import pow
n = int(input())
s = str(int(2**n))
tam = len(s)
if tam > 50:
    n = int(tam/50)
    for c in range(0, n):
        print(s[(c*50):((c+1)*50)])
    print(s[(n*50):])
else:
    print(s)
