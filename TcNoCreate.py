
# TC Kimlik No Oluşturma

top=0
import random
#from random import randint
tc = []
# tc.append(randint(1,5))
tc.append(random.randint(1,5)) 
for i in range(9):
    i=random.randint(0,9)
    tc.append(i)
for v in tc:
    top+=v
    top=top%10
    
tc.append(top)
print tc

