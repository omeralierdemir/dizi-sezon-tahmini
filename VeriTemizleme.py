import numpy as np


def satirTemizle(liste):
    kopru = []
    for i in liste:
        deg = i.replace("\n", "")   # aga tur verileri gürültülü geliyor. gürültüleri temizleyip türleri array haline getirdin

        deg = deg.replace(" ", "")
        deg = deg.split(",")
        kopru.append(deg)


    return kopru


def sezonHesapla(basT,bitT):

    sezonP = []
    sezonDurum = []
    kopru = 0

    for i in range(len(basT)):


        kopru = (int(bitT[i]) - int(basT[i]) + 1)
        sezonP.append(kopru)
        if(kopru==1):


            sezonDurum.append("basarisiz")

        elif(kopru==2):


            sezonDurum.append("basarili")
        else:

            sezonDurum.append("olgun")
    return sezonP,sezonDurum




def tarihBelirleme(tarihList):
    baslangicT = []
    bitisT = []

    bitT = "a"
    for i in tarihList:

        kopru = i.replace("(", "")
        kopru = kopru.replace(")", "")
        kopru = kopru.replace("I","")
        if ("–" in i):

            basT, bitT = kopru.split("–")

            if (bitT == ' ' and 2018 - int(basT) >= 10):

                bitT = str(int(basT) + 2)

            elif (bitT == ' ' and 2018 - int(basT) < 10):

                bitT = str(int(basT) + (2018 - int(basT)))

        else:

            basT, bitT = kopru, kopru

        baslangicT.append(basT)
        bitisT.append(bitT)


    return baslangicT, bitisT


def tur(dizi):
    kopru = []
   # for i in dizi:

    for i in range(len(dizi)):

        a = dizi[i][0]

        kopru.append(a)

    return kopru


def aktorNameCastArray(aktorList):


    sonuc = []
    for i in aktorList:

        if("," in i):

            dizi = i.split(",")

        else:

            dizi = i


        sonuc.append(dizi)

    return sonuc
def aktorPuan(imdbList, oyuncuList):
    aktorUniq = []
    aktorler = []
    count = 0
    sonuc = []

    for i in range(len(oyuncuList)):
        for j in range(len(oyuncuList[i])):

            if (oyuncuList[i][j] not in aktorUniq):

                aktorUniq.append(oyuncuList[i][j])
                aktorler.append([oyuncuList[i][j], 0, 0])
                aktorler[count][1] = float(imdbList[i])
                aktorler[count][2] = 1

                count = count + 1


            else:
                count2 = aktorUniq.index(oyuncuList[i][j])  # başkan ortalama almamışsın
                aktorler[count2][1] = aktorler[count2][1] + float(imdbList[i])
                aktorler[count2][2] = aktorler[count2][2] + 1

    for k in range(len(aktorler)):

        aktorler[k][1] = (aktorler[k][1] / aktorler[k][2])




    return aktorler,aktorUniq

def diziKadroPuan(aktorUniq,oyuncuList,aktorPuan):
 # başkan burada bir dizinin oyuncu kadrosunun puanlarının artimatik ortalamasını alıyorsun. aktorUniq aktorPuan metodunda oluşturduğun dublicate elemean
 #içermeyen aktor listesi, oyuncu listesi bir dizide geçen baş rol oyuncuları, aktor puan ise heterojen yapıdaki ["oyuncu ismi",puan,oynadığı dizi sayısı]
    toplam = 0
    count = 0
    sonuc = []

    for i in range(len(oyuncuList)):
        for j in range(len(oyuncuList[i])):

            if (oyuncuList[i][j]  in aktorUniq):

                index = aktorUniq.index(oyuncuList[i][j])
                toplam = toplam + aktorPuan[index][1]
                count = count + 1
                flag = 1
            else:
                flag = 0

        if(flag == 1):
            ortalama  = toplam / count
            sonuc.append(ortalama)
            count = 0
            toplam = 0
        else:

            sonuc.append(0)
        flag = 0


    return sonuc


def dictionary(turList):
    sonuc = []
    flag = 0
    count = 0
    toplam = 0
    sozluk = {"action": 16, "fantasy": 14, "sci-fi": 12, "drama": 18, "thriller": 16, "mystery": 14, "crime": 15,
              "adventure": 17, "comedy": 16, "romance": 16, "history": 8, "war": 16, "family": 15, "sport": 12,
              "music": 6, "talk-show": 14, "biography": 6, "horror": 10, "reality-tv": 12, "short": 0, "game-show": 12,
              "news": 15, "documentary": 10}


    for i in range(len(turList)):
        for j in range(len(turList[i])):

            if (turList[i][j].lower() in sozluk):

                toplam = int(sozluk[turList[i][j].lower()]) + toplam
                count = count + 1
                flag = 1

        if(flag == 1):

            ortalama = toplam / count
            toplam = 0
            count = 0
            flag = 0

        else:
            ortalama = 5
        sonuc.append(ortalama)


    return sonuc


def castOyuncuKadro(oyuncuKadro): # aga yek stringe düşürüyon burada stringi

    sonuc = []
    for i in oyuncuKadro:



        kopru =  ','.join(str(x) for x in i)
        sonuc.append(kopru)


    return sonuc






def diziKadroPuanForUser(oyuncuList):
    aktorUniq = ['Tekin Akmansoy', 'Leman Çidamli', 'Sevda Aydan', 'Hasim Hekimoglu', 'Emre Karayel', 'Elif Akçam',
                 'Çigdem Akçam', 'Aysegül Güven', 'Mehmet Ali Erbil', 'Sezer Güvenirgil', 'Korhan Abay', 'Handan Adali',
                 'Mehmet Ali Birand', 'Umur Birand', 'Can Dündar', 'Seyyal Taner', 'Perran Kutman', 'Sevket Altug',
                 'Ercan Yazgan', 'Altan Akisik', 'Nevin Akkaya', 'Fahri Aktürk', 'Halit Akçatepe', 'Oya Basar',
                 'Levent Kirca', 'Cüneyt Arkin', 'Ali Demirel', 'Suzan Akay', 'Demet Akbag', 'Caner Alkaya',
                 'Derya Baykal', 'Ece Alton', 'Haluk Bilginer', 'Müsfik Kenter', 'Haluk Kurtoglu', 'Seden Kiziltunç',
                 'Münir Özkul', 'Dogu Erkan', 'Üstün Asutay', 'Metin Akpinar', 'Zeki Alasya', 'Asuman Arsan',
                 'Arzu Atalay', 'Erdal Özyagcilar', 'Ayse Kökçü', 'Köksal Engür', 'Altan Erkekli', 'Güven Hokna',
                 'Alpay Izbirak', 'Arif Akkaya', 'Nevin Aypar', 'Ahmet Açan', 'Recep Acay', 'Hakan Akin',
                 'Bulent Aksoy', 'Dersu Yavuz Altun', 'Aysen Gruda', 'Aykut Oray', 'Selen Büke', 'Mehmet Beyazit',
                 'Metin Bilgin', 'Ilhan Ersoy', 'Esin Karakullukcu', 'Kemal Kuruçay', 'Baris Manço', 'Aydogan Temel',
                 'Murat Disli', 'Ali Zeytinbas', 'Cem Özer', 'Müjdat Gezen', 'Cenk Koray', 'Coskun Sabah',
                 'Jülide Ates', 'Pinar Erbas', 'Ece Üner', 'Umut Açabuga', 'Naz Onel', 'Atilla Sendil', 'Aleyna Uçar',
                 'Kemal Sunal', 'Alev Oraloglu', 'Erol Demiröz', 'Hakan Haksun', 'Erdinç Akbas', 'Hayrettin Aslan',
                 'Türkan Soray', 'Tarik Tarcan', 'Taner Barlas', 'Cem Davran', 'Sümer Tilmaç', 'Jülide Kural',
                 'Sevval Sam', 'Betül Arim', 'Bilge Sen', 'Dinçer Çekmez', 'Özlem Savas', 'Gamze Gözalan',
                 'Ebru Gündes', 'Serpil Tamur', 'Inanc Terzioglu', 'Açelya Akkoyun', 'Mesut Akusta',
                 'Yildiray Sahinler', 'Mine Biçakçi', 'Perihan Savas', 'Cahit Kasikcilar', 'Yüsra Geyik', 'Zuhal Topal',
                 'Binnur Serbetçioglu', 'Müjgan Agrali', 'Erdal Ugurlu', 'Ismail Hakki Akture', 'Coskun Ozturk',
                 'Asena', 'Gulcin Ergul', 'Olgun Simsek', 'Sivga', 'Melek Baykal', 'Selahattin Bel', 'Egemen Erturk',
                 'Tamer Karadagli', 'Fatih Altayli', 'Deniz Arman', 'Buket Aydin', 'Füsun Demirel', 'Nuray Uslu',
                 'Hülya Avsar', 'Tolga Savaci', 'Engin Koç', 'Ebru Simsek', 'Serdar Bordonaci', 'Emrah Demirci',
                 'Hakan Altuntas', 'Isik Aras', 'Ali Kirca', 'Türker Inanoglu', 'Tarik Akan', 'Güneri Civaoglu',
                 'Nilüfer Açikalin', 'Halit Ergenç', 'Selim Nasit', 'Melih Gümüsbiçak', 'Acun Ilicali', 'Kaan Uguralp',
                 'Nilgün Akçaoglu', 'Elçin Avci', 'Ümit Belen', 'Yilmaz Erdogan', 'Suat Sungur', 'Engin Günaydin',
                 'Erol Günaydin', 'Cengiz Küçükayvaz', 'Gül Gölge', 'Ümit Yesin', 'Kerem Alisik', 'Hilal Aslangiray',
                 'Nuray Deveci', 'Ferhan Sensoy', 'Suna Pekuysal', 'Rasim Öztekin', 'Meriç Acemi', 'Hamdi Alkan',
                 'Pinar Altug', 'Ferdi Atuner', 'Rutkay Aziz', 'Kaan Girgin', 'Dilek Turker', 'Yalçin Mentes',
                 'Buket Dereoglu', 'Neslihan Yeldan', 'Suzan Aksoy', 'Derya Alabora', 'Sinan Albayrak',
                 'Kürsat Alniaçik', 'Duygu Ankara', 'Hande Ataizi', 'Nilüfer Aydan', 'Müge Arda', 'Mustafa Arslan',
                 'Sonay Aydin', 'Beyaz', 'Wilma Elles', 'Demet Akalin', 'Deniz Seki', 'Seyfi Dursunoglu',
                 'Burçin Orhon', 'Süheyl Uygur', 'Ahmet Ugurlu', 'Hülya Böceklioglu', 'Münir Canar', 'Muzaffer Guvenc',
                 'Nuri Gökasan', 'Ergin Eren', 'Bersun Gorica', 'Hakan Guven', 'Sezen Aksu', 'Orhan Gencebay',
                 'Zeki Müren', 'Deniz Akkaya', 'Reha Yeprem', 'Erdogan Özeren', 'Gökhan Çelebi', 'M. Sitare Akbas',
                 'Halil Ergün', 'Deniz Gökçer', 'Sevinç Erbulak', 'Mine Çayiroglu', 'Turkan Derya', 'Sanem Çelik',
                 'Ece Uslu', 'Mustafa Alabora', 'Zerrin Arbas', 'Selda Alkor', 'Yasar Alptekin', 'Funda Barin',
                 'Gülben Ergen', 'Atilla Pakdemir', 'Ibrahim Tatlises', 'Göksel Kortay', 'Hakan Gerçek', 'Gökhan Arsoy',
                 'Dogan Aybay', 'Kenan Bal', 'Sibel Can', 'Ebru Cündübeyoglu', 'Burak Sarimola', 'Volkan Severcan',
                 'Ayla Algan', 'Hasibe Eren', 'Ali Erkazan', 'Alisan', 'Tugba Özay', 'Melda Arat Mutlu',
                 'Hakan Elyildirim', 'Sener Sen', 'Nedim Saban', 'Kadir Inanir', 'Ekrem Bora', 'Bahar Akça',
                 'Mürüvet Arik', 'Nejmi Aykar', 'Mehmet Aslantug', 'Iclal Aydin', 'Okan Bayülgen', 'Bulut Aras',
                 'Turgut Arseven', 'Burçin Abdullah', 'Betül Asçioglu', 'Ceyda Ates', 'Istemi Betil', 'Tugrul Arsever',
                 'Suzan Avci', 'Sühan Bardar', 'Burcu Basaran', 'Berna Laçin', 'Bergüzar Korel', 'Evrim Akin',
                 'Yildiz Asyali', 'Nesrin Isçi', 'Alp Korkmaz', 'Yunus Bülbül', 'Merve Erdogan', 'Müge Oruçkaptan',
                 'Memet Ali Alabora', 'Meltem Cumbul', 'Ayten Gökçer', 'Damla Ersubasi', 'Özcan Deniz', 'Haldun Boysan',
                 'Ipek Tuzcuoglu', 'Birgen Engin', 'Nami Esatgil', 'Idil Firat', 'Ciguli', 'Mete Yavasoglu',
                 'Peri Mehtap Çiçek', 'Murat Öncül', 'Tomris Oguzalp', 'Kenan Pars', 'Zehra Alptürk', 'Müjde Ar',
                 'Avni Yalçin', 'Suavi Eren', 'Selçuk Yöntem', 'Çetin Tekindor', 'Yeliz Tozan', 'Pitircik Akerman',
                 'Kerem Kobanbay', 'Münir Akça', 'Görkem Aribol', 'Günes Berberoglu', 'Önder Açikalin',
                 'Aysen Barutçuoglu', 'Sebnem Dönmez', 'Ilker Aksum', 'Nilgün Belgün', 'Tardu Flordun', 'Oya Aydogan',
                 'Ayça Bingöl', 'Volkan Adiyaman', 'Engin Hepileri', 'Erçin Sicakkan', 'Ali Seckiner Alici',
                 'Ramazan Arman', 'Alpay K. Atalan', 'Kerim Afsar', 'Erol Alpsoykan', 'Özlem Argon', 'Kenan Isik',
                 'Murat Yildirim', 'Berrin Arisoy', 'Yalçin Avsar', 'Durul Bazan', 'Zuhal Olcay', 'Ugur Polat',
                 'Emre Kinay', 'Ruhi Sari', 'Asli Altaylar', 'Demet Evgar', 'Haldun Dormen', 'Seray Sever',
                 'Sefik Ates Meric', 'Öykü Serter', 'Enis Arikan', 'Yavuz Arlisu', 'Murat Daltaban', 'Ali Atay',
                 'Nur Bal', 'Sedef Bildik', 'Yasemin Kosal', 'Aylin Arasil', 'Basak Sayan', 'Selin Türkoglu',
                 'Cevdet Aricilar', 'Serhan Arslan', 'Ozan Güven', 'Mümtaz Sevinç', 'Gül Onat', 'Ayse Tolga',
                 'Nadide Sultan', 'Fikret Hakan', 'Nebahat Çehre', 'Hakan Ural', 'Nefise Karatay', 'Suzan Acun',
                 'Murat Ahlatçi', 'Kaya Akarsu', 'Tayfun Eraslan', 'Nurhayat Kavrak', 'Levent Ülgen', 'Mustafa Ugurlu',
                 'Yesim Büber', 'Nihat Ileri', 'Nihan Durukan', 'Armoni Dikim', 'Koray Ergun', 'Can George Fenn',
                 'Ata Demirer', 'Esra Arslan', 'Melih Atalay', 'Mürsit Bag', 'Tülin Ayhan', 'Alev Cinbarci',
                 'Fatih Dogan', 'Baris Aksavas', 'Ferit Aktug', 'Kaan Urgancioglu', 'Serdar Gökhan', 'Tuba Ünsal',
                 'Mehmet Akif Asmaz', 'Nurgül Yesilçay', 'Hakan Boyav', 'Hakan Vanli', 'Yildiz Kenter', 'Can Gürzap',
                 'Basak Köklükaya', 'Burak Sergen', 'Furkan Kizilay', 'Aysecan Tatari', 'Zafer Ergin', 'Selin Dilmen',
                 'Yavuz Bingöl', 'Derya Artemel', 'Ipek Atagün', 'Mansur Ark', 'Belma Canciger', 'Erdem Akakçe',
                 'Sevinç Gürsen Akyildiz', 'Emrah', 'Özlem Conker', 'Mustafa Avkiran', 'Nurseli Idiz', 'Ilker Ayrik',
                 'Emrah Elçiboga', 'Burcak Isiner', 'Salih Kalyon', 'Bülent Polat', 'Feray Darici', 'Mert Firat',
                 'Zafer Gokcek', 'Serhat Mustafa Kiliç', 'Hatice Aslan', 'Aysegül Atik', 'Jale Azakli', 'Arzu Balkan',
                 'Peker Açikalin', 'Esin Eden', 'Doga Bekleriz', 'Gizem Güven', 'Ayda Aksel', 'Mazhar Alanson',
                 'Kartal Balaban', 'Burak Hakki', 'Nesrin Akdag', 'Ebru Akel', 'Nazan Ayas', 'Erol Aydin',
                 'Irem Arslan Aydin', 'Ceren Benderlioglu', 'Ihsan Bilsev', 'Necati Bilgiç', 'Mesut Ceylan',
                 'Bedia Ener', 'Avni Danyal', 'Hüseyin Avni Danyal', 'Süreyya Davulcuoglu', 'Yetkin Dikinciler',
                 'Onur Rüzgar Erkoçlar', 'Ceyda Düvenci', 'Dursun Ali Sarioglu', 'Seda Sayan', 'Celal Belgil',
                 'Asu Emre', 'Ruhsar Gültekin', 'Mehmet Aslan', 'Selim Erdogan', 'Selma Ergeç', 'Demir Demirkan',
                 'Berke Üzrek', 'Özgü Namal', 'Demet Söz', 'Varol Yasaroglu', 'Sencan Güleryüz', 'Tarik Pabuccuoglu',
                 'Iskender Bagcilar', 'Hikmet Bil', 'Oktay Engin', 'Ara Güler', 'Gülse Birsel', 'Sevket Çoruh',
                 'Kerem Atabeyoglu', 'Özge Borak', 'Fikret Kuskan', 'Zeynep Tokus', 'Talat Bulut', 'Rojda Demirer',
                 'Ahu Türkpençe', 'Arsen Gürzap', 'Berdan Mardini', 'Murat Çobangil', 'Serif Bozkurt', 'Timur Acar',
                 'Necati Sasmaz', 'Erdem Ergüney', 'Gürkan Uygun', 'Kenan Imirzalioglu', 'Ugur Yücel', 'Özkan Ugur',
                 'Fatma Girik', 'Mahmut Cevher', 'Gökçe Bahadir', 'Onur Özcan', 'Burak Altay', 'Yusuf Atala',
                 'Elif Ataman', 'Eren Balkan', 'Didem Balçin', 'Fatma Belgen', 'Çetin Akçan', 'Osman Albayrak',
                 'Michele Cedolin', 'Sahap Sayilgan', 'Nevra Serezli', 'Mehmetcan Mincinozlu', 'Emre Altug',
                 'Akasya Asiltürkmen', 'Yagmur Atacan', 'Deniz Adali', 'Zeynel Abidin Aggül', 'Baris Akarsu',
                 'Pelin Akat', 'Sevinç Aktansel', 'Kerem Altaylar', 'Ömür Arpaci', 'Ümit Acar', 'Nehir Erdogan',
                 'Dean Baykan', 'Ihsan Baysal', 'Emre Bozdogan', 'Neslihan Acar', 'Ilayda Akdogan', 'Cem Aktas',
                 'Icmal Aktuna', 'Levent Üzümcü', 'Hale Caneroglu', 'Senay Gürler', 'Berke Hürcan', 'Didem Inselel',
                 'Serdar Kinaci', 'Ahmet Kaynak', 'Ali Ipin', 'Ruhsar Öcal', 'Bekir Aksoy', 'Ilhan Sesen', 'Ülkü Duru',
                 'Esra Akkaya', 'Ezgi Asaroglu', 'Gökçe Akyildiz', 'Damla Cercisoglu', 'Çagla Sikel', 'Hale Akinli',
                 'Civan Canova', 'Laçin Ceylan', 'Burcu Kara', 'Yagmur Ün', 'Tolga Öztürk', 'Devrim Nas', 'Ragip Savas',
                 'Semsi Inkaya', 'Serkan Genç', 'Turhan Kaya', 'Özge Özberk', 'Erdal Cindoruk', 'Yasemen Heper',
                 'Dara Tan', 'Ege Aydan', 'Tugra Kaftancioglu', 'Yildiz Kaplan', 'Murat Serezli', 'Lale Basar',
                 'Damla Basbar', 'Nergis Kumbasar', 'Sezai Altekin', 'Alper Düzen', 'Hakan Yilmaz', 'Aytaç Agirlar',
                 'Aydemir Akbas', 'Necmettin Aktay', 'Eser Bayar', 'Hakverdi Biber', 'Ali Berge', 'Aziz Izzet Biçici',
                 'Bilal Yilmaz', 'Hakan Bilgin', 'Yagmur Kasifoglu', 'Mehtap Bayri', 'Tülay Bekret', 'Binnur Kaya',
                 'Arif Erkin Güzelbeyoglu', 'Cihan Ünal', 'Zerrin Sümer', 'Seçil Buket Akinci', 'Tuna Arman',
                 'Sevval Baspinar', 'Buket Yanmaz', 'Ali Riza Kubilay', 'Seda Fettahoglu', 'Berk Tokay', 'Erhan Abir',
                 'Melda Bekcan', 'Ali Basar', 'Esin Civangil', 'Ugur Kivilcim', 'Süleyman Çobanoglu', 'Sait Genay',
                 'Selçun Sonat', 'Özden Özgürdal', 'Onur Bay', 'Hülya Kalebayir Çelik', 'Melahat Abbasova',
                 'Kivanç Tatlitug', 'Songül Öden', 'Güngör Bayrak', 'Yeliz Sar', 'Özlem Akinözü', 'Aslan Altin',
                 'Bülent Kayabas', 'Okhan Behar', 'Billur Al', 'Cansu Ak', 'Mert Kiliç', 'Yeliz Akkaya', 'Göksel Arsoy',
                 'Isin Karaca', 'Zeynep Cassalini', 'Cemre Özer', 'Ergün Demir', 'Alara Ertürk', 'Beliz Gundogdu',
                 'Erkan Petekkaya', 'Sezin Akbasogullari', 'Ismail Hacioglu', 'Tülin Özen', 'Dolunay Soysert',
                 'Timuçin Esen', 'Özlem Düvencioglu', 'Orhan Aydin', 'Nur Sürer', 'Sinan Tuzcu', 'Tuba Büyüküstün',
                 'Sirin Öten', 'Okan Yalabik', 'Melis Birkan', 'Cem Kiliç', 'Haki Biçici', 'Ragip Gülen',
                 'Damla Sönmez', 'Teoman', 'Umut Tabak', 'Oya Okar', 'Gokhan Seyhan', 'Selin Demiratar',
                 'Gökcan Gökmen', 'Umut Oguz', 'Cemil Büyükdögerli', 'Volkan Cal', 'Sahan Gökbakar', 'Itir Esen',
                 'Asuman Dabak', 'Murat Onuk', 'Ali Düsenkalkar', 'Gökhan Aydinli', 'Furkan Engin', 'Kazim Eryüksel',
                 'Alp Kirsan', 'Çetin Altay', 'Özkan Ayalp', 'Ömer Naci Boz', 'Alay Cihan', 'Reha Muhtar',
                 'Devin Özgür Çinar', 'Melih Görgün', 'Tolga Evren', 'Ugur Çavusoglu', 'Tugba Akar', 'Ozan Akbaba',
                 'Yusuf Akgün', 'Melike Güner', 'Engin Altan Düzyatan', 'Pelinsu Pir', 'Gözde Kansu', 'Saruhan Hünel',
                 'Deniz Barut', 'Berk Balci', 'Seyda Delibasi', 'Cagkan Culha', 'Dicle Alkan', 'Levent Sülün',
                 'Billur Yazgan', 'Aysenur Yazicioglu', 'Beste Bereket', 'Ömer Güney', 'Bahar Yanilmaz', 'Merve Sevi',
                 'Özgür Ozan', 'Özlem Çinar', 'Burçin Terzioglu', 'Erkan Can', 'Deniz Çakir', 'Zeynep Kumral',
                 'Mehmet Çevik', 'Hakan Karahan', 'Selin Sekerci', 'Sinem Kobal', 'Serkan Senalp', 'Hakan Altiner',
                 'Sinan Çaliskanoglu', 'Nedime Agca', 'Yurtsen Fidan', 'Aytekin Cengiz', 'Fatih Altin', 'Cemal Toktas',
                 'Mehmet Akif Alakurt', 'Cansu Dere', 'Celil Nalcakan', 'Cansel Elcin', 'Beren Saat', 'Ugur Aslan',
                 'Sinem Öztufan', 'Cem Kölemenoglu', 'Özlem Yilmaz', 'Ece Bostanci', 'Ipek Erdem', 'Serhat Tutumluer',
                 'Yasemin Öztürk', 'Bülent Keser', 'Burhan Öçal', 'Özlem Tekin', 'Gökhan Tepe', 'Tolgahan Sayisman',
                 'Enes Atis', 'Burcu Biricik', 'Remzi Evren', 'Lemi Filozof', 'Zafer Alpat', 'Arif Piskin',
                 'Cüneyt Arda Pamuk', 'Erkan Avci', 'Deniz Ugur', 'Görkem Arda Keskin', 'Kutsi', 'Yesim Ceren Bozoglu',
                 'Defne Joy Foster', 'Melisa Sözen', 'Seda Çetin', 'Ilhami Adsal', 'Zeynep Akkoca', 'Umut Armagan',
                 'Cengiz Abazoglu', 'Ugurkan Erez', 'Eysan Özhim', 'Hülya Darcan', 'Oktay Kaynarca', 'Hakan Eratik',
                 'Emre Korkmaz', 'Gamze Özçelik', 'Behzat Uygur', 'Alinur Velidedeoglu', 'Cenk Ertaul', 'Burçak Isimer',
                 'Damla Özen', 'Ayca Zeynep Aydin', 'Kevork Türker', 'Fatma Kabasakal', 'Atilla Olgaç', 'Ezo Sunal',
                 'Batur Belirdi', 'Birce Akalay', 'Hüseyin Soysalan', 'Emel Çölgeçen', 'Serkan Altunorak',
                 'Tuncel Kurtiz', 'Sinan Sümer', 'Sönmez Atasoy', 'Fadik Sevin Atasoy', 'Kenan Çoban',
                 'Gülseren Gürtunca', 'Asli Tandogan', 'Alev Gürzap', 'Ferdi Tayfur', 'Serif Sezer', 'Nesrin Cavadzade',
                 'Erhan Ufak', 'Adnan Erdogan', 'Cahit Kayaoglu', 'Taylan Güner', 'Sinem Uslu', 'Bülent Çetinaslan',
                 'Ilker Kizmaz', 'Ferit Kaya', 'Pelin Karahan', 'Cansin Özyosun', 'Selen Seyven', 'Faik Ergin', 'Dogus',
                 'Seda Bakan', 'Burak Özçivit', 'Isil Yücesoy', 'Cihat Tamer', 'Ayça Aysin Turan', 'Tamay Kiliç',
                 'Yasemin Hadivent', 'Ismail Yk', 'Fatos Güçlü', 'Sarp Levendoglu', 'Bülent Sakrak', 'Cüneyt Özen',
                 'Yasemin Balik', 'Sahin Çelik', 'Emin Boztepe', 'Alper Develioglu', 'Gül Arcan', 'Tansu Biçer',
                 'Bahar Senbahar', 'Nejat Isler', 'Mehmet Günsür', 'Ebru Kocaaga', 'Sedef Avci', 'Hasan Küçükçetin',
                 'Necmi Yildirim', 'Merve Bolugur', 'Ipek Yaylacioglu', 'Nihan Büyükagaç', 'Hare Sürel', 'Tolga Futaci',
                 'Vahide Perçin', 'Duygu Yetis', 'Seda Akman', 'Asuman Krause', 'Ahmet Çakar', 'Berk Oktay',
                 'Bülent Alkis', 'Naz Elmas', 'Irmak Ünal', 'Emrecan Eker', 'Hasan Kaçan', 'Koksal Calik',
                 'Gamze Demirbilek', 'Erdinç Dinçer', 'Yalçin Güzelce', 'Hümeyra', 'Pamela Spence', 'Melike Öcalan',
                 'Canan Türker', 'Ayse Melike Çerçi', 'Arzum Onan', 'Berkay Ates', 'Yigit Özsener', 'Filiz Ahmet',
                 'Salih Bademci', 'Recep Özgür Dereli', 'Suzana Akbelge', 'Yelda Reynaud', 'Pamir Pekin',
                 'Zeynep Kiziltan', 'Cemre Kemer', 'Eren Bakici', 'Yasemin Yuruk', 'Azra Akin', 'Mert Öcal',
                 'Baran Ayhan', 'Murat Han', 'Pelin Ermis', 'Irem Altug', 'Oguzhan Yildiz', 'Atilgan Gümüs',
                 'Mehmet Özbek', 'Sema Mumcu', 'Fatih Koyunoglu', 'Ozman Sirgood', 'Keremcem', 'Hatice Sendil',
                 'Kerem Can', 'Nilay Olcay', 'Sezen Aray', 'Sezai Aydin', 'Cengiz Bozkurt', 'Gökhan Özen',
                 'Ipek Tenolcay', 'Korkmaz Polat', 'Selen Öztürk', 'Metin Belgin', 'Ergül Coskun', 'Alpay Aksum',
                 'Erkan Bektas', 'Ozan Çobanoglu', 'Engin Özsayin', 'Sevda Dalgiç', 'Bülent Emin Yarar', 'Fuad Javadov',
                 'Demir Karahan', 'Lilie Lossen', 'Birol Tarkan Yildiz', 'Burcu Günestutar', 'Önder K. Açikbas',
                 'Baris Basar', 'Elif Durdu', 'Mine Tugay', 'Okan Tangücü', 'Ayse Sule Bilgiç', 'Kiraç', 'Umut Temiz',
                 'Erdal Tosun', 'Hamdi Alp', 'Ibrahim Güldogan', 'Mehmet Ergin Balkas', 'Max Bendo', 'Inan Güngören',
                 'Bade Iscil', 'Sibel Kasapoglu', 'Asena Keskinci', 'Ege Tanman', 'Elif Ceren Balikçi', 'Tolga Çevik',
                 'Sarp Bozkurt', 'Firat Parlak', 'Özer Atik', 'Senay Akay', 'Caner Cindoruk', 'Demet Sasmaz',
                 'Gani Savata', 'Tarik Akyildiz', 'Hasan Ataol', 'Mehdi Bespinar', 'Süleyman Demirel', 'Ismail Hakki',
                 'Volga Sorgu', 'Selim Makaroglu', 'Sennur Canpolat', 'Kerem Corogil', 'Ugur Baltepe', 'Belgin Erdogan',
                 'Adem Yavuz Özata', 'Bigkem Melisa Özelçi', 'Gürsan Piri Onurlu', 'Murat Akkoyunlu', 'Berksan',
                 'Engin Alkan', 'Sedef Sahin', 'Isilay Gül', 'Feride Çetin', 'Emel Müftüoglu', 'Sener Kökkaya',
                 'Selim Gülgören', 'Gülden Dudarik', 'Algi Eke', 'Yusuf Ömer Sinav', 'Hande Soral', 'Fulya Zenginer',
                 'Elit Iscan', 'Selin Ilgar', 'Orhan Kilic', 'Mehmet Feim Mehmedof', 'Yasemin Kay Allen',
                 'Ferdi Akarnur', 'Nur Fettahoglu', 'Nese Karaböcek', 'Asli Kökçe', 'Muhittin Paydas',
                 'Mustafa Uzunyilmaz', 'Orhan Eskin', 'Ece Hakim', 'Elif Nur Kerkük', 'Pelin Sönmez', 'Defne Yalniz',
                 'Dogac Yildiz', 'Ece Çesmioglu', 'Zeynep Özkaya', 'Basri Albayrak', 'Ayça Varlier', 'Çelik Bilge',
                 'Nursim Demir', 'Ebru Aykaç', 'Özlem Baskaya', 'Sevil Ustekin', 'Funda Eryigit', 'Sebnem Bozoklu',
                 'Aysegül Akdemir', 'Gülsüm Alkan', 'Gökhan Soylu', 'Sinem Boyacioglu', 'Halim Ercan', 'Hakki Devrim',
                 'Tayfun Duygulu', 'Tan Arcan', 'Zeynep Beserler', 'Nadim Güç', 'Asli Sahin', 'Miray Daner',
                 'Hande Subasi', 'Özhan Carda', 'Sarp Akkaya', 'Aslihan Gürbüz', 'Esref Kolçak', 'Özgürcan Cevik',
                 'Temmuz Gürkan Karaca', 'Güven Kiraç', 'Manolya Asik', 'Öner Ates', 'Murat Bölücek', 'Riza Akin',
                 'Saadet Aksoy', 'Özge Özpirinçci', 'Erdal Besikçioglu', 'Berk Hakman', 'Leyla Lydia Tugutlu',
                 'Nazli Akin', 'Özlem Balci', 'Osman Bayraktutan', 'Tarik Ünlüoglu', 'Ali Sunal', 'Yigit Ari',
                 'Osmantan Erkir', 'Ayça Isildar', 'Anastasia Beloborodova', 'Sebahat Adalar', 'Kamil Adigüzel',
                 'Melek Akarsu', 'Baris Akkoyun', 'Ayberk Atilla', 'Ates Aydiner', 'Meryem Atmaca', 'Iraz Elif Kiraç',
                 'Yagiz Alp Simsek', 'Merve Altinkaya', 'Ercüment Balakoglu', 'Can Aydin', 'Kazim Carman',
                 'Guido Kessler', 'Nursel Ergin', 'Kadir Kandemir', 'Safak Sezer', 'Mahir Günsiray', 'Berfu Öngören',
                 'Burcu Binici', 'Ahmet Kural', 'Ufuk Özkan', 'Firat Tanis', 'Tayanç Ayaydin', 'Gülden Avsaroglu',
                 'Görkem Yeltan', 'Taner Ölmez', 'Serap Aksoy', 'Ipek Bilgin', 'Serdal Genç', 'Murat Ünalmis',
                 'Lale Yavas', 'Ahmet Devran Dayanc', 'Burak Demir', 'Leyla Giraud', 'Gamze Karaman', 'Soydan Soydas',
                 'Kenan Ece', 'Eray Özbal', 'Yilmaz Öztürk', 'Sevil Atasoy', 'Aytaç Arman', 'Korel Cezayirli',
                 'Orhan Biyikli', 'Özlem Tokaslan', 'Öner Erkan', 'Erkan Kolçak Köstendil', 'Çagdas Onur Öztürk',
                 'Vural Yasaroglu', 'Damla Deniz Turgut', 'Yeliz Baslangic', 'Bertan Benli', 'Martin Anthony',
                 'Stewart Copeland', 'Thomas Buesch', 'Michael Constantine', 'Arda Artun Konak', 'Feyyaz Gümüs',
                 'Mert Ögüt', 'Erdogan Gizem', 'Luran Ahmeti', 'Bilgen Akalan', 'Hande Alpaslan', 'Bihter Dinçel',
                 'Ahmet Saraçoglu', 'Serdar Orçin', 'Firat Dogruloglu', 'Burak Aksak', 'Zeynep Aydin', 'Erman Bagri',
                 'Gokhan Yikilkan', 'Hülya Koçyigit', 'Bahadir B. Bingöl', 'Irem Sultan Cengiz', 'Ali Ihsan Varol',
                 'Tomris Incer', 'Günay Karacaoglu', 'Zeynep Tugçe Bayat', 'Dilsad Çelebi', 'Miray Akay',
                 'Serenay Aktas', 'Selin Altay', 'Zafer Algöz', 'Didem Uzel', 'Bülent Inal', 'Tuncer Salman',
                 'Ipek Karapinar', 'Umut Kurt', 'Engin Akyürek', 'Firat Çelik', 'Yildiz Çagri Atiksoy',
                 'Aras Bulut Iynemli', 'Mete Horozoglu', 'Sahin Ergüney', 'Tolga Sala', 'Fatih Artman', 'Inanç Konukçu',
                 'Ahmet Rifat Sungar', 'Helin Melike Çal', 'Gülçin Tunçok', 'Melisa Toros', 'Mert Can Sevimli',
                 'Aron Buniel', 'Seyla Halis', 'Nihan Balyali', 'Erdeniz Kurucan', 'Pinar Ögün', 'Ruzgar Aksoy',
                 'Ali Gult', 'Pinar Kefeli', 'Iain Maynard', 'Taner Uzum', 'Askin Ibik', 'Murat Çelik', 'Nazli Bektas',
                 'Tansel Öngel', 'Nur Erkul', 'Ertan Saban', 'Meral Asiltürk', 'Kadir Dogulu', 'Ümit Erdim',
                 'Aysun Kayaci', 'Bora Karakul', 'Ertugrul Sakar', 'Mehmet Korhan Firat', 'Mutlu Albayram',
                 'Iskender Altin', 'Emre Emin Aravi', 'Esin Varan', 'Asena Tugal', 'Berat Akca', 'Almeda Abazi',
                 'Altay', 'Sibel Arna', 'Selahattin Acar', 'Toygun Ates', 'Sedat Bilenler', 'Zafer Altun',
                 'Çagatay Ulusoy', 'Feyza Civelek', 'Serkan Keskin', 'Osman Sonant', 'Alican Albayrak',
                 'Hilal Altinbilek', 'Nese Arat', 'Deniz Baysal', 'Selim Bayraktar', 'Evrim Dogan', 'Esin Yildiz',
                 'Baris Arduç', 'Barkin Bayoglu', 'Bugra Gülsoy', 'Öykü Karayel', 'Devrim Özder Akin', 'Furkan Andic',
                 'Erdal Bilingen', 'Metin Büktel', 'Gümeç Alpay Aslan', 'Cemal Hünal', 'Meltem Miraloglu', 'Onur Tuna',
                 'Fahriye Evcen Özçivit', 'Serkan Ercan', 'Hayko Cepkin', 'Doruk Cetin', 'Sezai Calli', 'Meric Alural',
                 'Sevki Altunbuken', 'Belçim Bilgin', 'Bahtiyar Engin', 'Beyti Engin', 'Onur Azad Yilmaz',
                 'Recep Aktug', 'Nejdet Erdem', 'Hazal Filiz Küçükköse', 'Alper Kul', 'Irem Sak', 'Refika Birgul',
                 'Murat Cemcir', 'Boglarka Csösz', 'Yunus Emre Kilinc', 'Leyla Okay', 'Dilek Pehlivan',
                 'Arda Tugra Asik', 'Güray Kip', 'Sermin Hürmeriç', 'Elvin Levinler', 'Cengiz Esiyok', 'Esvet Sahin',
                 'Ramazan Dogan', 'Neslihan Atagül', 'Merve Ates', 'Ibrahim Celikkol', 'Berna Koraltürk',
                 'Gözde Mutluer', 'Yunus Günçe', 'Marius Toma', 'Özgür Özaslan', 'Neslihan Maltepe', 'Özcan Varayli',
                 'Özgür Çevik', 'Mesut Yar', 'Zeynep Eronat', 'Aybars Kartal Özson', 'Songül Bayoglu', 'Hasan Say',
                 'Eda Ece', 'Günes Zavrak', 'Halil Babür', 'Sebnem Hassanisoughi', 'Lila Gürmen', 'Berkay Akin',
                 'Ozan Arabaci', 'Seçkin Özdemir', 'Baris Falay', 'Saygin Soysal', 'Eslem Akar', 'Cansu Tosun',
                 'Baris Bagci', 'Hikmet Aktas', 'Sehsuvar Aktas', 'Buse Arslan', 'Egemen Bagis', 'Nilay Tugba Baz',
                 'Melis Caba', 'Dogu Alpan', 'Leyla Göksun', 'Koray Kadiraga', 'Arda Kural', 'Cem Kurtoglu',
                 'Elcin Atamgüc', 'Meryem Akar', 'Öncil Aktarici', 'Fikret Altunhan', 'Vedat Baltaci', 'Müge Boz',
                 'Hadise', 'Murat Boz', 'Nazli Tolga', 'Gülbin Tosun', 'Goksenin Aktas', 'Umut Eskibatman',
                 'Oguz Oztas', 'Gulistan Sarbas', 'Cavit Çetin Güner', 'Sedat Mert', 'Alim Muzaffer',
                 'Mehrnoush Esmaeilpour', 'Selcuk Eisen', 'Levent Güner', 'Zeynep Tuncay', 'Hazal Kaya', 'Tugçe Kazaz',
                 'Furkan Palali', 'Dilara Aksüyek', 'Cumhuriyet Kiper', 'Konca Cilasun', 'Burak Sagyasar',
                 'Ezgi Eyüboglu', 'Övül Avkiran', 'Asli Enver', 'Güven Murat Akpinar', 'Incinur Dasdemir',
                 'Ayfer Dönmez', 'Adnan Sur', 'Yakup Sariyildiz', 'Levent Öktem', 'Sercan Badur', 'Sebnem Sönmez',
                 'Olkan Serdar Yildiz', 'Ivaylo Asparuhov', 'Kristian Kiehling', 'Konstantin Gerginov Timmy',
                 'Riza Kocaoglu', 'Berat Yenilmez', 'Vural Çelik', 'Haktan Pak', 'Gizem Karaca', 'Hakan Yildiz',
                 'Umut Orkun Eskibatman', 'Sabanur Aksoy', 'Selim Yegin', 'Çaglar Çorumlu', 'Alican Yücesoy',
                 'Sermet Yesil', 'Anil Yalçin', 'Görkem Mertsöz', 'Can Basak', 'Sinan Demirer', 'Dilek Güven',
                 'Yildiz Kültür', 'Gunce Mutlu', 'Ozge Ulusoy', 'Tiraje Basaran', 'Edis', 'Seda Telciler',
                 'Kivanç Baran Aslan', 'Rana Cabbar', 'Giannis Chatzigeorgiou', 'Stefanos Damatos', 'Gizem Denizci',
                 'Sükran Ovali', 'Ezgi Mola', 'Seher Devrim Yakut', 'Bora Akkas', 'Lavinia Longhi',
                 'Mehmet Ali Nuroglu', 'Erdal Yildiz', 'Esra Ronabar', 'Murat Arkin', 'Sevcan Yasar', 'Birol Denizci',
                 'Serpil Gül', 'Murat Aydin', 'Halis Bayraktaroglu', 'Mustafa Vuran', 'Alara Keçeci', 'Cihan Simsek',
                 'Turhan Cihan Simsek', 'Merve Hazer', 'Volkan Bora Dilek', 'Inanç Benlioglu', 'Meltem Dag',
                 'Basak Zebil', 'Adnan Koç', 'Nurhak Mine Soz', 'Ceren Hindistan', 'Tuba Dogma', 'Yaprak Durmaz',
                 'Süleyman Karadag', 'Sule Zeybek', 'Pelin Akil', 'Ulas Inan Inaç', 'Koray Erkök', 'Elçin Sangu',
                 'Cande Percem', 'Oguz Oktay', 'Inci Türkay', 'Okan Çabalar', 'Bahar Kerimoglu', 'Ceren Reis',
                 'Cezmi Baskin', 'Mustafa Üstündag', 'Carlos Martín', 'Ali Ersan Duru', 'Çisem Çanci', 'Can Atak',
                 'Zeynep Çamci', 'Asli Bekiroglu', 'Mehmet Atay', 'Yamaç Telli', 'Tim Seyfi', 'Atilla Pekdemir',
                 'Gürkan Kaçar', 'Özgür Emre Yildirim', 'Buket Orhan', 'Erol Gedik', 'Görkem Türkes', 'Kerem Bürsin',
                 'Hande Dogandemir', 'Yagmur Tanrisevsin', 'Ismail Ege Sasmaz', 'Orhan Güner', 'Ersin Korkut',
                 'Taner Tuncay', 'Nermin Koçak', 'Cahit Gök', 'Emir Bozkurt', 'Hakan Kurtas', 'Mehmet Özgür',
                 'Bengü Ergin', 'Nilperi Sahinkaya', 'Kaan Yildirim', 'Cankat Aydos', 'Serenay Sarikaya',
                 'Metin Akdülger', 'Yunus Emre Yildirimer', 'Ahmet Mümtaz Taylan', 'Mehmet Aykaç', 'Mehmet Esen',
                 'Serhan Yavas', 'Tolga Güleç', 'Efsane Odag', 'Didem Soydan', 'Ekin Koç', 'Demet Özdemir',
                 'Murat Balci', 'Emre Yetim', 'Özlem Çakar', 'Begüm Birgören', 'Nehir Büyükakçay', 'Elit Cam',
                 'Yesim Aliç', 'Göktug Alpasar', 'Duygu Sarisin', 'Defne Samyeli', 'Cagri Citanak', 'Cansu Demirci',
                 'Sina Ozer', 'Begüm Akkaya', 'Alihan Araci', 'Gözde Cigaci', 'Gülenay Kalkan', 'Zafer Diper',
                 'Berk Atan', 'Su Kutlu', 'Deger Soysal', 'Yasemin Erkent', 'Alp Akar', 'Evrim Alasya',
                 'Firat Altunmese', 'Ertugrul Aytaç Usun', 'Ayberk Aladar', 'Murat Sencan', 'Ata Atabek',
                 'Alp Guneyman', 'Kaan Gure', 'Yekta Kopan', 'Cem Yilmaz', 'Aylin Engör', 'Efsun Akkurt',
                 'Vildan Atasever', 'Mediha Aydin', 'Ozan Özcan', 'Caner Özyurtlu', 'Bengi Öztürk', 'Devrim Atmaca',
                 'Aysen Batigün', 'Ece Baykal', 'Doga Rutkay', 'Aylin Kontante', 'Erdem Akin', 'Muharrem Bayrak',
                 'Zahide Yetis', 'Ömer Levent Dilli', 'Tayfun Atac', 'Thiago Vlentim', 'Ali Tuna Dilli', 'Asli Ozmel',
                 'Sidal Damar', 'Ahmet Yenilmez', 'Tülay Bursa', 'Keremcan Köse', 'Sükrü Özyildiz', 'Fatih Portakal',
                 'Semra Dinçer', 'Nihan Asici', 'Yigit Mergen', 'Farah Zeynep Abdullah', 'Caglar Ertugrul',
                 'Damla Colbay', 'Faruk Acar', 'Vugar Aliyev', 'Sahin Sahin', 'Beslan Babaoglu', 'Ceren Moray',
                 'Bahar Sahin', 'Biran Damla Yilmaz', 'Sinasi Yurtsever', 'Sermiyan Midyat', 'Tarik Bayrak',
                 'Sinan Divrik', 'Emre Ihlamur', 'Merve Ihlamur', 'Emir Berke Zincidi', 'Baris Yalçin', 'Osman Beyaz',
                 'Aysel Durmus', 'Boran Gökçe', 'Eda Özdemir', 'Esin Gündogdu', 'Çiçek Acar', 'Ipek Bagriacik',
                 'Yusa Bozkurt', 'Gökhan Alkan', 'Aysenil Samlioglu', 'Erman Okay', 'Yesim Salkim', 'Ayse Akin',
                 'Ipek Ozagan', 'Ceren Koç', 'Özge Gürel', 'Serkan Çayoglu', 'Daghan Külegeç', 'Berk Cankat',
                 'Açelya Topaloglu', 'Ebru Özkan', 'Nursel Köse', 'Alina Boz', 'Selen Soyder', 'Yurdaer Okur',
                 'Ismail Demirci', 'Metin Çekmez', 'Almila Ada', 'Anil Altan', 'Bennu Yildirimlar', 'Filiz Kaya',
                 'Gülcan Arslan', 'Nadir Saribacak', 'Cem Korkmaz', 'Cihat Suvarioglu', 'Duygu Yurukce',
                 'Uraz Kaygilaroglu', 'Baran Akbulut', 'Mert Turak', 'Ali Barkin', 'Elvan Disli', 'Ceyhun Tutal',
                 'Ege Sezer', 'Ömer Faruk Biçer', 'Arda Beyaztas', 'Mehmet Duran', 'Atalay Demirci', 'Cengiz Coskun',
                 'Nurettin Sönmez', 'Cem Uçan', 'Kamil Güler', 'Hakan Yufkacigil', 'Erhan Alpay', 'Özgür Avsar',
                 'Elena Viunova', 'Burak Satibol', 'Emre Kivilcim', 'Ekrem Erdinç', 'Ozanay Alpkan', 'Emre Avsar',
                 'Yasar Aydinlioglu', 'Gül Arici', 'Onur Saylak', 'Numan Çakir', 'Ilayda Alisan', 'Ali Karagöz',
                 'Beste Kökdemir', 'Merve Oflaz', 'Basak Demiral', 'Cansu Gultekin', 'Hüseyin Güler', 'Sezgi Sena Akay',
                 'Nesem Akhan', 'Mehmet Küçük', 'Dilara Büyükbayraktar', 'Merve Anlagan', 'Mehmet Baran Erdogan',
                 'Ediz Hun', 'Leyla Kader Ilhan', 'Burak Can', 'Yagiz Kilinc', 'Ali Sürmeli', 'Gün Koper',
                 'Serdar Gökay Akduman', 'Tugçe Aksoylu', 'Meral Avci', 'Murat Ceylan', 'Zafer Mete', 'Necip Memili',
                 'Berk Erçer', 'Gonca Sariyildiz', 'Ilker Kaleli', 'Musa Uzunlar', 'Ali Il', 'Farid Khalifi',
                 'Adem Yilmaz', 'Reha Özcan', 'Samuray Polat Uncumusaoglu', 'Mazlum Kiper', 'Ufuk Bayraktar',
                 'Gökhan Azlag', 'Sadi Celil Cengiz', 'Fulya Ergünes', 'Hakan Sahin', 'Gökhan Atalay',
                 'Payidar Tüfekçioglu', 'Mehmet Çepiç', 'Tulin Yazkan', 'Kubra Suzgun', 'Serkan Tinmaz', 'Mehmet Celik',
                 'Coraline Chapatte', 'Deniz Erayvaz', 'Seren Sirince', 'Hakan Hepcan', 'Marie Hartlieb',
                 'Salih Zafer Kunt', 'Mustafa Devrim Özdinç', 'Can Yaman', 'Nilay Duru', 'Eren Vurdem', 'Yusuf Çim',
                 'Leyla Uner Ermaya', 'Kubilay Penbeklioglu', 'Dilan Çiçek Deniz', 'Büsra Develi', 'Melisa Senolsun',
                 'Gökhan Keser', 'Ruveyda Öksuz', 'Tolga Saritas', 'Burcu Özberk', 'Berrin Seker Civil',
                 'Suleyman Felek', 'Ayça Erturan', 'Sabina Ajrula', 'Hazar Ergüçlü', 'Arif Diren',
                 'Veda Yurtsever Ipek', 'Hakan Bozbey', 'Elif Küçük', 'Alp Pazarli', 'Akif Yardimci', 'Burak Kimyager',
                 'Meryem Sengül', 'Kayra Aleyna Zabçi', 'Tolga Öz', 'Mehdi Adlin', 'Erol Aksoy', 'Cansu Diktas',
                 'Yigit Dikmen', 'Samet Sirmali', 'Ahmet Olgun Sunaer', 'Alperen Duymaz', 'Hakan Dinçkol',
                 'Amine Gulse', 'Safak Pekdemir', 'Tamer Levent', 'Tülin Oral', 'Pelin Cift', 'Emrah Ablak',
                 'Levent Cantek', 'Bülent Üstün', 'Hande Özen', 'Ushan Çakir', 'Gülçin Santircioglu', 'Cengiz Özdemir',
                 'Ozan Sagsöz', 'Eren Hacisalihoglu', 'Alper Saldiran', 'Celile Toyon Uysal', 'Oya Unustasi',
                 'Dogan Akdogan', 'Giray Altinok', 'Özgün Bayraktar', 'Alper Baytekin', 'Merve Aydin',
                 'Turabi Çamkiran', 'Ulas Torun', 'Bengi Idil Uras', 'Ecem Özkaya', 'Seray Gözler', 'Deniz Celiloglu',
                 'Ülkü Hilal Çiftçi', 'Bige Önal', 'Zeynep Elçin', 'Emre Akça', 'Istephan Hakverdi',
                 'Kaan Tüfekçiyasar', 'Gülce Baydar', 'Zeynep Kankonde', 'Zeynep Anacan', 'Elif Cakman', 'Hande Erçel',
                 'Burak Deniz', 'Özcan Tekdemir', 'Merve Çagiran', 'Özge Özder', 'Aslihan Güner', 'Nil Karaibrahimgil',
                 'Öykü Celik', 'Ekin Mert Daymaz', 'Damla Aslanalp', 'Engin Öztürk', 'Ozan Dolunay', 'Meric Aral',
                 'Sumru Yavrucuk', 'Gökçe Özyol', 'Burak Serdar Sanal', 'Hayal Köseoglu', 'Nihal G. Koldas',
                 'Aras Aydin', 'Osman Karakoç', 'Hazal Subasi', 'Erkan Meriç', 'Aykut Igdeli', 'Sezer Avci',
                 'Ipek Ayaz', 'Boran Kuzum', 'Pinar Deniz', 'Beren Gokyildiz', 'Gonca Vuslateri',
                 'Kanbolat Gorkem Arslan', 'Deniz Can Aktas', 'Rabia Arslan', 'Kader Çabuk', 'Hatice Kirik',
                 'Ali Akdal', 'Emir Benderlioglu', 'Serkan Kuru', 'Sezin Bozaci', 'Eva Dedova', 'Doga Zeynep Doguslu',
                 'Tuba Erdem', 'Yeliz Kuvanci', 'Emir Öner', 'Dilara Akin Yazici', 'Emine Erdem', 'Burcu Kiratli',
                 'Beyza Kesebir', 'Kadir Agirçelik', 'Latif Akgedik', 'Faruk Akgören', 'Kenan Acar', 'Cem Aksakal',
                 'Savas Satis', 'Cihangir Ceyhan', 'Özgür Meric', 'Burak Sahin', 'Cemal Elçin Akar', 'Burcu Altin',
                 'Ahmet Selçuk Bay', 'Sebnem Dogruer', 'Basak Parlak', 'Yazmeen Baker', 'Ahmet Dizdaroglu',
                 'Baris Aytac', 'Yesim Gül Aksar', 'Oktay Alkan', 'Ibrahim Aslan', 'Gizem Akdag', 'Yasemin Aydan',
                 'Nesil Dinçelmas', 'Zeyd Gümüstutan', 'Berat Efe Parlar', 'Esat Polat Güler', 'Vicky Kaya',
                 'Gogo Garifallou', 'Vangelis Harisopoulos', 'Osman Alkas', 'Canan Erguder', 'Taha Ulukaya',
                 'Andac Ulukaya', 'Taner Sahin', 'Neslihan Ulusoy', 'Elif Baysal', 'Nevin Efe', 'Gamze Süner Atay',
                 'Alihan Türkdemir', 'Dilan Telkok', 'Baris Kiliç', 'Berrak Tüzünataç', 'Nazan Kesal', 'Sedef Akalin',
                 'Fatih Altinagac', 'Su Burcu Coskun', 'Burç Kümbetlioglu', 'Dogan Bayraktar', 'Nihat Altinkaya',
                 'Burak Sevinç', 'Anil Ilter', 'Hazal Senel', 'Cigdem Atasoyu', 'Ceyda Sener Baykal', 'Aylin Dinc',
                 'Fikret Durak', 'Ibrahim Eren Kilisli', 'Mutlu Ulusoy', 'Dilhan Naz Özgülüs', 'Tuvana Türkay',
                 'Nilay Deniz', 'Burcu Türünz', 'Basar Dogusoy', 'Ceyhun Mergiroglu', 'Ulas Tuna Astepe',
                 'Hayati Akbas', 'Seda Güven', 'Cemre Polat', 'Gürol Salman', 'Melis Tüzüngüç', 'Umit Kantarcilar',
                 'Ahmet Varli', 'Deniz Bolisik', 'Settar Tanriögen', 'Nergis Öztürk', 'Ilkay Akdagli',
                 'Hande Katipoglu', 'Batuhan Aydar', 'Ercan Kesal', 'Burak Sekmen', 'Bahadir Oz', 'Mehmet Arif Bulak',
                 'Beste Yilmazer', 'Akin Akinözü', 'Muhammet Uzuner', 'Feride Hilal Akin', 'Burçin Bildik',
                 'Erkan Sever', 'Seray Kaya', 'Oguzhan Ugur', 'Berk Uçar', 'Turan Oguzhan', 'Ezgi Ünal',
                 'Gözde Mukavelat', 'Emir Çiçek', 'Ahsen Eroglu', 'Müjde Uzman', 'Berkay Dabakoglu', 'Cem Ertunc',
                 'Berke Odaci', 'Ergin Ulunay', 'Serkan Balbal', 'Zeyno Günenç', 'Öykü Güven', 'Gökhan Akgül',
                 'Serhat Buga', 'Mesut Cobanbasi', 'Tuncay Koca', 'Yagmur Özbasmaci Mermer', 'Günes Emir',
                 'Mehmet Gürhan', 'Berna Canbeldek', 'Bilgehan Demir', 'Aycan Demirci', 'Cansu Dagdelen',
                 'Feri Baycu Güler', 'Ayris Alptekin', 'Suna Sancaktar', 'Emre Yesiloz', 'Feyza Özgür',
                 'Mustafa Mesut Baskir', 'Yavuz Selim Osmanoglu', 'Sevda Erginci', 'Gülsün Sare Fil', 'Erdinç Gülener',
                 'Özgü Kaya', 'Ali Meriç', 'Günes Hayat', 'Irem Helvacioglu', 'Ahu Sungur', 'Sarp Apak',
                 'Derya Karadas', 'Derya Kahraman', 'Sultan Köroglu Kiliç', 'Anil Berk Baki', 'Hilmicem Intepe',
                 'Nagihan Karadere', 'Adem Kilicci', 'Ugur Günes', 'Ezgi Senler', 'Özge Akdeniz', 'Kübra Akin',
                 'Emre Ataman', 'Birkan Sokullu', 'Haydar Biçakci', 'Emre Bolat', 'Hasan Ekinci', 'Turgut Eryilmaz',
                 'Rifat Kanpara', 'Ahmet Avni Yilmaz', 'Mahmut Kotan', 'Ahmet Akyol', 'Aleksandra Nikiforova',
                 'Fatih Ürek', 'Ezgi Yildirim', 'Reyhan Yildirim', 'Sevgül Kiroglu', 'Çagla Demir', 'Özlem Türkad',
                 'Naz Sayiner', 'Burak Yörük', 'Selen Uçer', 'Pelin Öztekin', 'Begüm Cana Özgür', 'Mizgin Ay',
                 'Tugçe Akgün', 'Karsu Dönmez', 'Elif Dogan', 'Öznur Serçeler', 'Berkay Veli', 'Sila Özlem Önemli',
                 'Emrah Akduman', 'Sude Dogar', 'Bestemsu Özdemir', 'Alp Navruz', 'Cemre Gümeli', 'Grzegorz Damiecki',
                 'Agnieszka Grochowska', 'Sylwia Juszczak', 'Wojciech Zoladkowicz', 'Ece Sükan', 'Onur Durmaz',
                 'Yagizcan Küçükcan', 'Cemre Kurum', 'Irem Çalhan', 'Serhat Teoman', 'Mehmet Yalçinkaya',
                 'Somer Sivrioglu', 'Hazer Amani', 'Hakan Kanik', 'Tolga Tekin', 'Mert Yazicioglu', 'Esra Bilgic',
                 'Zerrin Tekindor', 'Aybüke Pusat', 'Ibrahim Selim', 'Irem Erten', 'Mert Efe Günaydin', 'Furkan Inanir',
                 'Bartu Küçükçaglayan', 'Müfit Kayacan', 'Cem Zeynel Kiliç', 'Cemre Ebuzziya', 'Melisa Pamuk',
                 'Tugba Çinar', 'Eser Yenenler', 'Kubilay Aka', 'Özgür Ege Nalci', 'Burak Kut', 'Leya Kirsan',
                 'Beril Su Hatirnaz', 'Abdulkerim Tunc']

    aktorPuan = [['Tekin Akmansoy', 6.8, 1], ['Leman Çidamli', 6.8, 1], ['Sevda Aydan', 6.8, 1],
             ['Hasim Hekimoglu', 6.8, 1], ['Emre Karayel', 7.08, 5], ['Elif Akçam', 5.6, 1], ['Çigdem Akçam', 5.6, 1],
             ['Aysegül Güven', 5.6, 1], ['Mehmet Ali Erbil', 3.2249999999999996, 4],
             ['Sezer Güvenirgil', 2.8499999999999996, 2], ['Korhan Abay', 2.9, 2], ['Handan Adali', 2.9, 1],
             ['Mehmet Ali Birand', 7.099999999999999, 3], ['Umur Birand', 8.2, 1], ['Can Dündar', 7.533333333333334, 3],
             ['Seyyal Taner', 7.6, 1], ['Perran Kutman', 6.6, 5], ['Sevket Altug', 8.149999999999999, 2],
             ['Ercan Yazgan', 7.8999999999999995, 2], ['Altan Akisik', 7.5, 1], ['Nevin Akkaya', 7.5, 1],
             ['Fahri Aktürk', 7.5, 1], ['Halit Akçatepe', 7.279999999999999, 5], ['Oya Basar', 7.300000000000001, 2],
             ['Levent Kirca', 5.65, 2], ['Cüneyt Arkin', 5.46, 5], ['Ali Demirel', 8.4, 1],
             ['Suzan Akay', 7.949999999999999, 2], ['Demet Akbag', 6.4625, 8], ['Caner Alkaya', 7.6, 2],
             ['Derya Baykal', 6.199999999999999, 4], ['Ece Alton', 7.5, 1], ['Haluk Bilginer', 6.426666666666667, 15],
             ['Müsfik Kenter', 6.15, 2], ['Haluk Kurtoglu', 7.5, 1], ['Seden Kiziltunç', 6.6, 1],
             ['Münir Özkul', 6.6, 1], ['Dogu Erkan', 6.6, 1], ['Üstün Asutay', 6.6, 1],
             ['Metin Akpinar', 5.916666666666667, 6], ['Zeki Alasya', 4.380000000000001, 10], ['Asuman Arsan', 6.2, 1],
             ['Arzu Atalay', 4.95, 2], ['Erdal Özyagcilar', 6.35, 4], ['Ayse Kökçü', 7.75, 2],
             ['Köksal Engür', 7.424999999999999, 4], ['Altan Erkekli', 7.1, 2], ['Güven Hokna', 6.619999999999999, 5],
             ['Alpay Izbirak', 7.2, 1], ['Arif Akkaya', 4.2, 1], ['Nevin Aypar', 4.2, 1], ['Ahmet Açan', 4.2, 1],
             ['Recep Acay', 7.3, 1], ['Hakan Akin', 6.300000000000001, 4], ['Bulent Aksoy', 7.3, 1],
             ['Dersu Yavuz Altun', 7.4, 2], ['Aysen Gruda', 5.900000000000001, 3], ['Aykut Oray', 7.2, 1],
             ['Selen Büke', 7.2, 1], ['Mehmet Beyazit', 7.2, 1], ['Metin Bilgin', 7.675000000000001, 4],
             ['Ilhan Ersoy', 7.9, 1], ['Esin Karakullukcu', 7.9, 1], ['Kemal Kuruçay', 7.75, 2],
             ['Baris Manço', 5.8, 1], ['Aydogan Temel', 5.8, 1], ['Murat Disli', 5.8, 1], ['Ali Zeytinbas', 5.8, 1],
             ['Cem Özer', 6.35, 2], ['Müjdat Gezen', 6.25, 2], ['Cenk Koray', 6.2, 1], ['Coskun Sabah', 6.2, 1],
             ['Jülide Ates', 6.4, 1], ['Pinar Erbas', 6.4, 1], ['Ece Üner', 6.4, 1], ['Umut Açabuga', 6.0, 1],
             ['Naz Onel', 6.8, 2], ['Atilla Sendil', 6.0, 1], ['Aleyna Uçar', 6.0, 1],
             ['Kemal Sunal', 7.033333333333334, 3], ['Alev Oraloglu', 7.3, 1], ['Erol Demiröz', 7.3, 1],
             ['Hakan Haksun', 7.4, 2], ['Erdinç Akbas', 5.7, 2], ['Hayrettin Aslan', 7.0, 1],
             ['Türkan Soray', 6.199999999999999, 6], ['Tarik Tarcan', 5.7, 2], ['Taner Barlas', 5.05, 2],
             ['Cem Davran', 4.766666666666667, 9], ['Sümer Tilmaç', 8.7, 1], ['Jülide Kural', 8.7, 1],
             ['Sevval Sam', 5.95, 6], ['Betül Arim', 5.85, 4], ['Bilge Sen', 6.0, 1], ['Dinçer Çekmez', 6.7, 1],
             ['Özlem Savas', 6.7, 1], ['Gamze Gözalan', 5.2, 1], ['Ebru Gündes', 5.25, 4], ['Serpil Tamur', 5.2, 1],
             ['Inanc Terzioglu', 5.2, 1], ['Açelya Akkoyun', 5.166666666666667, 6],
             ['Mesut Akusta', 5.800000000000001, 4], ['Yildiray Sahinler', 6.85, 2], ['Mine Biçakçi', 6.5, 2],
             ['Perihan Savas', 7.6000000000000005, 3], ['Cahit Kasikcilar', 8.1, 1], ['Yüsra Geyik', 8.1, 1],
             ['Zuhal Topal', 7.5, 1], ['Binnur Serbetçioglu', 7.5, 1], ['Müjgan Agrali', 7.5, 1],
             ['Erdal Ugurlu', 6.8, 1], ['Ismail Hakki Akture', 6.8, 1], ['Coskun Ozturk', 6.8, 1],
             ['Asena', 5.433333333333334, 3], ['Gulcin Ergul', 5.050000000000001, 2],
             ['Olgun Simsek', 6.466666666666666, 3], ['Sivga', 6.9, 1], ['Melek Baykal', 4.85, 4],
             ['Selahattin Bel', 7.8, 1], ['Egemen Erturk', 7.8, 1], ['Tamer Karadagli', 4.76, 5],
             ['Fatih Altayli', 6.7, 1], ['Deniz Arman', 6.7, 1], ['Buket Aydin', 6.0, 2], ['Füsun Demirel', 6.08, 5],
             ['Nuray Uslu', 7.6, 2], ['Hülya Avsar', 4.119999999999999, 5], ['Tolga Savaci', 4.7, 1],
             ['Engin Koç', 4.7, 1], ['Ebru Simsek', 7.1, 1], ['Serdar Bordonaci', 7.1, 1], ['Emrah Demirci', 7.1, 1],
             ['Hakan Altuntas', 6.56, 5], ['Isik Aras', 6.949999999999999, 2], ['Ali Kirca', 4.5, 1],
             ['Türker Inanoglu', 4.5, 1], ['Tarik Akan', 5.55, 4], ['Güneri Civaoglu', 4.5, 1],
             ['Nilüfer Açikalin', 7.2, 1], ['Halit Ergenç', 5.933333333333334, 6], ['Selim Nasit', 7.2, 1],
             ['Melih Gümüsbiçak', 4.1, 1], ['Acun Ilicali', 4.65, 4], ['Kaan Uguralp', 4.1, 1],
             ['Nilgün Akçaoglu', 5.7, 1], ['Elçin Avci', 5.7, 1], ['Ümit Belen', 5.95, 2], ['Yilmaz Erdogan', 8.4, 1],
             ['Suat Sungur', 8.4, 1], ['Engin Günaydin', 7.75, 2], ['Erol Günaydin', 5.1000000000000005, 3],
             ['Cengiz Küçükayvaz', 6.1, 1], ['Gül Gölge', 6.1, 1], ['Ümit Yesin', 5.05, 2],
             ['Kerem Alisik', 4.859999999999999, 5], ['Hilal Aslangiray', 6.449999999999999, 2],
             ['Nuray Deveci', 5.3, 1], ['Ferhan Sensoy', 6.2, 1], ['Suna Pekuysal', 6.2, 1],
             ['Rasim Öztekin', 6.279999999999999, 5], ['Meriç Acemi', 6.35, 2], ['Hamdi Alkan', 5.95, 2],
             ['Pinar Altug', 4.666666666666667, 6], ['Ferdi Atuner', 5.5, 1], ['Rutkay Aziz', 4.5, 1],
             ['Kaan Girgin', 4.5, 1], ['Dilek Turker', 4.5, 1], ['Yalçin Mentes', 6.033333333333334, 3],
             ['Buket Dereoglu', 6.75, 2], ['Neslihan Yeldan', 5.633333333333333, 3], ['Suzan Aksoy', 6.075, 4],
             ['Derya Alabora', 7.0, 4], ['Sinan Albayrak', 6.2, 5], ['Kürsat Alniaçik', 6.633333333333333, 3],
             ['Duygu Ankara', 4.25, 2], ['Hande Ataizi', 4.27, 10], ['Nilüfer Aydan', 4.633333333333333, 3],
             ['Müge Arda', 5.8, 1], ['Mustafa Arslan', 5.75, 2], ['Sonay Aydin', 5.8, 1], ['Beyaz', 5.95, 4],
             ['Wilma Elles', 7.0, 2], ['Demet Akalin', 5.5, 3], ['Deniz Seki', 7.2, 1], ['Seyfi Dursunoglu', 4.1, 1],
             ['Burçin Orhon', 4.199999999999999, 2], ['Süheyl Uygur', 4.1, 1], ['Ahmet Ugurlu', 7.6, 1],
             ['Hülya Böceklioglu', 7.1, 1], ['Münir Canar', 7.1, 1], ['Muzaffer Guvenc', 7.1, 1],
             ['Nuri Gökasan', 7.1, 1], ['Ergin Eren', 7.5, 1], ['Bersun Gorica', 7.5, 1], ['Hakan Guven', 7.5, 1],
             ['Sezen Aksu', 6.9, 1], ['Orhan Gencebay', 6.9, 1], ['Zeki Müren', 6.9, 1], ['Deniz Akkaya', 3.0, 2],
             ['Reha Yeprem', 3.8, 1], ['Erdogan Özeren', 3.8, 1], ['Gökhan Çelebi', 4.366666666666667, 3],
             ['M. Sitare Akbas', 4.725, 4], ['Halil Ergün', 6.1, 2], ['Deniz Gökçer', 5.74, 5],
             ['Sevinç Erbulak', 5.85, 2], ['Mine Çayiroglu', 6.7, 1], ['Turkan Derya', 6.5, 1],
             ['Sanem Çelik', 5.933333333333334, 3], ['Ece Uslu', 5.574999999999999, 4], ['Mustafa Alabora', 5.65, 2],
             ['Zerrin Arbas', 6.5, 1], ['Selda Alkor', 5.75, 2], ['Yasar Alptekin', 4.6, 2], ['Funda Barin', 3.3, 1],
             ['Gülben Ergen', 4.166666666666667, 3], ['Atilla Pakdemir', 3.3, 1], ['Ibrahim Tatlises', 3.3, 1],
             ['Göksel Kortay', 5.8, 1], ['Hakan Gerçek', 5.733333333333333, 3], ['Gökhan Arsoy', 4.1, 1],
             ['Dogan Aybay', 4.1, 1], ['Kenan Bal', 4.62, 5], ['Sibel Can', 3.5, 3],
             ['Ebru Cündübeyoglu', 5.433333333333333, 3], ['Burak Sarimola', 1.7, 1], ['Volkan Severcan', 4.2, 2],
             ['Ayla Algan', 7.45, 4], ['Hasibe Eren', 5.449999999999999, 2], ['Ali Erkazan', 5.75, 2],
             ['Alisan', 3.025, 4], ['Tugba Özay', 3.3, 1], ['Melda Arat Mutlu', 3.4666666666666663, 3],
             ['Hakan Elyildirim', 3.3, 1], ['Sener Sen', 8.7, 1], ['Nedim Saban', 8.7, 1], ['Kadir Inanir', 4.4, 7],
             ['Ekrem Bora', 4.35, 2], ['Bahar Akça', 6.68, 5], ['Mürüvet Arik', 6.65, 2], ['Nejmi Aykar', 6.95, 2],
             ['Mehmet Aslantug', 6.071428571428571, 7], ['Iclal Aydin', 6.3999999999999995, 3],
             ['Okan Bayülgen', 6.8, 4], ['Bulut Aras', 6.466666666666666, 3], ['Turgut Arseven', 6.2, 1],
             ['Burçin Abdullah', 5.45, 4], ['Betül Asçioglu', 6.4, 1], ['Ceyda Ates', 5.6499999999999995, 6],
             ['Istemi Betil', 5.975, 4], ['Tugrul Arsever', 5.35, 2], ['Suzan Avci', 3.9, 1], ['Sühan Bardar', 3.9, 1],
             ['Burcu Basaran', 3.9, 1], ['Berna Laçin', 4.36, 5], ['Bergüzar Korel', 5.859999999999999, 5],
             ['Evrim Akin', 5.050000000000001, 2], ['Yildiz Asyali', 5.949999999999999, 2], ['Nesrin Isçi', 6.6, 1],
             ['Alp Korkmaz', 6.6, 1], ['Yunus Bülbül', 2.8, 1], ['Merve Erdogan', 2.8, 1], ['Müge Oruçkaptan', 2.8, 1],
             ['Memet Ali Alabora', 5.95, 2], ['Meltem Cumbul', 5.05, 4], ['Ayten Gökçer', 5.733333333333333, 3],
             ['Damla Ersubasi', 6.4, 1], ['Özcan Deniz', 4.959999999999999, 5], ['Haldun Boysan', 4.075, 4],
             ['Ipek Tuzcuoglu', 4.566666666666666, 3], ['Birgen Engin', 7.2, 1], ['Nami Esatgil', 7.800000000000001, 2],
             ['Idil Firat', 6.233333333333333, 3], ['Ciguli', 6.2, 1], ['Mete Yavasoglu', 6.2, 1],
             ['Peri Mehtap Çiçek', 6.2, 1], ['Murat Öncül', 6.2, 1], ['Tomris Oguzalp', 5.6, 1], ['Kenan Pars', 5.6, 1],
             ['Zehra Alptürk', 4.5, 2], ['Müjde Ar', 5.4, 2], ['Avni Yalçin', 5.8, 2], ['Suavi Eren', 5.8, 2],
             ['Selçuk Yöntem', 7.25, 4], ['Çetin Tekindor', 6.4750000000000005, 8], ['Yeliz Tozan', 6.8, 2],
             ['Pitircik Akerman', 4.6, 1], ['Kerem Kobanbay', 4.6, 1], ['Münir Akça', 4.6, 2],
             ['Görkem Aribol', 3.0, 1], ['Günes Berberoglu', 3.0, 1], ['Önder Açikalin', 6.4, 1],
             ['Aysen Barutçuoglu', 6.4, 1], ['Sebnem Dönmez', 6.0, 2], ['Ilker Aksum', 6.172727272727273, 11],
             ['Nilgün Belgün', 4.140000000000001, 5], ['Tardu Flordun', 5.699999999999999, 6], ['Oya Aydogan', 5.6, 2],
             ['Ayça Bingöl', 6.199999999999999, 2], ['Volkan Adiyaman', 5.62, 5], ['Engin Hepileri', 6.925, 4],
             ['Erçin Sicakkan', 8.6, 1], ['Ali Seckiner Alici', 7.5, 1], ['Ramazan Arman', 7.5, 1],
             ['Alpay K. Atalan', 6.3, 4], ['Kerim Afsar', 3.0, 1], ['Erol Alpsoykan', 4.7, 2], ['Özlem Argon', 3.0, 1],
             ['Kenan Isik', 6.333333333333333, 3], ['Murat Yildirim', 7.080000000000001, 5], ['Berrin Arisoy', 6.4, 1],
             ['Yalçin Avsar', 6.4, 1], ['Durul Bazan', 4.666666666666667, 6], ['Zuhal Olcay', 6.633333333333333, 3],
             ['Ugur Polat', 5.720000000000001, 5], ['Emre Kinay', 5.457142857142857, 7],
             ['Ruhi Sari', 6.8999999999999995, 3], ['Asli Altaylar', 5.65, 4], ['Demet Evgar', 7.75, 6],
             ['Haldun Dormen', 6.3, 1], ['Seray Sever', 4.6, 2], ['Sefik Ates Meric', 3.3, 1], ['Öykü Serter', 3.3, 1],
             ['Enis Arikan', 6.166666666666667, 3], ['Yavuz Arlisu', 5.0, 1], ['Murat Daltaban', 5.766666666666667, 3],
             ['Ali Atay', 7.266666666666666, 3], ['Nur Bal', 4.4, 1], ['Sedef Bildik', 4.4, 1],
             ['Yasemin Kosal', 4.2, 1], ['Aylin Arasil', 5.85, 2], ['Basak Sayan', 4.4, 2], ['Selin Türkoglu', 7.5, 1],
             ['Cevdet Aricilar', 7.5, 1], ['Serhan Arslan', 5.8, 2], ['Ozan Güven', 7.449999999999999, 4],
             ['Mümtaz Sevinç', 4.0, 1], ['Gül Onat', 3.75, 2], ['Ayse Tolga', 5.5, 2], ['Nadide Sultan', 4.0, 1],
             ['Fikret Hakan', 5.25, 2], ['Nebahat Çehre', 5.433333333333333, 3], ['Hakan Ural', 5.0, 1],
             ['Nefise Karatay', 6.2, 2], ['Suzan Acun', 3.6, 1], ['Murat Ahlatçi', 3.6, 1], ['Kaya Akarsu', 3.6, 1],
             ['Tayfun Eraslan', 5.2, 1], ['Nurhayat Kavrak', 5.2, 1], ['Levent Ülgen', 4.0, 4],
             ['Mustafa Ugurlu', 6.15, 2], ['Yesim Büber', 6.56, 5], ['Nihat Ileri', 5.8, 1], ['Nihan Durukan', 5.8, 1],
             ['Armoni Dikim', 7.65, 2], ['Koray Ergun', 7.65, 2], ['Can George Fenn', 7.65, 2], ['Ata Demirer', 7.2, 1],
             ['Esra Arslan', 3.4, 1], ['Melih Atalay', 3.4, 1], ['Mürsit Bag', 4.95, 2], ['Tülin Ayhan', 6.5, 1],
             ['Alev Cinbarci', 6.5, 1], ['Fatih Dogan', 6.5, 1], ['Baris Aksavas', 6.2, 2], ['Ferit Aktug', 6.35, 2],
             ['Kaan Urgancioglu', 5.666666666666667, 3], ['Serdar Gökhan', 6.5, 2],
             ['Tuba Ünsal', 5.366666666666667, 3], ['Mehmet Akif Asmaz', 6.1, 1],
             ['Nurgül Yesilçay', 5.1000000000000005, 7], ['Hakan Boyav', 6.3, 4], ['Hakan Vanli', 5.1, 2],
             ['Yildiz Kenter', 6.6, 1], ['Can Gürzap', 6.05, 2], ['Basak Köklükaya', 6.433333333333333, 6],
             ['Burak Sergen', 4.916666666666667, 6], ['Furkan Kizilay', 4.9, 1], ['Aysecan Tatari', 4.9, 1],
             ['Zafer Ergin', 5.85, 2], ['Selin Dilmen', 8.0, 1], ['Yavuz Bingöl', 4.5200000000000005, 5],
             ['Derya Artemel', 4.6, 1], ['Ipek Atagün', 4.6, 1], ['Mansur Ark', 3.6, 1],
             ['Belma Canciger', 3.8499999999999996, 2], ['Erdem Akakçe', 6.866666666666667, 3],
             ['Sevinç Gürsen Akyildiz', 6.733333333333334, 3], ['Emrah', 4.35, 2],
             ['Özlem Conker', 5.324999999999999, 4], ['Mustafa Avkiran', 6.375, 4],
             ['Nurseli Idiz', 5.366666666666667, 3], ['Ilker Ayrik', 5.733333333333333, 6], ['Emrah Elçiboga', 6.0, 1],
             ['Burcak Isiner', 6.0, 1], ['Salih Kalyon', 5.9, 2], ['Bülent Polat', 6.55, 2], ['Feray Darici', 5.8, 1],
             ['Mert Firat', 6.319999999999999, 5], ['Zafer Gokcek', 3.766666666666667, 3],
             ['Serhat Mustafa Kiliç', 6.6000000000000005, 4], ['Hatice Aslan', 4.8, 4], ['Aysegül Atik', 6.8, 2],
             ['Jale Azakli', 6.1, 1], ['Arzu Balkan', 6.1, 1], ['Peker Açikalin', 2.9, 1], ['Esin Eden', 2.9, 1],
             ['Doga Bekleriz', 4.6, 1], ['Gizem Güven', 3.9499999999999997, 2], ['Ayda Aksel', 6.9, 2],
             ['Mazhar Alanson', 6.1, 1], ['Kartal Balaban', 6.1, 1], ['Burak Hakki', 5.05, 4], ['Nesrin Akdag', 6.2, 1],
             ['Ebru Akel', 5.1, 5], ['Nazan Ayas', 5.25, 2], ['Erol Aydin', 4.4, 1], ['Irem Arslan Aydin', 6.4, 1],
             ['Ceren Benderlioglu', 5.225, 4], ['Ihsan Bilsev', 6.4, 1], ['Necati Bilgiç', 4.5, 1],
             ['Mesut Ceylan', 4.5, 1], ['Bedia Ener', 5.05, 2], ['Avni Danyal', 5.4, 1],
             ['Hüseyin Avni Danyal', 6.0, 3], ['Süreyya Davulcuoglu', 5.4, 1],
             ['Yetkin Dikinciler', 6.366666666666667, 3], ['Onur Rüzgar Erkoçlar', 5.5, 1],
             ['Ceyda Düvenci', 4.366666666666666, 3], ['Dursun Ali Sarioglu', 2.3, 1],
             ['Seda Sayan', 2.0999999999999996, 2], ['Celal Belgil', 7.5, 1], ['Asu Emre', 5.8, 2],
             ['Ruhsar Gültekin', 7.0, 2], ['Mehmet Aslan', 5.824999999999999, 4],
             ['Selim Erdogan', 5.933333333333334, 3], ['Selma Ergeç', 6.066666666666667, 3], ['Demir Demirkan', 3.9, 1],
             ['Berke Üzrek', 3.9, 1], ['Özgü Namal', 5.825, 4], ['Demet Söz', 3.9, 1], ['Varol Yasaroglu', 7.4, 1],
             ['Sencan Güleryüz', 6.3, 1], ['Tarik Pabuccuoglu', 5.775, 4], ['Iskender Bagcilar', 6.3, 1],
             ['Hikmet Bil', 7.5, 1], ['Oktay Engin', 7.5, 1], ['Ara Güler', 7.5, 1], ['Gülse Birsel', 7.525, 4],
             ['Sevket Çoruh', 5.6, 2], ['Kerem Atabeyoglu', 6.339999999999999, 5], ['Özge Borak', 6.65, 2],
             ['Fikret Kuskan', 6.933333333333334, 3], ['Zeynep Tokus', 7.5, 1], ['Talat Bulut', 5.06, 5],
             ['Rojda Demirer', 5.3625, 8], ['Ahu Türkpençe', 4.7, 3], ['Arsen Gürzap', 6.766666666666667, 3],
             ['Berdan Mardini', 6.3, 1], ['Murat Çobangil', 5.5, 2], ['Serif Bozkurt', 6.3, 1], ['Timur Acar', 5.35, 2],
             ['Necati Sasmaz', 7.125, 4], ['Erdem Ergüney', 7.2, 1], ['Gürkan Uygun', 6.640000000000001, 5],
             ['Kenan Imirzalioglu', 7.32, 5], ['Ugur Yücel', 7.050000000000001, 4], ['Özkan Ugur', 7.6, 2],
             ['Fatma Girik', 4.800000000000001, 2], ['Mahmut Cevher', 4.7, 1], ['Gökçe Bahadir', 6.7, 4],
             ['Onur Özcan', 6.2, 1], ['Burak Altay', 6.7, 3], ['Yusuf Atala', 6.0, 1], ['Elif Ataman', 6.0, 1],
             ['Eren Balkan', 5.6, 2], ['Didem Balçin', 6.033333333333334, 3], ['Fatma Belgen', 5.7, 1],
             ['Çetin Akçan', 6.0, 1], ['Osman Albayrak', 6.0, 1], ['Michele Cedolin', 3.3, 1],
             ['Sahap Sayilgan', 3.3, 1], ['Nevra Serezli', 4.1, 2], ['Mehmetcan Mincinozlu', 5.1, 2],
             ['Emre Altug', 5.975, 4], ['Akasya Asiltürkmen', 5.066666666666666, 3], ['Yagmur Atacan', 6.25, 2],
             ['Deniz Adali', 6.0, 1], ['Zeynel Abidin Aggül', 6.0, 1], ['Baris Akarsu', 5.5, 3], ['Pelin Akat', 6.0, 1],
             ['Sevinç Aktansel', 3.6, 2], ['Kerem Altaylar', 2.85, 2], ['Ömür Arpaci', 5.15, 6],
             ['Ümit Acar', 4.733333333333333, 6], ['Nehir Erdogan', 4.575, 4], ['Dean Baykan', 6.15, 2],
             ['Ihsan Baysal', 6.5, 1], ['Emre Bozdogan', 6.5, 1], ['Neslihan Acar', 5.800000000000001, 2],
             ['Ilayda Akdogan', 6.9, 2], ['Cem Aktas', 6.4, 1], ['Icmal Aktuna', 5.5, 2], ['Levent Üzümcü', 6.85, 2],
             ['Hale Caneroglu', 7.6, 2], ['Senay Gürler', 7.3, 3], ['Berke Hürcan', 6.9, 1],
             ['Didem Inselel', 5.875, 4], ['Serdar Kinaci', 6.9, 1], ['Ahmet Kaynak', 5.1, 1], ['Ali Ipin', 5.1, 1],
             ['Ruhsar Öcal', 5.1, 1], ['Bekir Aksoy', 3.925, 4], ['Ilhan Sesen', 5.4, 1],
             ['Ülkü Duru', 5.400000000000001, 3], ['Esra Akkaya', 7.0, 1], ['Ezgi Asaroglu', 5.5, 3],
             ['Gökçe Akyildiz', 5.7, 2], ['Damla Cercisoglu', 5.2, 1], ['Çagla Sikel', 2.4, 3], ['Hale Akinli', 6.8, 1],
             ['Civan Canova', 6.8, 1], ['Laçin Ceylan', 6.8, 1], ['Burcu Kara', 5.15, 4], ['Yagmur Ün', 4.9, 1],
             ['Tolga Öztürk', 4.9, 1], ['Devrim Nas', 3.45, 2], ['Ragip Savas', 5.65, 2], ['Semsi Inkaya', 5.3, 2],
             ['Serkan Genç', 7.9, 2], ['Turhan Kaya', 7.2, 2], ['Özge Özberk', 6.1499999999999995, 6],
             ['Erdal Cindoruk', 6.6, 2], ['Yasemen Heper', 6.7, 1], ['Dara Tan', 6.7, 1],
             ['Ege Aydan', 5.733333333333334, 3], ['Tugra Kaftancioglu', 4.0, 1], ['Yildiz Kaplan', 4.0, 1],
             ['Murat Serezli', 5.1, 2], ['Lale Basar', 6.5, 2], ['Damla Basbar', 6.7, 1], ['Nergis Kumbasar', 6.8, 2],
             ['Sezai Altekin', 4.65, 2], ['Alper Düzen', 5.25, 2], ['Hakan Yilmaz', 6.8999999999999995, 3],
             ['Aytaç Agirlar', 5.9, 2], ['Aydemir Akbas', 5.65, 2], ['Necmettin Aktay', 2.9, 1], ['Eser Bayar', 2.9, 1],
             ['Hakverdi Biber', 7.0, 1], ['Ali Berge', 7.0, 1], ['Aziz Izzet Biçici', 7.0, 1],
             ['Bilal Yilmaz', 5.1000000000000005, 6], ['Hakan Bilgin', 3.6, 1], ['Yagmur Kasifoglu', 4.7, 2],
             ['Mehtap Bayri', 5.45, 4], ['Tülay Bekret', 5.0, 1], ['Binnur Kaya', 6.366666666666667, 3],
             ['Arif Erkin Güzelbeyoglu', 7.05, 2], ['Cihan Ünal', 5.166666666666667, 3],
             ['Zerrin Sümer', 5.933333333333334, 3], ['Seçil Buket Akinci', 6.1, 1], ['Tuna Arman', 6.1, 1],
             ['Sevval Baspinar', 6.1, 1], ['Buket Yanmaz', 4.1, 1], ['Ali Riza Kubilay', 4.1, 1],
             ['Seda Fettahoglu', 5.55, 2], ['Berk Tokay', 4.1, 1], ['Erhan Abir', 7.4, 1], ['Melda Bekcan', 7.3, 1],
             ['Ali Basar', 6.166666666666667, 3], ['Esin Civangil', 6.099999999999999, 3], ['Ugur Kivilcim', 7.3, 1],
             ['Süleyman Çobanoglu', 5.0, 1], ['Sait Genay', 5.0, 1], ['Selçun Sonat', 5.0, 1],
             ['Özden Özgürdal', 5.0, 1], ['Onur Bay', 4.5, 1], ['Hülya Kalebayir Çelik', 4.5, 1],
             ['Melahat Abbasova', 5.25, 2], ['Kivanç Tatlitug', 6.942857142857142, 7],
             ['Songül Öden', 5.8999999999999995, 3], ['Güngör Bayrak', 5.8, 1], ['Yeliz Sar', 6.6, 1],
             ['Özlem Akinözü', 5.0, 2], ['Aslan Altin', 6.6, 1], ['Bülent Kayabas', 6.5, 3], ['Okhan Behar', 3.7, 1],
             ['Billur Al', 4.8, 1], ['Cansu Ak', 7.0, 1], ['Mert Kiliç', 5.3, 3],
             ['Yeliz Akkaya', 6.199999999999999, 2], ['Göksel Arsoy', 4.8, 1], ['Isin Karaca', 3.2, 1],
             ['Zeynep Cassalini', 3.2, 1], ['Cemre Özer', 4.9, 1], ['Ergün Demir', 3.5, 1], ['Alara Ertürk', 3.5, 1],
             ['Beliz Gundogdu', 3.5, 1], ['Erkan Petekkaya', 5.62, 5], ['Sezin Akbasogullari', 6.216666666666668, 6],
             ['Ismail Hacioglu', 4.975, 4], ['Tülin Özen', 6.6499999999999995, 2], ['Dolunay Soysert', 6.45, 4],
             ['Timuçin Esen', 6.6000000000000005, 3], ['Özlem Düvencioglu', 6.4, 2], ['Orhan Aydin', 5.2, 2],
             ['Nur Sürer', 6.6, 2], ['Sinan Tuzcu', 6.85, 2], ['Tuba Büyüküstün', 6.5, 6], ['Sirin Öten', 6.7, 1],
             ['Okan Yalabik', 6.800000000000001, 4], ['Melis Birkan', 7.2, 2], ['Cem Kiliç', 5.9, 1],
             ['Haki Biçici', 3.5, 1], ['Ragip Gülen', 4.45, 2], ['Damla Sönmez', 5.833333333333333, 3],
             ['Teoman', 3.5, 1], ['Umut Tabak', 4.725, 4], ['Oya Okar', 3.85, 2], ['Gokhan Seyhan', 4.2, 1],
             ['Selin Demiratar', 6.2, 1], ['Gökcan Gökmen', 6.2, 1], ['Umut Oguz', 4.7, 2],
             ['Cemil Büyükdögerli', 6.949999999999999, 2], ['Volkan Cal', 6.8, 1], ['Sahan Gökbakar', 6.8, 1],
             ['Itir Esen', 5.1, 1], ['Asuman Dabak', 3.7, 2], ['Murat Onuk', 3.1, 1], ['Ali Düsenkalkar', 4.05, 2],
             ['Gökhan Aydinli', 5.7, 1], ['Furkan Engin', 5.7, 1], ['Kazim Eryüksel', 5.7, 1], ['Alp Kirsan', 6.2, 2],
             ['Çetin Altay', 2.4, 1], ['Özkan Ayalp', 4.3, 2], ['Ömer Naci Boz', 2.4, 1], ['Alay Cihan', 2.4, 1],
             ['Reha Muhtar', 2.5, 1], ['Devin Özgür Çinar', 7.2, 1], ['Melih Görgün', 7.2, 1], ['Tolga Evren', 7.2, 1],
             ['Ugur Çavusoglu', 6.666666666666667, 3], ['Tugba Akar', 7.5, 1], ['Ozan Akbaba', 7.3, 2],
             ['Yusuf Akgün', 6.7, 3], ['Melike Güner', 5.074999999999999, 4], ['Engin Altan Düzyatan', 5.5, 6],
             ['Pelinsu Pir', 4.9, 1], ['Gözde Kansu', 6.7, 1], ['Saruhan Hünel', 6.5, 3], ['Deniz Barut', 7.2, 1],
             ['Berk Balci', 5.1, 1], ['Seyda Delibasi', 5.1, 1], ['Cagkan Culha', 4.166666666666667, 3],
             ['Dicle Alkan', 3.3, 1], ['Levent Sülün', 4.3, 2], ['Billur Yazgan', 4.8, 2],
             ['Aysenur Yazicioglu', 5.05, 2], ['Beste Bereket', 4.3, 1], ['Ömer Güney', 5.433333333333334, 3],
             ['Bahar Yanilmaz', 5.5, 1], ['Merve Sevi', 5.433333333333334, 3], ['Özgür Ozan', 3.7, 1],
             ['Özlem Çinar', 3.7, 1], ['Burçin Terzioglu', 6.949999999999999, 4], ['Erkan Can', 7.3, 5],
             ['Deniz Çakir', 5.6, 2], ['Zeynep Kumral', 7.0, 1], ['Mehmet Çevik', 6.0, 2], ['Hakan Karahan', 7.0, 1],
             ['Selin Sekerci', 5.75, 4], ['Sinem Kobal', 4.325, 4], ['Serkan Senalp', 4.3, 3],
             ['Hakan Altiner', 3.0, 2], ['Sinan Çaliskanoglu', 2.05, 2], ['Nedime Agca', 7.3, 1],
             ['Yurtsen Fidan', 1.3, 1], ['Aytekin Cengiz', 2.4, 2], ['Fatih Altin', 1.3, 1], ['Cemal Toktas', 5.0, 2],
             ['Mehmet Akif Alakurt', 5.1000000000000005, 3], ['Cansu Dere', 7.0, 3], ['Celil Nalcakan', 5.0, 2],
             ['Cansel Elcin', 6.1571428571428575, 7], ['Beren Saat', 6.8, 3], ['Ugur Aslan', 3.25, 2],
             ['Sinem Öztufan', 2.9, 1], ['Cem Kölemenoglu', 2.9, 1], ['Özlem Yilmaz', 5.525, 4],
             ['Ece Bostanci', 5.5, 1], ['Ipek Erdem', 5.5, 1], ['Serhat Tutumluer', 5.325, 4],
             ['Yasemin Öztürk', 3.95, 2], ['Bülent Keser', 3.7, 1], ['Burhan Öçal', 5.7, 1], ['Özlem Tekin', 5.6, 2],
             ['Gökhan Tepe', 5.5, 2], ['Tolgahan Sayisman', 4.9, 5], ['Enes Atis', 5.55, 2], ['Burcu Biricik', 5.35, 2],
             ['Remzi Evren', 3.8, 1], ['Lemi Filozof', 3.8, 1], ['Zafer Alpat', 7.6, 1],
             ['Arif Piskin', 6.199999999999999, 2], ['Cüneyt Arda Pamuk', 7.6, 1], ['Erkan Avci', 6.866666666666667, 3],
             ['Deniz Ugur', 4.9750000000000005, 4], ['Görkem Arda Keskin', 4.1, 1], ['Kutsi', 5.066666666666666, 3],
             ['Yesim Ceren Bozoglu', 5.3, 2], ['Defne Joy Foster', 7.95, 2], ['Melisa Sözen', 6.283333333333332, 6],
             ['Seda Çetin', 2.0, 1], ['Ilhami Adsal', 4.666666666666667, 3], ['Zeynep Akkoca', 2.0, 1],
             ['Umut Armagan', 2.0, 1], ['Cengiz Abazoglu', 2.3, 1], ['Ugurkan Erez', 2.3, 1], ['Eysan Özhim', 3.1, 1],
             ['Hülya Darcan', 5.066666666666666, 3], ['Oktay Kaynarca', 5.08, 5], ['Hakan Eratik', 5.45, 2],
             ['Emre Korkmaz', 6.2, 1], ['Gamze Özçelik', 2.4, 1], ['Behzat Uygur', 2.4, 1],
             ['Alinur Velidedeoglu', 2.4, 1], ['Cenk Ertaul', 2.4, 1], ['Burçak Isimer', 6.7, 1],
             ['Damla Özen', 6.7, 1], ['Ayca Zeynep Aydin', 4.65, 2], ['Kevork Türker', 6.7, 1],
             ['Fatma Kabasakal', 2.0, 2], ['Atilla Olgaç', 1.2, 1], ['Ezo Sunal', 3.6, 2],
             ['Batur Belirdi', 5.633333333333333, 3], ['Birce Akalay', 6.15, 8], ['Hüseyin Soysalan', 4.25, 2],
             ['Emel Çölgeçen', 5.633333333333333, 3], ['Serkan Altunorak', 5.633333333333333, 3],
             ['Tuncel Kurtiz', 4.0, 1], ['Sinan Sümer', 5.3, 1], ['Sönmez Atasoy', 6.6, 1],
             ['Fadik Sevin Atasoy', 5.35, 2], ['Kenan Çoban', 6.949999999999999, 2], ['Gülseren Gürtunca', 6.6, 1],
             ['Asli Tandogan', 4.720000000000001, 5], ['Alev Gürzap', 4.55, 2], ['Ferdi Tayfur', 6.0, 2],
             ['Serif Sezer', 5.7, 1], ['Nesrin Cavadzade', 6.3, 6], ['Erhan Ufak', 6.3, 1], ['Adnan Erdogan', 6.3, 1],
             ['Cahit Kayaoglu', 6.3, 1], ['Taylan Güner', 6.5, 1], ['Sinem Uslu', 4.9, 2],
             ['Bülent Çetinaslan', 4.9, 2], ['Ilker Kizmaz', 6.5, 1], ['Ferit Kaya', 5.699999999999999, 2],
             ['Pelin Karahan', 6.05, 2], ['Cansin Özyosun', 4.4, 2], ['Selen Seyven', 5.85, 2], ['Faik Ergin', 5.2, 1],
             ['Dogus', 2.1, 1], ['Seda Bakan', 5.814285714285714, 7], ['Burak Özçivit', 5.659999999999999, 5],
             ['Isil Yücesoy', 5.1, 3], ['Cihat Tamer', 5.5, 1], ['Ayça Aysin Turan', 5.125, 4], ['Tamay Kiliç', 2.6, 1],
             ['Yasemin Hadivent', 2.6, 1], ['Ismail Yk', 5.9, 1], ['Fatos Güçlü', 5.9, 1],
             ['Sarp Levendoglu', 6.0249999999999995, 4], ['Bülent Sakrak', 6.1, 2], ['Cüneyt Özen', 5.8, 1],
             ['Yasemin Balik', 5.8, 1], ['Sahin Çelik', 5.8, 1], ['Emin Boztepe', 5.8, 1], ['Alper Develioglu', 5.8, 1],
             ['Gül Arcan', 2.5, 1], ['Tansu Biçer', 5.45, 2], ['Bahar Senbahar', 2.5, 1], ['Nejat Isler', 7.6, 1],
             ['Mehmet Günsür', 7.85, 2], ['Ebru Kocaaga', 5.0, 1], ['Sedef Avci', 5.88, 5],
             ['Hasan Küçükçetin', 6.1, 1], ['Necmi Yildirim', 6.2, 1], ['Merve Bolugur', 4.7, 2],
             ['Ipek Yaylacioglu', 6.0, 1], ['Nihan Büyükagaç', 6.200000000000001, 4],
             ['Hare Sürel', 6.333333333333333, 3], ['Tolga Futaci', 6.0, 1], ['Vahide Perçin', 5.766666666666667, 3],
             ['Duygu Yetis', 4.05, 2], ['Seda Akman', 5.459999999999999, 5], ['Asuman Krause', 2.8, 1],
             ['Ahmet Çakar', 2.8, 1], ['Berk Oktay', 5.7250000000000005, 4], ['Bülent Alkis', 4.9, 2],
             ['Naz Elmas', 5.6, 2], ['Irmak Ünal', 4.7, 1], ['Emrecan Eker', 4.1, 1], ['Hasan Kaçan', 4.1, 1],
             ['Koksal Calik', 1.2, 1], ['Gamze Demirbilek', 1.2, 1], ['Erdinç Dinçer', 1.2, 1],
             ['Yalçin Güzelce', 1.2, 1], ['Hümeyra', 5.166666666666667, 3], ['Pamela Spence', 5.2, 1],
             ['Melike Öcalan', 5.2, 1], ['Canan Türker', 4.2, 1], ['Ayse Melike Çerçi', 5.300000000000001, 2],
             ['Arzum Onan', 3.5, 1], ['Berkay Ates', 5.166666666666667, 3], ['Yigit Özsener', 5.4, 1],
             ['Filiz Ahmet', 6.75, 2], ['Salih Bademci', 7.225, 4], ['Recep Özgür Dereli', 7.7, 1],
             ['Suzana Akbelge', 7.7, 1], ['Yelda Reynaud', 6.3, 1], ['Pamir Pekin', 5.05, 2],
             ['Zeynep Kiziltan', 6.3, 1], ['Cemre Kemer', 3.2, 1], ['Eren Bakici', 3.2, 1], ['Yasemin Yuruk', 3.2, 1],
             ['Azra Akin', 4.2, 3], ['Mert Öcal', 3.9, 1], ['Baran Ayhan', 3.9, 1], ['Murat Han', 5.533333333333334, 3],
             ['Pelin Ermis', 5.5, 1], ['Irem Altug', 5.4, 2], ['Oguzhan Yildiz', 5.5, 1], ['Atilgan Gümüs', 5.25, 2],
             ['Mehmet Özbek', 3.8, 1], ['Sema Mumcu', 3.8, 1], ['Fatih Koyunoglu', 5.333333333333333, 3],
             ['Ozman Sirgood', 4.3999999999999995, 3], ['Keremcem', 4.733333333333333, 6], ['Hatice Sendil', 3.2, 1],
             ['Kerem Can', 3.2, 1], ['Nilay Olcay', 3.2, 1], ['Sezen Aray', 5.45, 2], ['Sezai Aydin', 3.9, 1],
             ['Cengiz Bozkurt', 7.0, 3], ['Gökhan Özen', 4.7, 1], ['Ipek Tenolcay', 4.4, 2], ['Korkmaz Polat', 4.7, 1],
             ['Selen Öztürk', 6.7, 4], ['Metin Belgin', 4.1, 2], ['Ergül Coskun', 1.9, 1], ['Alpay Aksum', 6.65, 2],
             ['Erkan Bektas', 5.4, 2], ['Ozan Çobanoglu', 4.7, 1], ['Engin Özsayin', 4.9, 2], ['Sevda Dalgiç', 3.3, 1],
             ['Bülent Emin Yarar', 2.95, 2], ['Fuad Javadov', 7.15, 2], ['Demir Karahan', 6.666666666666667, 3],
             ['Lilie Lossen', 7.15, 2], ['Birol Tarkan Yildiz', 7.4, 1], ['Burcu Günestutar', 2.2, 1],
             ['Önder K. Açikbas', 4.333333333333333, 3], ['Baris Basar', 3.15, 2], ['Elif Durdu', 2.2, 1],
             ['Mine Tugay', 5.4, 2], ['Okan Tangücü', 6.7, 1], ['Ayse Sule Bilgiç', 4.9, 2], ['Kiraç', 3.8, 1],
             ['Umut Temiz', 3.8, 1], ['Erdal Tosun', 3.8, 1], ['Hamdi Alp', 6.7, 3], ['Ibrahim Güldogan', 6.5, 1],
             ['Mehmet Ergin Balkas', 2.6, 1], ['Max Bendo', 3.5999999999999996, 2], ['Inan Güngören', 2.6, 1],
             ['Bade Iscil', 5.55, 2], ['Sibel Kasapoglu', 2.9, 1], ['Asena Keskinci', 4.366666666666666, 3],
             ['Ege Tanman', 2.9, 1], ['Elif Ceren Balikçi', 4.266666666666667, 3], ['Tolga Çevik', 7.75, 4],
             ['Sarp Bozkurt', 8.05, 2], ['Firat Parlak', 7.75, 4], ['Özer Atik', 7.75, 4], ['Senay Akay', 1.6, 1],
             ['Caner Cindoruk', 4.78, 5], ['Demet Sasmaz', 1.6, 1], ['Gani Savata', 1.6, 1], ['Tarik Akyildiz', 6.0, 1],
             ['Hasan Ataol', 6.0, 1], ['Mehdi Bespinar', 6.0, 1], ['Süleyman Demirel', 6.0, 1],
             ['Ismail Hakki', 6.333333333333333, 3], ['Volga Sorgu', 5.5, 1], ['Selim Makaroglu', 5.5, 1],
             ['Sennur Canpolat', 7.3, 1], ['Kerem Corogil', 7.3, 1], ['Ugur Baltepe', 1.1, 1],
             ['Belgin Erdogan', 1.1, 1], ['Adem Yavuz Özata', 4.0, 1], ['Bigkem Melisa Özelçi', 6.4, 2],
             ['Gürsan Piri Onurlu', 6.3, 1], ['Murat Akkoyunlu', 5.15, 2], ['Berksan', 3.1, 1], ['Engin Alkan', 2.9, 1],
             ['Sedef Sahin', 2.9, 1], ['Isilay Gül', 2.9, 1], ['Feride Çetin', 5.5, 2], ['Emel Müftüoglu', 5.1, 1],
             ['Sener Kökkaya', 5.1, 1], ['Selim Gülgören', 6.0, 1], ['Gülden Dudarik', 6.0, 1], ['Algi Eke', 5.425, 4],
             ['Yusuf Ömer Sinav', 6.5, 1], ['Hande Soral', 4.75, 2], ['Fulya Zenginer', 3.4, 1], ['Elit Iscan', 3.4, 1],
             ['Selin Ilgar', 3.4, 1], ['Orhan Kilic', 5.4, 1], ['Mehmet Feim Mehmedof', 4.65, 2],
             ['Yasemin Kay Allen', 6.833333333333333, 3], ['Ferdi Akarnur', 4.65, 2],
             ['Nur Fettahoglu', 6.866666666666667, 3], ['Nese Karaböcek', 4.3, 1], ['Asli Kökçe', 4.3, 1],
             ['Muhittin Paydas', 4.3, 1], ['Mustafa Uzunyilmaz', 4.3, 1], ['Orhan Eskin', 6.9, 1],
             ['Ece Hakim', 6.9, 1], ['Elif Nur Kerkük', 6.9, 1], ['Pelin Sönmez', 2.2, 1], ['Defne Yalniz', 5.1, 1],
             ['Dogac Yildiz', 5.1, 1], ['Ece Çesmioglu', 5.1, 1], ['Zeynep Özkaya', 5.1, 1],
             ['Basri Albayrak', 6.133333333333333, 3], ['Ayça Varlier', 6.833333333333333, 3], ['Çelik Bilge', 6.7, 1],
             ['Nursim Demir', 6.0, 1], ['Ebru Aykaç', 6.7, 2], ['Özlem Baskaya', 6.0, 1], ['Sevil Ustekin', 6.3, 1],
             ['Funda Eryigit', 7.8999999999999995, 3], ['Sebnem Bozoklu', 7.4, 2], ['Aysegül Akdemir', 6.4, 1],
             ['Gülsüm Alkan', 6.4, 1], ['Gökhan Soylu', 3.4, 1], ['Sinem Boyacioglu', 5.6, 1], ['Halim Ercan', 5.6, 1],
             ['Hakki Devrim', 7.0, 1], ['Tayfun Duygulu', 7.0, 1], ['Tan Arcan', 4.15, 2], ['Zeynep Beserler', 4.8, 1],
             ['Nadim Güç', 4.8, 1], ['Asli Sahin', 5.6000000000000005, 3], ['Miray Daner', 6.5, 3],
             ['Hande Subasi', 7.85, 2], ['Özhan Carda', 5.5, 1], ['Sarp Akkaya', 6.300000000000001, 4],
             ['Aslihan Gürbüz', 5.825, 4], ['Esref Kolçak', 3.6, 1], ['Özgürcan Cevik', 4.76, 5],
             ['Temmuz Gürkan Karaca', 3.3, 1], ['Güven Kiraç', 6.45, 2], ['Manolya Asik', 6.300000000000001, 2],
             ['Öner Ates', 5.9, 1], ['Murat Bölücek', 5.819999999999999, 5], ['Riza Akin', 6.333333333333333, 3],
             ['Saadet Aksoy', 7.0, 1], ['Özge Özpirinçci', 6.2749999999999995, 4],
             ['Erdal Besikçioglu', 7.519999999999999, 5], ['Berk Hakman', 6.7749999999999995, 4],
             ['Leyla Lydia Tugutlu', 7.0, 3], ['Nazli Akin', 1.5, 1], ['Özlem Balci', 1.65, 2],
             ['Osman Bayraktutan', 1.5, 1], ['Tarik Ünlüoglu', 6.2, 1], ['Ali Sunal', 6.6499999999999995, 4],
             ['Yigit Ari', 6.8, 1], ['Osmantan Erkir', 6.8, 1], ['Ayça Isildar', 6.8, 1],
             ['Anastasia Beloborodova', 4.6, 1], ['Sebahat Adalar', 7.566666666666666, 3], ['Kamil Adigüzel', 6.95, 2],
             ['Melek Akarsu', 7.5, 1], ['Baris Akkoyun', 6.75, 2], ['Ayberk Atilla', 7.0, 1], ['Ates Aydiner', 7.0, 1],
             ['Meryem Atmaca', 6.0, 1], ['Iraz Elif Kiraç', 6.0, 1], ['Yagiz Alp Simsek', 6.0, 1],
             ['Merve Altinkaya', 4.9, 1], ['Ercüment Balakoglu', 4.9, 1], ['Can Aydin', 5.7, 1],
             ['Kazim Carman', 5.7, 1], ['Guido Kessler', 5.7, 1], ['Nursel Ergin', 4.1, 1], ['Kadir Kandemir', 4.1, 1],
             ['Safak Sezer', 3.8333333333333335, 3], ['Mahir Günsiray', 5.266666666666667, 3],
             ['Berfu Öngören', 5.8, 1], ['Burcu Binici', 4.7, 3], ['Ahmet Kural', 7.633333333333333, 3],
             ['Ufuk Özkan', 5.14, 5], ['Firat Tanis', 7.1, 1], ['Tayanç Ayaydin', 6.199999999999999, 2],
             ['Gülden Avsaroglu', 5.35, 2], ['Görkem Yeltan', 5.3, 1], ['Taner Ölmez', 5.6, 2], ['Serap Aksoy', 4.8, 1],
             ['Ipek Bilgin', 7.8, 2], ['Serdal Genç', 6.6, 1], ['Murat Ünalmis', 5.533333333333332, 3],
             ['Lale Yavas', 6.6, 1], ['Ahmet Devran Dayanc', 6.1, 1], ['Burak Demir', 5.36, 5],
             ['Leyla Giraud', 5.2, 2], ['Gamze Karaman', 3.5, 1], ['Soydan Soydas', 3.5, 1],
             ['Kenan Ece', 5.449999999999999, 4], ['Eray Özbal', 4.3, 1], ['Yilmaz Öztürk', 4.3, 1],
             ['Sevil Atasoy', 6.6, 1], ['Aytaç Arman', 3.9, 1], ['Korel Cezayirli', 5.7, 2], ['Orhan Biyikli', 6.5, 2],
             ['Özlem Tokaslan', 5.0, 2], ['Öner Erkan', 6.666666666666667, 3],
             ['Erkan Kolçak Köstendil', 7.233333333333334, 3], ['Çagdas Onur Öztürk', 7.0, 1],
             ['Vural Yasaroglu', 6.7, 1], ['Damla Deniz Turgut', 3.5, 1], ['Yeliz Baslangic', 3.5, 1],
             ['Bertan Benli', 6.6, 1], ['Martin Anthony', 6.9, 1], ['Stewart Copeland', 6.9, 1],
             ['Thomas Buesch', 6.9, 1], ['Michael Constantine', 6.9, 1], ['Arda Artun Konak', 2.25, 2],
             ['Feyyaz Gümüs', 2.3, 1], ['Mert Ögüt', 4.5, 2], ['Erdogan Gizem', 4.699999999999999, 2],
             ['Luran Ahmeti', 6.4, 1], ['Bilgen Akalan', 6.4, 1], ['Hande Alpaslan', 6.4, 1],
             ['Bihter Dinçel', 5.733333333333333, 3], ['Ahmet Saraçoglu', 6.633333333333334, 3],
             ['Serdar Orçin', 7.2, 1], ['Firat Dogruloglu', 7.2, 1], ['Burak Aksak', 7.5, 1], ['Zeynep Aydin', 7.5, 1],
             ['Erman Bagri', 7.5, 1], ['Gokhan Yikilkan', 7.8, 1], ['Hülya Koçyigit', 4.9, 1],
             ['Bahadir B. Bingöl', 4.8, 1], ['Irem Sultan Cengiz', 4.8, 1], ['Ali Ihsan Varol', 7.4, 1],
             ['Tomris Incer', 5.9, 1], ['Günay Karacaoglu', 6.35, 2], ['Zeynep Tugçe Bayat', 6.75, 2],
             ['Dilsad Çelebi', 6.1, 2], ['Miray Akay', 5.65, 2], ['Serenay Aktas', 5.325, 4],
             ['Selin Altay', 4.766666666666667, 3], ['Zafer Algöz', 6.033333333333334, 6], ['Didem Uzel', 4.3, 1],
             ['Bülent Inal', 5.625, 4], ['Tuncer Salman', 4.3, 1], ['Ipek Karapinar', 4.45, 2], ['Umut Kurt', 6.9, 1],
             ['Engin Akyürek', 6.466666666666666, 3], ['Firat Çelik', 5.966666666666666, 3],
             ['Yildiz Çagri Atiksoy', 7.166666666666667, 3], ['Aras Bulut Iynemli', 6.95, 4],
             ['Mete Horozoglu', 4.95, 4], ['Sahin Ergüney', 3.6, 1], ['Tolga Sala', 3.6, 1], ['Fatih Artman', 7.55, 2],
             ['Inanç Konukçu', 7.6499999999999995, 2], ['Ahmet Rifat Sungar', 5.5, 1], ['Helin Melike Çal', 5.5, 1],
             ['Gülçin Tunçok', 4.25, 2], ['Melisa Toros', 5.6, 1], ['Mert Can Sevimli', 6.5, 2],
             ['Aron Buniel', 5.6, 1], ['Seyla Halis', 5.6, 1], ['Nihan Balyali', 5.46, 5], ['Erdeniz Kurucan', 6.1, 1],
             ['Pinar Ögün', 5.3, 1], ['Ruzgar Aksoy', 6.125, 4], ['Ali Gult', 7.1, 1], ['Pinar Kefeli', 7.1, 1],
             ['Iain Maynard', 7.1, 1], ['Taner Uzum', 7.1, 1], ['Askin Ibik', 7.1, 1], ['Murat Çelik', 7.1, 1],
             ['Nazli Bektas', 7.1, 1], ['Tansel Öngel', 7.199999999999999, 2], ['Nur Erkul', 7.3, 1],
             ['Ertan Saban', 7.3, 1], ['Meral Asiltürk', 7.1, 1], ['Kadir Dogulu', 5.459999999999999, 5],
             ['Ümit Erdim', 5.6, 1], ['Aysun Kayaci', 5.6, 1], ['Bora Karakul', 5.6, 1], ['Ertugrul Sakar', 5.6, 1],
             ['Mehmet Korhan Firat', 5.6, 1], ['Mutlu Albayram', 6.4, 1], ['Iskender Altin', 6.4, 1],
             ['Emre Emin Aravi', 6.4, 1], ['Esin Varan', 2.6, 1], ['Asena Tugal', 2.6, 1], ['Berat Akca', 2.6, 1],
             ['Almeda Abazi', 5.1000000000000005, 3], ['Altay', 4.5, 1], ['Sibel Arna', 4.5, 1],
             ['Selahattin Acar', 6.4, 1], ['Toygun Ates', 6.4, 1], ['Sedat Bilenler', 6.4, 1],
             ['Zafer Altun', 7.949999999999999, 2], ['Çagatay Ulusoy', 6.825, 4], ['Feyza Civelek', 5.4, 1],
             ['Serkan Keskin', 8.6, 3], ['Osman Sonant', 8.6, 3], ['Alican Albayrak', 6.5, 1],
             ['Hilal Altinbilek', 5.725, 4], ['Nese Arat', 6.5, 1], ['Deniz Baysal', 6.55, 6],
             ['Selim Bayraktar', 6.35, 2], ['Evrim Dogan', 3.5, 1], ['Esin Yildiz', 3.5, 1], ['Baris Arduç', 5.15, 2],
             ['Barkin Bayoglu', 7.7, 1], ['Bugra Gülsoy', 7.65, 4], ['Öykü Karayel', 7.133333333333333, 3],
             ['Devrim Özder Akin', 4.9, 1], ['Furkan Andic', 5.525, 4], ['Erdal Bilingen', 4.9, 1],
             ['Metin Büktel', 4.9, 1], ['Gümeç Alpay Aslan', 6.1000000000000005, 3], ['Cemal Hünal', 5.9, 1],
             ['Meltem Miraloglu', 4.75, 2], ['Onur Tuna', 5.449999999999999, 2],
             ['Fahriye Evcen Özçivit', 6.6000000000000005, 3], ['Serkan Ercan', 5.5, 1],
             ['Hayko Cepkin', 6.7749999999999995, 4], ['Doruk Cetin', 5.3, 1], ['Sezai Calli', 5.3, 1],
             ['Meric Alural', 6.5, 2], ['Sevki Altunbuken', 5.3, 1], ['Belçim Bilgin', 5.3, 1],
             ['Bahtiyar Engin', 3.9, 2], ['Beyti Engin', 5.3, 1], ['Onur Azad Yilmaz', 6.2, 1], ['Recep Aktug', 6.2, 1],
             ['Nejdet Erdem', 2.2, 1], ['Hazal Filiz Küçükköse', 5.233333333333333, 3],
             ['Alper Kul', 7.066666666666666, 3], ['Irem Sak', 7.25, 2], ['Refika Birgul', 7.4, 1],
             ['Murat Cemcir', 7.5249999999999995, 4], ['Boglarka Csösz', 7.5, 1], ['Yunus Emre Kilinc', 7.5, 1],
             ['Leyla Okay', 7.5, 1], ['Dilek Pehlivan', 7.5, 1], ['Arda Tugra Asik', 6.3, 1], ['Güray Kip', 6.3, 1],
             ['Sermin Hürmeriç', 6.3, 1], ['Elvin Levinler', 3.8499999999999996, 2], ['Cengiz Esiyok', 4.1, 1],
             ['Esvet Sahin', 4.1, 1], ['Ramazan Dogan', 4.1, 1], ['Neslihan Atagül', 5.8, 3], ['Merve Ates', 5.65, 2],
             ['Ibrahim Celikkol', 6.82, 5], ['Berna Koraltürk', 5.5, 1], ['Gözde Mutluer', 5.666666666666667, 6],
             ['Yunus Günçe', 6.1, 2], ['Marius Toma', 6.7, 1], ['Özgür Özaslan', 6.7, 1], ['Neslihan Maltepe', 4.3, 1],
             ['Özcan Varayli', 5.9, 2], ['Özgür Çevik', 7.5, 1], ['Mesut Yar', 6.6, 1], ['Zeynep Eronat', 6.6, 1],
             ['Aybars Kartal Özson', 6.6, 2], ['Songül Bayoglu', 6.7, 1], ['Hasan Say', 6.7, 1], ['Eda Ece', 4.0, 2],
             ['Günes Zavrak', 2.5, 1], ['Halil Babür', 2.5, 1], ['Sebnem Hassanisoughi', 5.3999999999999995, 3],
             ['Lila Gürmen', 5.15, 2], ['Berkay Akin', 7.2, 1], ['Ozan Arabaci', 7.2, 1],
             ['Seçkin Özdemir', 6.942857142857143, 7], ['Baris Falay', 6.75, 2], ['Saygin Soysal', 7.65, 2],
             ['Eslem Akar', 6.05, 2], ['Cansu Tosun', 7.15, 2], ['Baris Bagci', 7.1, 2], ['Hikmet Aktas', 7.0, 1],
             ['Sehsuvar Aktas', 7.0, 1], ['Buse Arslan', 5.666666666666667, 3], ['Egemen Bagis', 7.0, 1],
             ['Nilay Tugba Baz', 5.3, 1], ['Melis Caba', 5.3, 1], ['Dogu Alpan', 6.6, 1], ['Leyla Göksun', 5.9, 1],
             ['Koray Kadiraga', 5.9, 1], ['Arda Kural', 5.9, 1], ['Cem Kurtoglu', 4.35, 2], ['Elcin Atamgüc', 4.1, 1],
             ['Meryem Akar', 5.8, 1], ['Öncil Aktarici', 5.8, 1], ['Fikret Altunhan', 5.8, 1],
             ['Vedat Baltaci', 6.7, 1], ['Müge Boz', 6.35, 2], ['Hadise', 6.4, 1], ['Murat Boz', 6.4, 1],
             ['Nazli Tolga', 8.2, 1], ['Gülbin Tosun', 8.2, 1], ['Goksenin Aktas', 5.4, 2], ['Umut Eskibatman', 3.6, 1],
             ['Oguz Oztas', 5.4, 2], ['Gulistan Sarbas', 3.6, 1], ['Cavit Çetin Güner', 4.6, 1], ['Sedat Mert', 4.6, 1],
             ['Alim Muzaffer', 4.6, 1], ['Mehrnoush Esmaeilpour', 7.3, 1], ['Selcuk Eisen', 7.3, 1],
             ['Levent Güner', 7.5, 1], ['Zeynep Tuncay', 7.5, 1], ['Hazal Kaya', 5.525, 4], ['Tugçe Kazaz', 5.9, 1],
             ['Furkan Palali', 5.266666666666667, 3], ['Dilara Aksüyek', 5.65, 2], ['Cumhuriyet Kiper', 6.5, 1],
             ['Konca Cilasun', 6.0, 1], ['Burak Sagyasar', 6.0, 1], ['Ezgi Eyüboglu', 5.525, 4],
             ['Övül Avkiran', 6.0, 1], ['Asli Enver', 7.0600000000000005, 5], ['Güven Murat Akpinar', 8.3, 1],
             ['Incinur Dasdemir', 5.6, 1], ['Ayfer Dönmez', 4.9, 2], ['Adnan Sur', 8.5, 1],
             ['Yakup Sariyildiz', 8.5, 1], ['Levent Öktem', 5.3, 1], ['Sercan Badur', 5.6, 2],
             ['Sebnem Sönmez', 6.3, 1], ['Olkan Serdar Yildiz', 6.3, 1], ['Ivaylo Asparuhov', 5.0, 1],
             ['Kristian Kiehling', 5.0, 1], ['Konstantin Gerginov Timmy', 5.0, 1], ['Riza Kocaoglu', 7.4, 1],
             ['Berat Yenilmez', 7.6, 2], ['Vural Çelik', 7.0, 1], ['Haktan Pak', 4.3, 1],
             ['Gizem Karaca', 6.033333333333334, 3], ['Hakan Yildiz', 7.2, 1], ['Umut Orkun Eskibatman', 7.2, 1],
             ['Sabanur Aksoy', 5.0, 1], ['Selim Yegin', 5.0, 1], ['Çaglar Çorumlu', 6.0, 2],
             ['Alican Yücesoy', 6.74, 5], ['Sermet Yesil', 7.9, 1], ['Anil Yalçin', 4.2, 1], ['Görkem Mertsöz', 4.2, 1],
             ['Can Basak', 7.3, 1], ['Sinan Demirer', 7.3, 1], ['Dilek Güven', 7.3, 1], ['Yildiz Kültür', 5.7, 1],
             ['Gunce Mutlu', 2.2, 1], ['Ozge Ulusoy', 2.2, 1], ['Tiraje Basaran', 4.8, 1], ['Edis', 4.8, 1],
             ['Seda Telciler', 4.2, 1], ['Kivanç Baran Aslan', 4.2, 1], ['Rana Cabbar', 4.4, 1],
             ['Giannis Chatzigeorgiou', 4.4, 1], ['Stefanos Damatos', 4.4, 1], ['Gizem Denizci', 4.4, 1],
             ['Sükran Ovali', 6.300000000000001, 2], ['Ezgi Mola', 6.800000000000001, 2],
             ['Seher Devrim Yakut', 5.375, 4], ['Bora Akkas', 5.333333333333333, 3], ['Lavinia Longhi', 7.5, 1],
             ['Mehmet Ali Nuroglu', 6.8, 3], ['Erdal Yildiz', 7.5, 1], ['Esra Ronabar', 6.95, 2],
             ['Murat Arkin', 4.1, 1], ['Sevcan Yasar', 7.35, 2], ['Birol Denizci', 6.199999999999999, 2],
             ['Serpil Gül', 7.6, 1], ['Murat Aydin', 5.6, 1], ['Halis Bayraktaroglu', 5.55, 2],
             ['Mustafa Vuran', 4.7, 1], ['Alara Keçeci', 4.7, 1], ['Cihan Simsek', 6.1, 1],
             ['Turhan Cihan Simsek', 6.1, 1], ['Merve Hazer', 6.1, 1], ['Volkan Bora Dilek', 3.8, 1],
             ['Inanç Benlioglu', 3.8, 1], ['Meltem Dag', 3.8, 1], ['Basak Zebil', 3.8, 1], ['Adnan Koç', 3.3, 1],
             ['Nurhak Mine Soz', 3.3, 1], ['Ceren Hindistan', 4.35, 2], ['Tuba Dogma', 1.8, 1],
             ['Yaprak Durmaz', 3.25, 2], ['Süleyman Karadag', 1.8, 1], ['Sule Zeybek', 3.6, 1],
             ['Pelin Akil', 5.7625, 8], ['Ulas Inan Inaç', 5.5, 1], ['Koray Erkök', 5.75, 2], ['Elçin Sangu', 7.06, 5],
             ['Cande Percem', 6.0, 1], ['Oguz Oktay', 3.9, 1], ['Inci Türkay', 3.9, 1], ['Okan Çabalar', 7.2, 1],
             ['Bahar Kerimoglu', 5.6, 1], ['Ceren Reis', 5.6, 1], ['Cezmi Baskin', 4.15, 2],
             ['Mustafa Üstündag', 6.166666666666667, 3], ['Carlos Martín', 4.5, 1],
             ['Ali Ersan Duru', 5.133333333333334, 3], ['Çisem Çanci', 4.9, 1], ['Can Atak', 4.9, 1],
             ['Zeynep Çamci', 6.3, 3], ['Asli Bekiroglu', 7.050000000000001, 2], ['Mehmet Atay', 5.666666666666667, 3],
             ['Yamaç Telli', 7.0, 1], ['Tim Seyfi', 7.0, 1], ['Atilla Pekdemir', 7.0, 1], ['Gürkan Kaçar', 7.0, 1],
             ['Özgür Emre Yildirim', 7.0, 1], ['Buket Orhan', 2.8, 1], ['Erol Gedik', 6.8, 1],
             ['Görkem Türkes', 6.8, 1], ['Kerem Bürsin', 6.68, 5], ['Hande Dogandemir', 7.133333333333333, 3],
             ['Yagmur Tanrisevsin', 5.966666666666666, 3], ['Ismail Ege Sasmaz', 6.85, 2], ['Orhan Güner', 6.55, 2],
             ['Ersin Korkut', 7.1, 1], ['Taner Tuncay', 7.3, 1], ['Nermin Koçak', 7.3, 1], ['Cahit Gök', 7.6, 2],
             ['Emir Bozkurt', 6.5, 1], ['Hakan Kurtas', 5.75, 2], ['Mehmet Özgür', 7.1, 1], ['Bengü Ergin', 7.1, 1],
             ['Nilperi Sahinkaya', 5.633333333333333, 3], ['Kaan Yildirim', 6.575, 4], ['Cankat Aydos', 5.125, 4],
             ['Serenay Sarikaya', 7.4, 2], ['Metin Akdülger', 6.25, 2], ['Yunus Emre Yildirimer', 6.0, 2],
             ['Ahmet Mümtaz Taylan', 7.599999999999999, 3], ['Mehmet Aykaç', 7.15, 2], ['Mehmet Esen', 6.9, 2],
             ['Serhan Yavas', 5.2, 1], ['Tolga Güleç', 5.2, 1], ['Efsane Odag', 7.1, 1], ['Didem Soydan', 7.1, 1],
             ['Ekin Koç', 6.95, 2], ['Demet Özdemir', 6.0, 5], ['Murat Balci', 6.1, 1], ['Emre Yetim', 6.1, 1],
             ['Özlem Çakar', 6.1, 1], ['Begüm Birgören', 7.15, 2], ['Nehir Büyükakçay', 3.4, 1], ['Elit Cam', 4.05, 2],
             ['Yesim Aliç', 3.4, 1], ['Göktug Alpasar', 3.4, 1], ['Duygu Sarisin', 3.1, 1], ['Defne Samyeli', 3.6, 1],
             ['Cagri Citanak', 3.6, 1], ['Cansu Demirci', 5.1, 1], ['Sina Ozer', 5.449999999999999, 2],
             ['Begüm Akkaya', 6.1, 1], ['Alihan Araci', 6.1, 1], ['Gözde Cigaci', 5.449999999999999, 2],
             ['Gülenay Kalkan', 6.1, 1], ['Zafer Diper', 4.4, 1], ['Berk Atan', 5.8999999999999995, 3],
             ['Su Kutlu', 5.766666666666667, 3], ['Deger Soysal', 4.7, 1], ['Yasemin Erkent', 4.7, 1],
             ['Alp Akar', 4.949999999999999, 2], ['Evrim Alasya', 6.366666666666667, 3],
             ['Firat Altunmese', 6.866666666666667, 3], ['Ertugrul Aytaç Usun', 4.8, 1], ['Ayberk Aladar', 4.8, 1],
             ['Murat Sencan', 7.2, 1], ['Ata Atabek', 7.2, 1], ['Alp Guneyman', 7.2, 1], ['Kaan Gure', 7.2, 1],
             ['Yekta Kopan', 7.15, 2], ['Cem Yilmaz', 7.3, 1], ['Aylin Engör', 5.4, 1], ['Efsun Akkurt', 6.2, 1],
             ['Vildan Atasever', 6.066666666666666, 3], ['Mediha Aydin', 6.2, 1], ['Ozan Özcan', 6.4, 1],
             ['Caner Özyurtlu', 6.4, 1], ['Bengi Öztürk', 5.2, 1], ['Devrim Atmaca', 5.2, 1], ['Aysen Batigün', 5.2, 1],
             ['Ece Baykal', 5.2, 1], ['Doga Rutkay', 6.7, 1], ['Aylin Kontante', 6.7, 1], ['Erdem Akin', 5.6, 1],
             ['Muharrem Bayrak', 5.6, 1], ['Zahide Yetis', 5.1, 1], ['Ömer Levent Dilli', 7.1, 1],
             ['Tayfun Atac', 7.1, 1], ['Thiago Vlentim', 7.1, 1], ['Ali Tuna Dilli', 7.1, 1], ['Asli Ozmel', 7.2, 1],
             ['Sidal Damar', 7.2, 1], ['Ahmet Yenilmez', 7.2, 1], ['Tülay Bursa', 7.6, 1], ['Keremcan Köse', 7.6, 1],
             ['Sükrü Özyildiz', 7.15, 4], ['Fatih Portakal', 9.1, 1], ['Semra Dinçer', 7.5, 1], ['Nihan Asici', 4.7, 1],
             ['Yigit Mergen', 4.7, 1], ['Farah Zeynep Abdullah', 6.4, 2], ['Caglar Ertugrul', 7.0, 4],
             ['Damla Colbay', 5.95, 2], ['Faruk Acar', 6.6, 1], ['Vugar Aliyev', 6.6, 1], ['Sahin Sahin', 7.7, 1],
             ['Beslan Babaoglu', 7.7, 1], ['Ceren Moray', 6.45, 2], ['Bahar Sahin', 5.0, 1],
             ['Biran Damla Yilmaz', 5.7, 1], ['Sinasi Yurtsever', 8.6, 1], ['Sermiyan Midyat', 4.4, 1],
             ['Tarik Bayrak', 6.8, 1], ['Sinan Divrik', 6.8, 1], ['Emre Ihlamur', 6.8, 1], ['Merve Ihlamur', 6.8, 1],
             ['Emir Berke Zincidi', 3.6500000000000004, 2], ['Baris Yalçin', 5.8, 1], ['Osman Beyaz', 5.5, 1],
             ['Aysel Durmus', 5.5, 1], ['Boran Gökçe', 5.5, 1], ['Eda Özdemir', 2.6, 1], ['Esin Gündogdu', 2.6, 1],
             ['Çiçek Acar', 6.2, 2], ['Ipek Bagriacik', 5.2, 1], ['Yusa Bozkurt', 5.2, 1],
             ['Gökhan Alkan', 5.766666666666667, 3], ['Aysenil Samlioglu', 4.3, 1], ['Erman Okay', 4.3, 1],
             ['Yesim Salkim', 4.3, 1], ['Ayse Akin', 4.8, 1], ['Ipek Ozagan', 4.8, 1], ['Ceren Koç', 4.8, 1],
             ['Özge Gürel', 6.5, 4], ['Serkan Çayoglu', 5.4, 1], ['Daghan Külegeç', 5.4, 1], ['Berk Cankat', 6.275, 4],
             ['Açelya Topaloglu', 5.566666666666666, 3], ['Ebru Özkan', 6.7, 2], ['Nursel Köse', 6.95, 2],
             ['Alina Boz', 6.95, 2], ['Selen Soyder', 6.7, 2], ['Yurdaer Okur', 6.85, 2], ['Ismail Demirci', 6.9, 1],
             ['Metin Çekmez', 4.9, 1], ['Almila Ada', 6.050000000000001, 2], ['Anil Altan', 6.366666666666667, 3],
             ['Bennu Yildirimlar', 6.800000000000001, 2], ['Filiz Kaya', 5.3, 1], ['Gülcan Arslan', 7.35, 2],
             ['Nadir Saribacak', 6.766666666666667, 3], ['Cem Korkmaz', 5.6, 1], ['Cihat Suvarioglu', 5.6, 1],
             ['Duygu Yurukce', 5.6, 1], ['Uraz Kaygilaroglu', 6.933333333333333, 3],
             ['Baran Akbulut', 7.566666666666667, 3], ['Mert Turak', 7.5, 1], ['Ali Barkin', 7.5, 1],
             ['Elvan Disli', 7.5, 1], ['Ceyhun Tutal', 7.5, 1], ['Ege Sezer', 4.7, 1], ['Ömer Faruk Biçer', 4.7, 1],
             ['Arda Beyaztas', 4.7, 1], ['Mehmet Duran', 4.7, 1], ['Atalay Demirci', 5.5, 1], ['Cengiz Coskun', 7.2, 1],
             ['Nurettin Sönmez', 7.2, 1], ['Cem Uçan', 6.6, 1], ['Kamil Güler', 6.6, 1], ['Hakan Yufkacigil', 6.6, 1],
             ['Erhan Alpay', 6.3, 1], ['Özgür Avsar', 6.3, 1], ['Elena Viunova', 6.0, 1], ['Burak Satibol', 5.15, 2],
             ['Emre Kivilcim', 3.0, 1], ['Ekrem Erdinç', 3.0, 1], ['Ozanay Alpkan', 3.0, 1], ['Emre Avsar', 8.6, 1],
             ['Yasar Aydinlioglu', 8.6, 1], ['Gül Arici', 7.8, 1], ['Onur Saylak', 5.7, 1], ['Numan Çakir', 7.7, 1],
             ['Ilayda Alisan', 7.7, 1], ['Ali Karagöz', 6.8, 1], ['Beste Kökdemir', 6.15, 2], ['Merve Oflaz', 6.8, 1],
             ['Basak Demiral', 3.2, 1], ['Cansu Gultekin', 3.2, 1], ['Hüseyin Güler', 3.2, 1],
             ['Sezgi Sena Akay', 4.933333333333334, 3], ['Nesem Akhan', 3.4, 1], ['Mehmet Küçük', 5.5, 1],
             ['Dilara Büyükbayraktar', 5.5, 1], ['Merve Anlagan', 5.5, 1], ['Mehmet Baran Erdogan', 6.8, 1],
             ['Ediz Hun', 6.8, 1], ['Leyla Kader Ilhan', 6.8, 1], ['Burak Can', 4.8, 1], ['Yagiz Kilinc', 5.8, 1],
             ['Ali Sürmeli', 7.3, 1], ['Gün Koper', 6.9, 1], ['Serdar Gökay Akduman', 5.7, 1],
             ['Tugçe Aksoylu', 5.7, 1], ['Meral Avci', 5.7, 1], ['Murat Ceylan', 5.85, 2], ['Zafer Mete', 5.5, 1],
             ['Necip Memili', 5.933333333333333, 3], ['Berk Erçer', 3.8, 1], ['Gonca Sariyildiz', 3.8, 1],
             ['Ilker Kaleli', 8.4, 1], ['Musa Uzunlar', 8.4, 1], ['Ali Il', 8.4, 2], ['Farid Khalifi', 7.3, 1],
             ['Adem Yilmaz', 2.6, 1], ['Reha Özcan', 6.133333333333333, 3], ['Samuray Polat Uncumusaoglu', 7.1, 1],
             ['Mazlum Kiper', 7.1, 1], ['Ufuk Bayraktar', 6.5, 1], ['Gökhan Azlag', 4.4, 1],
             ['Sadi Celil Cengiz', 4.4, 1], ['Fulya Ergünes', 4.4, 1], ['Hakan Sahin', 6.2, 1],
             ['Gökhan Atalay', 7.25, 2], ['Payidar Tüfekçioglu', 7.2, 1], ['Mehmet Çepiç', 7.2, 1],
             ['Tulin Yazkan', 4.7, 1], ['Kubra Suzgun', 5.15, 2], ['Serkan Tinmaz', 4.8, 1], ['Mehmet Celik', 6.3, 2],
             ['Coraline Chapatte', 5.0, 1], ['Deniz Erayvaz', 5.0, 1], ['Seren Sirince', 5.4, 1],
             ['Hakan Hepcan', 5.1, 1], ['Marie Hartlieb', 5.1, 1], ['Salih Zafer Kunt', 5.1, 1],
             ['Mustafa Devrim Özdinç', 5.1, 1], ['Can Yaman', 7.1000000000000005, 3], ['Nilay Duru', 5.15, 2],
             ['Eren Vurdem', 5.7, 1], ['Yusuf Çim', 5.2, 1], ['Leyla Uner Ermaya', 5.2, 1],
             ['Kubilay Penbeklioglu', 5.2, 1], ['Dilan Çiçek Deniz', 6.633333333333333, 3], ['Büsra Develi', 6.35, 2],
             ['Melisa Senolsun', 6.2, 2], ['Gökhan Keser', 3.9, 1], ['Ruveyda Öksuz', 3.9, 1],
             ['Tolga Saritas', 6.35, 2], ['Burcu Özberk', 6.75, 2], ['Berrin Seker Civil', 6.6, 1],
             ['Suleyman Felek', 6.6, 1], ['Ayça Erturan', 7.1, 1], ['Sabina Ajrula', 7.1, 1],
             ['Hazar Ergüçlü', 6.58, 5], ['Arif Diren', 6.2, 1], ['Veda Yurtsever Ipek', 6.2, 1],
             ['Hakan Bozbey', 6.5, 1], ['Elif Küçük', 6.5, 1], ['Alp Pazarli', 6.5, 1], ['Akif Yardimci', 6.5, 1],
             ['Burak Kimyager', 4.9, 1], ['Meryem Sengül', 4.9, 1], ['Kayra Aleyna Zabçi', 4.9, 1],
             ['Tolga Öz', 4.9, 1], ['Mehdi Adlin', 7.566666666666667, 3], ['Erol Aksoy', 7.6, 1],
             ['Cansu Diktas', 7.6, 1], ['Yigit Dikmen', 5.2, 1], ['Samet Sirmali', 5.6, 1],
             ['Ahmet Olgun Sunaer', 5.6, 1], ['Alperen Duymaz', 6.833333333333333, 3], ['Hakan Dinçkol', 5.4, 2],
             ['Amine Gulse', 5.8, 1], ['Safak Pekdemir', 5.8, 1], ['Tamer Levent', 7.2, 1], ['Tülin Oral', 7.2, 1],
             ['Pelin Cift', 7.9, 1], ['Emrah Ablak', 7.0, 1], ['Levent Cantek', 7.0, 1], ['Bülent Üstün', 7.0, 1],
             ['Hande Özen', 6.8, 1], ['Ushan Çakir', 7.5, 1], ['Gülçin Santircioglu', 7.5, 1],
             ['Cengiz Özdemir', 8.0, 1], ['Ozan Sagsöz', 8.0, 1], ['Eren Hacisalihoglu', 6.5, 1],
             ['Alper Saldiran', 6.15, 2], ['Celile Toyon Uysal', 6.5, 1], ['Oya Unustasi', 6.5, 1],
             ['Dogan Akdogan', 7.65, 2], ['Giray Altinok', 8.0, 1], ['Özgün Bayraktar', 8.0, 1],
             ['Alper Baytekin', 8.0, 1], ['Merve Aydin', 5.3, 1], ['Turabi Çamkiran', 5.3, 1], ['Ulas Torun', 4.3, 2],
             ['Bengi Idil Uras', 7.4, 1], ['Ecem Özkaya', 7.1, 1], ['Seray Gözler', 7.133333333333333, 3],
             ['Deniz Celiloglu', 6.1, 1], ['Ülkü Hilal Çiftçi', 4.8, 2], ['Bige Önal', 3.8, 1],
             ['Zeynep Elçin', 3.8, 1], ['Emre Akça', 6.2, 1], ['Istephan Hakverdi', 6.2, 1],
             ['Kaan Tüfekçiyasar', 6.2, 1], ['Gülce Baydar', 6.2, 1], ['Zeynep Kankonde', 4.3, 1],
             ['Zeynep Anacan', 6.1, 1], ['Elif Cakman', 6.1, 1], ['Hande Erçel', 6.55, 2],
             ['Burak Deniz', 6.949999999999999, 2], ['Özcan Tekdemir', 7.3, 1], ['Merve Çagiran', 7.3, 1],
             ['Özge Özder', 6.766666666666667, 3], ['Aslihan Güner', 6.6, 1], ['Nil Karaibrahimgil', 7.0, 1],
             ['Öykü Celik', 6.7, 1], ['Ekin Mert Daymaz', 6.7, 1], ['Damla Aslanalp', 6.7, 1], ['Engin Öztürk', 5.4, 1],
             ['Ozan Dolunay', 6.2, 3], ['Meric Aral', 6.2, 2], ['Sumru Yavrucuk', 3.5, 1], ['Gökçe Özyol', 3.5, 1],
             ['Burak Serdar Sanal', 5.8, 1], ['Hayal Köseoglu', 5.8, 1], ['Nihal G. Koldas', 7.4, 1],
             ['Aras Aydin', 4.6, 1], ['Osman Karakoç', 4.6, 1], ['Hazal Subasi', 5.300000000000001, 2],
             ['Erkan Meriç', 4.7, 1], ['Aykut Igdeli', 4.7, 1], ['Sezer Avci', 6.2, 1], ['Ipek Ayaz', 6.2, 1],
             ['Boran Kuzum', 7.65, 2], ['Pinar Deniz', 7.45, 2], ['Beren Gokyildiz', 7.3, 2],
             ['Gonca Vuslateri', 6.8, 1], ['Kanbolat Gorkem Arslan', 5.6, 1], ['Deniz Can Aktas', 5.6, 1],
             ['Rabia Arslan', 4.7, 1], ['Kader Çabuk', 4.7, 1], ['Hatice Kirik', 4.7, 1], ['Ali Akdal', 6.4, 1],
             ['Emir Benderlioglu', 6.4, 1], ['Serkan Kuru', 7.1, 2], ['Sezin Bozaci', 5.9, 1], ['Eva Dedova', 5.9, 1],
             ['Doga Zeynep Doguslu', 5.9, 1], ['Tuba Erdem', 6.5, 1], ['Yeliz Kuvanci', 6.5, 1], ['Emir Öner', 6.5, 1],
             ['Dilara Akin Yazici', 6.2, 1], ['Emine Erdem', 4.6, 1], ['Burcu Kiratli', 4.6, 1],
             ['Beyza Kesebir', 4.3, 1], ['Kadir Agirçelik', 6.0, 1], ['Latif Akgedik', 6.0, 1],
             ['Faruk Akgören', 6.0, 1], ['Kenan Acar', 7.0, 1], ['Cem Aksakal', 7.0, 1], ['Savas Satis', 8.2, 1],
             ['Cihangir Ceyhan', 8.2, 1], ['Özgür Meric', 8.2, 1], ['Burak Sahin', 8.2, 1],
             ['Cemal Elçin Akar', 7.7, 1], ['Burcu Altin', 6.8999999999999995, 3], ['Ahmet Selçuk Bay', 7.1, 1],
             ['Sebnem Dogruer', 7.1, 1], ['Basak Parlak', 6.55, 2], ['Yazmeen Baker', 5.8, 1],
             ['Ahmet Dizdaroglu', 7.4, 1], ['Baris Aytac', 6.9, 1], ['Yesim Gül Aksar', 6.8, 1],
             ['Oktay Alkan', 6.8, 1], ['Ibrahim Aslan', 6.8, 1], ['Gizem Akdag', 6.3, 1], ['Yasemin Aydan', 6.3, 1],
             ['Nesil Dinçelmas', 6.3, 1], ['Zeyd Gümüstutan', 6.3, 1], ['Berat Efe Parlar', 2.3, 1],
             ['Esat Polat Güler', 2.3, 1], ['Vicky Kaya', 5.0, 1], ['Gogo Garifallou', 5.0, 1],
             ['Vangelis Harisopoulos', 5.0, 1], ['Osman Alkas', 6.05, 2], ['Canan Erguder', 6.1, 1],
             ['Taha Ulukaya', 9.3, 1], ['Andac Ulukaya', 9.3, 1], ['Taner Sahin', 9.3, 1], ['Neslihan Ulusoy', 9.3, 1],
             ['Elif Baysal', 8.1, 1], ['Nevin Efe', 8.1, 1], ['Gamze Süner Atay', 7.3, 1], ['Alihan Türkdemir', 6.1, 1],
             ['Dilan Telkok', 6.1, 1], ['Baris Kiliç', 6.1, 1], ['Berrak Tüzünataç', 8.1, 1], ['Nazan Kesal', 7.1, 1],
             ['Sedef Akalin', 6.7, 1], ['Fatih Altinagac', 6.7, 1], ['Su Burcu Coskun', 6.7, 1],
             ['Burç Kümbetlioglu', 6.2, 1], ['Dogan Bayraktar', 6.2, 1], ['Nihat Altinkaya', 7.0, 1],
             ['Burak Sevinç', 7.0, 1], ['Anil Ilter', 2.8, 1], ['Hazal Senel', 5.5, 1], ['Cigdem Atasoyu', 5.9, 1],
             ['Ceyda Sener Baykal', 5.9, 1], ['Aylin Dinc', 5.9, 1], ['Fikret Durak', 5.9, 1],
             ['Ibrahim Eren Kilisli', 5.7, 1], ['Mutlu Ulusoy', 5.7, 1], ['Dilhan Naz Özgülüs', 5.7, 1],
             ['Tuvana Türkay', 5.7, 1], ['Nilay Deniz', 6.550000000000001, 2], ['Burcu Türünz', 6.8, 1],
             ['Basar Dogusoy', 6.8, 1], ['Ceyhun Mergiroglu', 6.0, 1], ['Ulas Tuna Astepe', 6.5, 2],
             ['Hayati Akbas', 5.8, 1], ['Seda Güven', 7.2, 1], ['Cemre Polat', 6.6, 1], ['Gürol Salman', 6.6, 1],
             ['Melis Tüzüngüç', 5.5, 1], ['Umit Kantarcilar', 5.5, 1], ['Ahmet Varli', 5.5, 1],
             ['Deniz Bolisik', 5.5, 1], ['Settar Tanriögen', 5.0, 1], ['Nergis Öztürk', 5.0, 1],
             ['Ilkay Akdagli', 6.0, 1], ['Hande Katipoglu', 1.2, 1], ['Batuhan Aydar', 6.2, 1], ['Ercan Kesal', 8.3, 1],
             ['Burak Sekmen', 7.7, 1], ['Bahadir Oz', 7.7, 1], ['Mehmet Arif Bulak', 7.7, 1],
             ['Beste Yilmazer', 7.7, 1], ['Akin Akinözü', 7.8, 1], ['Muhammet Uzuner', 8.7, 1],
             ['Feride Hilal Akin', 6.3, 1], ['Burçin Bildik', 6.3, 1], ['Erkan Sever', 7.2, 1], ['Seray Kaya', 7.7, 1],
             ['Oguzhan Ugur', 7.2, 1], ['Berk Uçar', 7.2, 1], ['Turan Oguzhan', 7.2, 1], ['Ezgi Ünal', 7.2, 1],
             ['Gözde Mukavelat', 7.4, 1], ['Emir Çiçek', 7.4, 1], ['Ahsen Eroglu', 7.4, 1], ['Müjde Uzman', 7.4, 1],
             ['Berkay Dabakoglu', 6.9, 1], ['Cem Ertunc', 6.9, 1], ['Berke Odaci', 6.9, 1], ['Ergin Ulunay', 6.9, 1],
             ['Serkan Balbal', 4.1, 1], ['Zeyno Günenç', 4.1, 1], ['Öykü Güven', 4.1, 1], ['Gökhan Akgül', 8.0, 1],
             ['Serhat Buga', 8.0, 1], ['Mesut Cobanbasi', 8.0, 1], ['Tuncay Koca', 8.0, 1],
             ['Yagmur Özbasmaci Mermer', 6.4, 1], ['Günes Emir', 6.4, 1], ['Mehmet Gürhan', 6.4, 1],
             ['Berna Canbeldek', 6.2, 1], ['Bilgehan Demir', 6.2, 1], ['Aycan Demirci', 6.2, 1],
             ['Cansu Dagdelen', 2.5, 1], ['Feri Baycu Güler', 2.5, 1], ['Ayris Alptekin', 7.0, 1],
             ['Suna Sancaktar', 7.0, 1], ['Emre Yesiloz', 8.6, 1], ['Feyza Özgür', 8.6, 1],
             ['Mustafa Mesut Baskir', 8.6, 1], ['Yavuz Selim Osmanoglu', 8.6, 1], ['Sevda Erginci', 6.95, 2],
             ['Gülsün Sare Fil', 8.4, 1], ['Erdinç Gülener', 7.4, 1], ['Özgü Kaya', 6.9, 1], ['Ali Meriç', 5.5, 1],
             ['Günes Hayat', 5.5, 1], ['Irem Helvacioglu', 7.0, 1], ['Ahu Sungur', 6.4, 1], ['Sarp Apak', 7.0, 1],
             ['Derya Karadas', 7.0, 1], ['Derya Kahraman', 5.0, 1], ['Sultan Köroglu Kiliç', 5.0, 1],
             ['Anil Berk Baki', 5.0, 1], ['Hilmicem Intepe', 5.0, 1], ['Nagihan Karadere', 5.0, 1],
             ['Adem Kilicci', 5.0, 1], ['Ugur Günes', 6.7, 1], ['Ezgi Senler', 6.9, 1], ['Özge Akdeniz', 5.9, 1],
             ['Kübra Akin', 5.9, 1], ['Emre Ataman', 5.9, 1], ['Birkan Sokullu', 6.6, 1], ['Haydar Biçakci', 5.8, 1],
             ['Emre Bolat', 5.8, 1], ['Hasan Ekinci', 5.8, 1], ['Turgut Eryilmaz', 5.8, 1], ['Rifat Kanpara', 8.4, 1],
             ['Ahmet Avni Yilmaz', 8.4, 1], ['Mahmut Kotan', 8.4, 1], ['Ahmet Akyol', 8.4, 1],
             ['Aleksandra Nikiforova', 7.1, 1], ['Fatih Ürek', 7.1, 1], ['Ezgi Yildirim', 7.1, 1],
             ['Reyhan Yildirim', 7.1, 1], ['Sevgül Kiroglu', 7.1, 1], ['Çagla Demir', 6.3, 1], ['Özlem Türkad', 6.3, 1],
             ['Naz Sayiner', 7.0, 1], ['Burak Yörük', 5.8, 1], ['Selen Uçer', 5.8, 1], ['Pelin Öztekin', 5.8, 1],
             ['Begüm Cana Özgür', 7.8, 1], ['Mizgin Ay', 7.8, 1], ['Tugçe Akgün', 7.8, 1], ['Karsu Dönmez', 7.8, 1],
             ['Elif Dogan', 5.8, 1], ['Öznur Serçeler', 8.2, 1], ['Berkay Veli', 6.2, 1], ['Sila Özlem Önemli', 6.2, 1],
             ['Emrah Akduman', 6.2, 1], ['Sude Dogar', 6.2, 1], ['Bestemsu Özdemir', 6.1, 1], ['Alp Navruz', 7.9, 1],
             ['Cemre Gümeli', 7.9, 1], ['Grzegorz Damiecki', 6.4, 1], ['Agnieszka Grochowska', 6.4, 1],
             ['Sylwia Juszczak', 6.4, 1], ['Wojciech Zoladkowicz', 6.4, 1], ['Ece Sükan', 7.2, 1],
             ['Onur Durmaz', 3.6, 1], ['Yagizcan Küçükcan', 3.6, 1], ['Cemre Kurum', 3.6, 1], ['Irem Çalhan', 3.6, 1],
             ['Serhat Teoman', 7.8, 1], ['Mehmet Yalçinkaya', 5.2, 1], ['Somer Sivrioglu', 5.2, 1],
             ['Hazer Amani', 5.25, 2], ['Hakan Kanik', 5.2, 1], ['Tolga Tekin', 5.9, 1], ['Mert Yazicioglu', 5.9, 1],
             ['Esra Bilgic', 5.9, 1], ['Zerrin Tekindor', 7.4, 1], ['Aybüke Pusat', 7.4, 1], ['Ibrahim Selim', 9.4, 1],
             ['Irem Erten', 9.4, 1], ['Mert Efe Günaydin', 9.4, 1], ['Furkan Inanir', 9.4, 1],
             ['Bartu Küçükçaglayan', 8.0, 1], ['Müfit Kayacan', 8.0, 1], ['Cem Zeynel Kiliç', 8.0, 1],
             ['Cemre Ebuzziya', 8.0, 1], ['Melisa Pamuk', 8.9, 1], ['Tugba Çinar', 3.6, 1], ['Eser Yenenler', 5.3, 1],
             ['Kubilay Aka', 5.3, 1], ['Özgür Ege Nalci', 7.8, 1], ['Burak Kut', 7.8, 1], ['Leya Kirsan', 7.8, 1],
             ['Beril Su Hatirnaz', 8.0, 1], ['Abdulkerim Tunc', 8.0, 1]]

    toplam = 0
    count = 0
    sonuc = []

    for i in range(len(oyuncuList)):
        for j in range(len(oyuncuList[i])):

            if (oyuncuList[i][j] in aktorUniq):

                index = aktorUniq.index(oyuncuList[i][j])
                toplam = toplam + aktorPuan[index][1]
                count = count + 1
                flag = 1
            else:
                flag = 0

        if (flag == 1):
            ortalama = toplam / count
            sonuc.append(ortalama)
            count = 0
            toplam = 0
        else:

            sonuc.append(0)
        flag = 0

    return sonuc
