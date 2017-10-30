import string

L1 = ['adam', 'LISA', 'barT']

def normalized(s):
    return s[0].upper()+s[1:].lower()

L2 = list(map(string.capwords, L1))
L3 = list(map(normalized, L1))
L4 = list(map(lambda s:s[0].upper()+s[1:].lower(), L1))

print(L1)
print(L2)
print(L3)
print(L4)

#结果：
#['adam', 'LISA', 'barT']
#['Adam', 'Lisa', 'Bart']
#['Adam', 'Lisa', 'Bart']
#['Adam', 'Lisa', 'Bart']