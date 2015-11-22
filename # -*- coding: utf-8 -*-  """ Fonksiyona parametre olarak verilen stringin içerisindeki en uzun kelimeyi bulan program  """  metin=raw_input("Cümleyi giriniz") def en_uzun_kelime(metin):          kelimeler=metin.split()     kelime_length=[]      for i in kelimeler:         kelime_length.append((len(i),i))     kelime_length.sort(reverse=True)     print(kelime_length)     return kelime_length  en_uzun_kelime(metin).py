# -*- coding: utf-8 -*- 
""" Fonksiyona parametre olarak verilen stringin içerisindeki en uzun kelimeyi bulan program  """ 
metin=raw_input("Cümleyi giriniz") 
def en_uzun_kelime(metin):          
  kelimeler=metin.split()     
  kelime_length=[]      
  for i in kelimeler:         
  kelime_length.append((len(i),i))    
  kelime_length.sort(reverse=True)     
  print(kelime_length)     
  return kelime_length  

en_uzun_kelime(metin)           
