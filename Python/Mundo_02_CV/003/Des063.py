n = int(input("Quantos termos quer mostrar? "))
print("-"*30)
t1 = 0
t2 = 1
c = 3
t3 = 0
print("{} → {}".format(t1, t2), end='')
while c <= n:
    t3 = t1 + t2
    print("→ {}".format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print('')
print('~'*30)
print("FIM!!")