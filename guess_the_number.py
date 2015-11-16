# -*- coding: utf-8 -*-

from random import randint, randrange

random_number = randint(0,3)
tahmin_hakki = 5

while(tahmin_hakki>0):
    choice = int(raw_input("Tahmininiz\n"))
    
    print ""
    
    if choice<random_number:
        print "daha buyuk bir syi giriniz\n"

    elif choice>random_number:
        print "daha kucuk bir sayi giriniz\n"
    elif choice == random_number:
        print "TEBRİKLER... "
        break

    tahmin_hakki=tahmin_hakki-1
    if(tahmin_hakki==0):
        print "Tahmin hakkiniz bitmiştir "
        break
    continue
