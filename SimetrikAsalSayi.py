
def reverse_int(n):
    return int(str(n)[::-1])

print 2

for i in range(3,1001):

    bolundu = False
    for j in range(2,i):
            if i % j == 0 or reverse_int(i)%j==0:
                bolundu=True
                
    if bolundu == False:
        print i




