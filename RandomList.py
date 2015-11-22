import random

liste=[]

for i in range(10):
    liste.append(random.randint(1,10))

print liste

even_list=[]
for i in liste:
    if i%2==0:
        even_list.append(i)
print even_list
