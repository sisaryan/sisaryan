#emrullahın ağzını açık bırakacak o uygulama.
print("Eray Sona Padişahın ve emrullahın Şifreli mesajlaşma uygulamasına hoşgeldiniz. ")
while True:

    print("  Hangi işlemi yapmak istersiniz.  :   ")
    print("  ") #satir boşluğu bıraktım çirkin gözükmesin diye
    print("  Mesajı şifreye çevir ==> 1 ")
    print("  Şifreyi mesaja çevir ==> 2 ")
    print("  ") #satir boşluğu bıraktım çirkin gözükmesin diye
    giris = int(input("1 veya 2:  "))
    
    if giris == 1:
        print("  ")
        print("^".center(70,"^"))
        print("Mesajı şifreye çevirme işlemine girdiniz: ")
        print("^".center(70,"^"))

        sifre1 = input("Şifrelenecek mesajı giriniz:  ")
        sifre1len = len(sifre1)
        sifre1len = str(sifre1len)
        sifreTrue = sifre1len.endswith("0") or sifre1len.endswith("2") or sifre1len.endswith("4") or sifre1len.endswith("6") or sifre1len.endswith("8")
        
        if sifreTrue == True:
            sifre1 = sifre1 + " "
        sifre11 = sifre1[::-2]             #şifrenin ilk yarısını ikişerli şekilde tersine çeviriyorum
        sifre111 = sifre1 + str(1)          
        sifre111 = sifre111[::-2]          #şifrenin diğer yarısını ikişerli şekilde tersine çeviriyorum
        sifreson = sifre111 + sifre11      #artı bir olan şifreyi ilke sonra diğerini sona ekleyip topluyorum
        
        print(" ")
        print("Şifrelenmiş mesajınız kullanıma hazır:  ",sifreson)
        print("Şifrenizin karakter sayısı: ", len(sifreson))
        print("  ")
        print("Padişah Eray'ın programını kullandığınız için teşekkür ederim.  ")
        print("^".center(70,"^"))
        print("  ")


    if giris == 2:
        print(" ")
        print("^".center(70,"^"))
        print("Mesajı şifreye çevirme işlemine girdiniz. ")
        print("^".center(70,"^"))

        mesaj2 = input("Şifreyi giriniz:  ")
        mesaj2 = mesaj2.strip()
        mesajkaraktersayisi = len(mesaj2)

        mesajkaraktersayisininyarisi = round(mesajkaraktersayisi / 2)  # burada da kesim işlemi için ikiye böldün ve yuvarlamasını yaptın
        mesajkaraktersayisininyarisi = mesajkaraktersayisininyarisi
        #şimdiyse ikiye böleceğim
        mesajyaribir = mesaj2[:mesajkaraktersayisininyarisi:] #ilk başı aldığın sayının eksilisi ile sondan alabilirsin
        mesajyariiki = mesaj2[mesajkaraktersayisininyarisi::]
        #şimdiyse ters çevireceğim
        mesajyaribir = mesajyaribir[::-1]
        mesajyariiki = mesajyariiki[::-1]
        #şimdiyse eşitlemeleri yapmam gerekecek

        if True:

            e1 = mesajyariiki[0:1]
            e2 = mesajyaribir[0:1]
            e3 = mesajyariiki[1:2]
            e4 = mesajyaribir[1:2]
            e5 = mesajyariiki[2:3]
            e6 = mesajyaribir[2:3]
            e7 = mesajyariiki[3:4]
            e8 = mesajyaribir[3:4]
            e9 = mesajyariiki[4:5]
            e10 = mesajyaribir[4:5]
            e11 = mesajyariiki[5:6]
            e12 = mesajyaribir[5:6]
            e13 = mesajyariiki[6:7]
            e14 = mesajyaribir[6:7]
            e15 = mesajyariiki[7:8]
            e16 = mesajyaribir[7:8]
            e17 = mesajyariiki[8:9]
            e18 = mesajyaribir[8:9]
            e19 = mesajyariiki[9:10]
            e20 = mesajyaribir[9:10]
            e21 = mesajyariiki[10:11]
            e22 = mesajyaribir[10:11]
            e23 = mesajyariiki[11:12]
            e24 = mesajyaribir[11:12]
            e25 = mesajyariiki[12:13]
            e26 = mesajyaribir[12:13]
            e27 = mesajyariiki[13:14]
            e28 = mesajyaribir[13:14]
            e29 = mesajyariiki[14:15]
            e30 = mesajyaribir[14:15]
            e31 = mesajyariiki[15:16]
            e32 = mesajyaribir[15:16]
            e33 = mesajyariiki[16:17]
            e34 = mesajyaribir[16:17]
            e35 = mesajyariiki[17:18]
            e36 = mesajyaribir[17:18]
            e37 = mesajyariiki[18:19]
            e38 = mesajyaribir[18:19]
            e39 = mesajyariiki[19:20]
            e40 = mesajyaribir[19:20]
            e41 = mesajyariiki[20:21]
            e42 = mesajyaribir[20:21]
            e43 = mesajyariiki[21:22]
            e44 = mesajyaribir[21:22]
            e45 = mesajyariiki[22:23]
            e46 = mesajyaribir[22:23]
            e47 = mesajyariiki[23:24]
            e48 = mesajyaribir[23:24]
            e49 = mesajyariiki[24:25]
            e50 = mesajyaribir[24:25]
            e51 = mesajyariiki[25:26]
            e52 = mesajyaribir[25:26]
            e53 = mesajyariiki[26:27]
            e54 = mesajyaribir[26:27]
            e55 = mesajyariiki[27:28]
            e56 = mesajyaribir[27:28]
            e57 = mesajyariiki[28:29]
            e58 = mesajyaribir[28:29]
            e59 = mesajyariiki[29:30]
            e60 = mesajyaribir[29:30]
            e61 = mesajyariiki[30:31]
            e62 = mesajyaribir[30:31]
            mesaj = e1+e2+e3+e4+e5+e6+e7+e8+e9+e10+e11+e12+e13+e14+e15+e16+e17+e18+e19+e20+e21+e22+e23+e24+e25+e26+e27+e28+e29+e30+e31+e32+e33+e34+e35+e36+e37+e38+e39+e40+e41+e42+e43+e44+e45+e47+e46+e47+e48+e49+e50+e51+e52+e53+e54+e55+e56+e57+e58+e59+e60+e61+e62
            mesajlen = len(mesaj)
            mesajlen = mesajlen - 1
            mesaj = mesaj[:mesajlen]

        if True:
            mesajimiz = mesaj       #kelime bulma uygulaması
            print(" ")
            mesajimizharf = len(mesajimiz)
            mesajimizkelime = len(mesajimiz.split()) 
            mesajimizcumle1 = len(mesajimiz.split('.')) #   '.' içerisine aldığımızda str olarak gözüktüğü için mantıklı yani
            mesajimizcumle2 = len(mesajimiz.split("?")) 
            mesajimizcumle = mesajimizcumle1 + mesajimizcumle2 - 1
            print("Şifresi çözülmüş mesajınız:  ", mesaj)

            yazi1 = "mesaj harf sayısı: " + str(mesajimizharf)
            yazi2 = "mesaj kelime sayısı: " + str(mesajimizkelime)
            yazi3 = "mesaj cümle sayısı: " + str(mesajimizcumle)
            print(yazi1)
            print(yazi2)
            print(yazi3)
        print("^".center(70,"^"))
        print(" ")