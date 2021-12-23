ls = []
n = int(input('ELementlar sonini kiriting: '))

for i in range(n):
    a = int(input())
    ls.append(a)

print(ls)

katta = max(ls)

print (katta)
print (ls.index(katta))


