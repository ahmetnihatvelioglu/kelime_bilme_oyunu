import random

# Kelime listesi
kelime_listesi = ['python', 'programlama', 'oyun', 'kitap', 'meyve']

def gizli_kelime_gosterimi(gizli_kelime, tahminler):
    # Gizli kelime gösterimini oluşturur
    return " ".join(c if c in tahminler else "_" for c in gizli_kelime)

def kelime_tahmin_oyunu():
    print("Kelime Tahmin Oyununa Hoş Geldiniz!")
    
    while True:
        # Oyunu başlatmak isteyip istemediğini sor
        oyun_baslat = input("Oyunu başlatmak için 'E' tuşuna basın veya 'Q' tuşuna basarak çıkın: ")
        
        if oyun_baslat.upper() == 'E':
            # Oyunu başlatmak için rastgele bir kelime seçin
            gizli_kelime = random.choice(kelime_listesi)

            # Kullanıcının tahminlerini saklamak için bir liste oluşturun
            tahminler = []

            while True:
                # Gizli kelimeyi göster
                gizli_kelime_goster = gizli_kelime_gosterimi(gizli_kelime, tahminler)
                print("Tahmin edilecek kelime: ", gizli_kelime_goster)

                # Kullanıcıdan tahmin al
                tahmin = input("Bir harf veya kelime tahmini yapın: ").lower()

                if len(tahmin) == 1: # Eğer tek bir harf tahmini yapıldıysa
                    if tahmin in tahminler:
                        print("Bu harfi zaten tahmin ettiniz.")
                    else:
                        tahminler.append(tahmin)
                else: # Eğer bir kelime tahmini yapıldıysa
                    if tahmin == gizli_kelime:
                        print("Tebrikler! Doğru kelimeyi tahmin ettiniz. Kelime:", gizli_kelime)
                        break
                    else:
                        print("Yanlış kelime tahmini.")

                # Doğru kelimeyi tahmin etmiş mi kontrol et
                if gizli_kelime == gizli_kelime_gosterimi(gizli_kelime, tahminler):
                    print("Tebrikler! Doğru kelimeyi tahmin ettiniz. Kelime:", gizli_kelime)
                    break

            devam_oyun = input("Yeni bir oyun başlatmak için 'E' tuşuna basın veya 'Q' tuşuna basarak çıkın: ")
            if devam_oyun.upper() == 'Q':
                print("Oyundan çıktınız. Tekrar bekleriz!")
                break
        else:
            print("Oyundan çıktınız. Tekrar bekleriz!")
            break

kelime_tahmin_oyunu()

        