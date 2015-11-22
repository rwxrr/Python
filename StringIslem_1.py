def string(metin):
    if len(metin)<2:
        return " "
    else:
        return metin[0:2] + metin[-2:]

metin=raw_input("metni giriniz")

print string(metin)
