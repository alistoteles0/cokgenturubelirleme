print("Çokgeniniz kenar sayısına göre türünü belirtme programı.")
a = int(input("Çokgeniniz kaç kenarlıdır? (3,4): "))
if a == 4:
    kenar1 = float(input("Birinci kenarın uzunluğunu giriniz: "))
    kenar2 = float(input("İkinci kenarın uzunluğunu giriniz: "))
    kenar3 = float(input("Üçüncü kenarın uzunluğunu giriniz: "))
    kenar4 = float(input("Dördüncü kenarın uzunluğunu giriniz: "))
    if kenar1 <= 0:
        print("Lütfen geçerli bir kenar uzunluğu giriniz.")
    elif kenar2 <= 0:
        print("Lütfen geçerli bir kenar uzunluğu giriniz.")
    elif kenar3 <= 0:
        print("Lütfen geçerli bir kenar uzunluğu giriniz.")
    elif kenar4 <= 0:
        print("Lütfen geçerli bir kenar uzunluğu giriniz.")
    else:
        if kenar1 == kenar2:
            if kenar3 == kenar4:
                if kenar1 == kenar3:
                    print("Çokgeniniz kare veya eşkenar dörtgendir.")
            if kenar3 == kenar4:
                if kenar1!=kenar3:
                    print("Çokgeniniz dikdörtgen veya paralelkenardır.")
            if kenar3 != kenar4:
                print("Çokgeniniz çeşitkenar çokgendir.")
        if kenar1 != kenar2:
            if kenar2 == kenar4:
                if kenar1 == kenar3:
                    print("Çokgeniniz dikdörtgen veya paralelkenardır.")
            if kenar2 != kenar4:
                if kenar3 == kenar2:
                    print("Çokgeniniz dikdörtgen veya paralelkenardır.")            
        if kenar1 != kenar2:
            if kenar2==kenar3:
                if kenar1 != kenar4:
                    print("Çokgeniniz çeşitkenar çokgendir.")
            if kenar2 != kenar4:
                if kenar2 != kenar3:
                    print("Çokgeniniz çeşitkenar çokgendir.")
if a == 3:
    k1 = float(input("Birinci kenarın uzunluğunu giriniz: "))
    k2 = float(input("İkinci kenarın uzunluğunu giriniz: "))
    k3 = float(input("Üçüncü kenarın uzunluğunu giriniz: "))
    if k1 <= 0:
        print("Lütfen geçerli bir kenar uzunluğu giriniz.")
    elif k2 <= 0:
        print("Lütfen geçerli bir kenar uzunluğu giriniz.")
    elif k3 <= 0:
        print("Lütfen geçerli bir kenar uzunluğu giriniz.")
    else:
        if k1 <= abs(k2-k3) or k1 > k2+k3:
                print("Girdiğiniz kenar uzunlukları üçgen eşitsizliğine uymuyor.")
        elif k2 <= abs(k3-k1) or k2 > k3+k1:
                print("Girdiğiniz kenar uzunlukları üçgen eşitsizliğine uymuyor.")
        elif k3 <= abs(k1-k2) or k3 > k1+k2:
                print("Girdiğiniz kenar uzunlukları üçgen eşitsizliğine uymuyor.")
        else:
            if k1 == k2:
                if k1 == k3:
                    print("Girdiğiniz üçgen eşkenar üçgendir.")
                if k1 != k3:
                    print("Girdiğiniz üçgen ikizkenar üçgendir.")
            elif k1 == k3:
                if k1 == k2:
                    print("Girdiğiniz üçgen eşkenar üçgendir.")
                if k1 != k2:
                    print("Girdiğiniz üçgen ikizkenar üçgendir.")
            elif k2 == k3:
                if k2 == k1:
                    print("Girdiğiniz üçgen eşkenar üçgendir.")
                if k2 != k1:
                    print("Girdiğiniz üçgen ikizkenar üçgendir.")
            else:
                print("Girdiğiniz üçgen çeşitkenar üçgendir.")
                    
                    
                    
                    
    
           
        
        
    
    