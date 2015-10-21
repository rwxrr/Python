# -*- coding: utf-8 -*-
import goslate

gs=goslate.Goslate()
print "Cikis icin  : q veya Q"
while True:
    
    
    print "1 : İngilizce- Türkçe \n 2 : Türkçe-İngilizce "
    tercih=int(raw_input("Seciminiz : 1 veya 2 \n"))
    if tercih==1:
        
        word=raw_input("Cevrilecek kelime \n ->> ")
        solved=gs.translate(''+word, 'tr')
        print "kelime ceviriniz \n ->> " + solved
        continue
    
        if word=='q' or 'Q':
            break

        

    if tercih==2:
        
        word=raw_input("Cevrilecek kelime \n ->> ")
        solved=gs.translate(''+word,'en')
        print "kelime ceviriniz \n ->>" + solved
        continue
        if word=='q' or 'Q':
            break

        
