list=[]
for i in range (334):
    list.append(3 * i)
for g in range (200):
    if (5 * g) in list:
        continue
    else:
        list.append (5 * g)
print (sum (list))
