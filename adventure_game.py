
"""
Oyuncuya birden fazla seçenek sunarak oyunu farklı varyasyonlarda oynanabilir
hale getirmeye çalıştım ve oyuna birden fazla son hazırladım. Amacım oyunun
oynanabilirliğini artırmaktı. Kullanıcının seçimlerine göre oyunun gidişatı
değişiyor. Oyun sonunda kullanıcı başarıyla oyunun bitredebilr ya da oyunu
kaybeder.
"""

"""
oyunun 3 tane sonu var sonlardan birine iki farklı noktadan ulaşma imkanı var
ama kodda bir noktada ipucu vermeyi unutmuşum bu yüzden seçimlerden birinde
oyun devam etmiyor. sağ-1-2-2-2 
"""

import time 

def yavas_yaz(metin): #time modülünden yararlanarak harf harf yazan fonk. 
    for harf in metin:
        print(harf, end='', flush=True)
        time.sleep(0.03)
    print()

#kullanıcının sadece ismin depo eden class
class Karakter: 
    def __init__(self, isim):
        self.isim = isim

#karakter sınıfının kalıtımı. ayrıca ipuçları adında bir liste.
class Oyuncu(Karakter):
    def __init__(self, isim):
        super().__init__(isim)
        self.ipuclar = []
        #list

    def ipucu_ekle(self, ipucu):
        self.ipuclar.append(ipucu)

    def ipuclari_goster(self):
        if not self.ipuclar:
            yavas_yaz("Henüz hiç ipucu toplamadın.")
        else:
            yavas_yaz("\nTopladığın ipuçları:")
            for i, ip in enumerate(self.ipuclar, 1):
                print(f"{i}. {ip}")
                
#Oyunun hikayesinin kullanıcıya anlatıldığı fonksiyon
def giris(oyuncu):
    yavas_yaz(f"{oyuncu.isim}, İpucu adventure game'e hoş geldin.\n")
    yavas_yaz("*********************************************************")
    yavas_yaz("""*  Bembeyaz bir odada gözlerini açıyorsun...                    *
Etrafı inceliyorsun. Gözüne duvarda asılı bir not ilişiyor.  
Notta şöyle diyor: 'Buradan kurtulmak istiyorsan sana verilen görevleri yapmalısın.
Bulunduğun odada bir kapı göreceksin. Bu kapının ardında seni farklı görevler bekliyor.
Her türlü olasılığa hazırlıklı ol'""")
    yavas_yaz("*********************************************************")
    yavas_yaz("\n-Ne ormanı? Görevler mi? Nereye düştüm ben? Umarım bu bir rüyadır.\n\n")

#görevleri depo ettiğim dict
    gorevler = {
        1: "Ormandaki ipuçlarını bul",
        2: "Sana verilen görevleri yerine getir.",
        3: "Çıkış kapısını bul ve oyunu bitir"
    }
    print("İşte görevlerin:", gorevler)
    yavas_yaz("\nArtık hazırsın... Başarılar...\n")

#
def orman_gorevi(oyuncu):
    yavas_yaz("Kapıyı açıyorsun.")
    yavas_yaz("\nOrmana doğru ilerliyorsun...\n")
    patika_koordinatlari = [("sağ", "canavar"), ("sol", "ipucu")]
    
    
    #kullanıcıya ipucu vermek için kullandığım döngü
    for yol, sonuc in patika_koordinatlari:
      print(f"{yol.capitalize()} yolunda seni bekleyen: {sonuc}")

    secim = input("""Ormanın girişinde patika ikiye ayrılıyor. Hangi patikadan 
ilerlemek istersin? (sağ/sol): """).lower()

    if secim == "sağ":
        yavas_yaz("\nSağ patikaya saptın. Sakince yürüyorsun\n")
        yavas_yaz("Garip sesler duyuyorsun... İnsan sesi mi o?\n")
        altsecim = input("""1. Sese doğru git\n2. İpuçlarını bulmaya devam et\nSeçimin: """)

        if altsecim == "1":
            yavas_yaz("\nSese doğru yürüyorsun...")
            yavas_yaz("O da kim? Sana yardım edebilir...")
            yavas_yaz("Yanına gidiyorsun")

            tuzaksecimi = input("""Canavarın tuzağına düştün. Şimdi ne yapacaksın?
1. Kaçmaya çalış\n2. Canavarla dövüş\nSeçimin: """)

            if tuzaksecimi == "1":
                yavas_yaz("Kaçmayı başardın. İpuçlarına odaklan.")
            elif tuzaksecimi == "2":
                yavas_yaz("Canavarla savaştın ve kazandın!")
            else:
                yavas_yaz("Geçerli bir seçim yapmadın. Geri dönüp tekrar denemelisin.")
                orman_gorevi(oyuncu)

        elif altsecim == "2":
            yavas_yaz("Ormanda ilerlerken yerde gizli bir not buluyorsun.")
            yavas_yaz("""Notta yazanlar: 'Ormanda yürürken hep önümde durur, ben adım
atınca o da atar. Ne olabilir?'""")
            yavas_yaz("-Bu bir bilmece olmalı.")
            yavas_yaz("-Cevabı da 'GÖLGE'")
            oyuncu.ipucu_ekle("Gölge")

    elif secim == "sol":
        yavas_yaz("""Pembe çiçekli ağaçların arasında yürüyorsun. Sağında kesilmiş 
bir ağaç kovuğu var. Ağaç kovuğunun üzerinde bir şekil var.\n""")
        yavas_yaz("-Bu bir '*' işareti gibi gözüküyor. İpucu olmalı\n")
        oyuncu.ipucu_ekle("*")
        yavas_yaz("İlerlemeye devam ediyorsun...\n\n")
    else:
        yavas_yaz("Geçerli bir seçim yapmadın. Geri dönüp tekrar denemelisin.")
        orman_gorevi(oyuncu)

#oyuncuya oyunun ilerlemesi için seçim sansı sunduğum fonk
def secim(oyuncu):
    yavas_yaz("Ormanda ilerlemeye devam ediyorsun...\n")
    yavas_yaz("Etrafta kuş sesi ve ağaçtan başka hiçbir şey yok...\n")
    yavas_yaz("-Galiba kayboldum. Nasıl yolumu bulacağım?\n")
    yavas_yaz("Biraz daha ilerledikten sonra yerde bir kutu görüyorsun.")
    yavas_yaz("Kutuyu dikkatlice açıyorsun... Kutunun içinden not çıkıyor.")
    yavas_yaz("-Bir not daha!\n")
    yavas_yaz("""Notta şöyle diyor: Sona neredeyse yaklaştın. Son bir 
görevin kaldı. Sana iki seçenek sunuyorum.

1. seçeneği seçersen olup bitenin nedenini anlamadan odanda uyanacaksın. 
2. seçeneği seçersen neler olup bittiğini öğreneceksin. Karar senin\n""")

    sec = input("Seçimin (1/2): ")
    if sec == "1":
        yavas_yaz("-Bunlar rüya mıydı yoksa gerçek mi?\n\n")
        altsecim = input("Baştan başlamak ister misin? (e/h): ").lower()
        if altsecim == "e":
            oyunu_baslat()
        else:
            print("Oynadığın için teşekkürler.")
            exit()
    elif sec == "2":
        yavas_yaz("Şimdi yapman gereken şey çok basit: Çıkış kapısını bul.")
        yavas_yaz("Bulduğun ipuçlarıyla kapının kilidini aç ve oyunu bitir.\n\n")
    else:
        yavas_yaz("Geçerli bir seçim yapmadın. Geri dönüp tekrar denemelisin.")
        secim(oyuncu)

#oyuncunun oyunu sonlandırabilmesi için tanımladığım fonk
def kapı_sifre(oyuncu):
    yavas_yaz("Kapıdaki not: Kapının şifresini bulursan kurtulacaksın.")
    oyuncu.ipuclari_goster()
    sifre = input("Bulduğun ipuçlarına göre şifreyi gir: ")
    if sifre.lower() in ["gölge", "*"]:
        yavas_yaz("Tebrikler kurtulmayı başardın.")
        yavas_yaz("""Burada olup bitenleri öğrenmeye hak kazandın.\n
Duyduğunda inanamayacaksın ama arkadaşların seni şakaladı. Bu yaşadığın şeylerin
hepsi 1 Nisan şakasıydı ':)'""")
        tekrar = input("Tekrar oynamak ister misin? (e/h): ").lower()
        if tekrar == "e":
            oyunu_baslat()
        else:
            yavas_yaz("Oynadığın için teşekkürler.")
            exit()
    else:
        yavas_yaz("Yanlış şifre. Geri dönüp tekrar denemelisin.")
        kapı_sifre(oyuncu)

def son_gorev(oyuncu):
    yavas_yaz("-Bu da ne demek? Dalga mı geçiyorlar benimle.")
    yavas_yaz("-Ben çıkış kapısını nereden bulacağım koskoca ormanda\n")
    yavas_yaz("-Her şeyin başladığı beyaz odaya dönmeliyim belki gözden bir şeyler kaçırmışımdır.")
    yavas_yaz("-Ya da biraz daha ilerlersem belki kapı karşıma çıkar.")
    sec = input("Seç: 1. Beyaz odaya dön | 2. İlerlemeye devam et : ")

    if sec == "1":
        yavas_yaz("Beyaz odaya döndün ancak kapı kapandı ve hapsoldun.")
        yavas_yaz("OYUNU KAYBETTİN.")
        tekrar = input("Tekrar oynamak ister misin? (e/h): ").lower()
        if tekrar == "e":
            oyunu_baslat()
        else:
            print("Oynadığın için teşekkürler.")
            exit()
    elif sec == "2":
        yavas_yaz("Patika boyunca ilerliyorsun... Kapı karşıda!")
        kapı_sifre(oyuncu)
    else:
        yavas_yaz("Geçerli bir seçim yapmadın. Geri dönüp tekrar denemelisin.")
        son_gorev(oyuncu)
        
#oyunu başlatma fonk
def oyunu_baslat():
    
    while True:
        cevap = input("\nMaceraya hazır mısın? (E/H): ").strip().lower()
        print()
        if cevap == "e":
            isim = input("Karakterinin adı ne olsun? ")
            print()
            oyuncu = Oyuncu(isim)
            break
        else:
            print("Tekrar dene...")
#burada fonksiyonları çağırarak oyunu kullanılabilir hale getirdim
    giris(oyuncu)
    orman_gorevi(oyuncu)
    secim(oyuncu)
    son_gorev(oyuncu)

oyunu_baslat()
