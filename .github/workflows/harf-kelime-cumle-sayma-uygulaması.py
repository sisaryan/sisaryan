print(''' "kaç karakter kelime?" uygulamasına hoşgeldiniz. ''')
while True:

    yazi = input("yazinizi giriniz: ")
    print(" ")
    yaziharf = len(yazi)
    yazikelime = len(yazi.split()) 
    yazicumle1 = len(yazi.split('.')) #   '.' içerisine aldığımızda str olarak gözüktüğü için mantıklı yani
    yazicumle2 = len(yazi.split("?")) 
    yazicumle = yazicumle1 + yazicumle2 - 1

    yazi1 = "yazınızın harf sayısı: " + str(yaziharf)
    yazi2 = "yazınızın kelime sayısı: " + str(yazikelime)
    yazi3 = "yazınızın cümle sayısı: " + str(yazicumle)
    print(yazi1)
    print(yazi2)
    print(yazi3)
    print(" ")
    print(" ")