# emrullahın ağzını açık bırakacak bir başka uygulama- KELİME EZBERLEME UYGULAMASI VEYA DERS ÇALIŞMA UYGULAMASI.
import random
while True:
    if True:
        print("*************".center(85," "))
        print("     Kelime ezberleme uygulamasına hoşgeldiniz.     ".center(85,"*"))
        print("*************".center(85," "))
        print(" ")
        print("Kullanma talimatları; ")
        print("1. kural -> Öncelikle ezberlemeniz gereken kelimeleri girmelisiniz.")
        print("2. kural -> Eğer kelimelere çalışırken tekrar kelime girmek isterseniz cevap kısmına 'kelime gir' yazmanız yeterli.")
        print(" ")
        #Eğer istersek kodlarda değişiklik yapıp sırf kelime ingilizce türkçe yapmak veya ders çalışmak için ayarlayabilirz.
    englishword = []
    turkishword = []
    for i in range(15):
        i += 1
        englishword.append(input(f"{i}. kelimenizin V2 – Past Simple hali: ").lower())
        turkishword.append(input(f"{i}. kelimenizin V3 – Past Participle hali: ").lower())
        print(" ")
        if i == 5:
            print("V2 – Past Simple hali kelimeleriniz: ",turkishword)
            print("V3 – Past Participle Kelimeleriniz: ",englishword)
            print(" ")
        if i == 10:
            print("V2 – Past Simple kelimeleriniz: ",turkishword)
            print("V3 – Past Participle Kelimeleriniz: ",englishword)
            print(" ")
        if i == 15:
            print("V2 – Past Simple kelimeleriniz: ",turkishword)
            print("V3 – Past Participle Kelimeleriniz: ",englishword)
            print(" ")        
    dictwords = {
            1:{turkishword[0]:englishword[0]},
            2:{turkishword[1]:englishword[1]},
            3:{turkishword[2]:englishword[2]},
            4:{turkishword[3]:englishword[3]},
            5:{turkishword[4]:englishword[4]},
            6:{turkishword[5]:englishword[5]},
            7:{turkishword[6]:englishword[6]},
            8:{turkishword[7]:englishword[7]},
            9:{turkishword[8]:englishword[8]},
            10:{turkishword[9]:englishword[9]},
            11:{turkishword[10]:englishword[10]},
            12:{turkishword[11]:englishword[11]},
            13:{turkishword[12]:englishword[12]},
            14:{turkishword[13]:englishword[13]},
            15:{turkishword[14]:englishword[14]}
    }
    while True:
        print(" ")
        number = int(random.uniform(1,16))
        # print("number ",number)
        print("^".center(70,"^"))
        answer = input(f''' '{dictwords[number][turkishword[number - 1]]}' kelimesinin ikinci hali nedir:  ''')
        answer.lower().strip()
        if answer != turkishword[number -1]:
            print(f''' '{answer}' doğru cevap değildi.''')
            print("^".center(70,"^"))
            print(" ")
        if answer == turkishword[number -1]:
            print(f'''Tebrikler. '{answer}' doğru cevaptı. ''')
            print("^".center(70,"^"))
            print(" ")
        if answer == "kelime gir":
            break
