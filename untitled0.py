mevalar = ['olma', 'olcha', 'nok']
mevalar.insert(1,'tarvuz')
mevalar.append('uzum')
narx = [1000,2000,3000]
mevalar.extend(narx[0:2])
mevalar.pop()
a = mevalar.pop()
del mevalar[2]
# mevalar.clear()


# if x in mevalar:
#     print('Bor')
# else:
#     print('yuq')
print(mevalar)
# print(a)