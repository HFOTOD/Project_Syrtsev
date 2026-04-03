f1 = open('text18-1.txt', encoding='UTF-8')
l = f1.readlines()
f1.close()

l[0], l[3] = l[3], l[0]

f2 = open('text18-2.txt', 'w')
f2.writelines(l)
f2.close()