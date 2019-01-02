from bs4 import BeautifulSoup
import requests
import VeriTemizleme as vt
import pandas as pd
import KNN as knn


# url = 'https://www.imdb.com/search/title?title_type=tv_series&countries=tr&ref_=adv_prv'
# url2 = "https://www.imdb.com/search/title?title_type=tv_series&countries=tr&sort=year,asc"
# url3 = "https://www.imdb.com/search/title?title_type=tv_series&countries=tr&sort=year,asc"
# url4 = "https://www.imdb.com/search/title?title_type=tv_series&countries=tr&sort=year,asc&start=51&ref_=adv_nxt"
# reps = requests.get(url)
# soup = BeautifulSoup(reps.content,'html.parser')
#
# contentVerileri = soup.find_all('div',{"class":"lister-item-content"})

def internettenVeriCekme():
    # print(len(contentVerileri))
    diziIsimleri = []
    tarihVerileri = []
    tur = []
    turT = []
    imdbRange = []
    actor = []
    kopru = []

    for urlDeger in range(1, 1301, 50):

        if (urlDeger == 1):
            url = "https://www.imdb.com/search/title?title_type=tv_series&countries=tr&sort=year,asc&ref_=adv_prv"

        else:
            url = "https://www.imdb.com/search/title?title_type=tv_series&countries=tr&sort=year,asc&start=" + str(
                urlDeger) + "&ref_=adv_nxt"

        reps = requests.get(url)
        soup = BeautifulSoup(reps.content, 'html.parser')
        contentVerileri = soup.find_all('div', {"class": "lister-item-content"})

        for i in contentVerileri:

            if ((i.find("strong")) != None and (i.find("p").find("span", {"class": "genre"})) != None and
                    i.find_all("p")[2].find_all("a") != None and (i.find("p").find("span", {"class": "genre"}))):
                diziIsimleri.append(i.find("h3").find('a').text)
                tarihVerileri.append(i.find("h3").find('span', {"class": "lister-item-year text-muted unbold"}).text)

                turT.append(i.find("p").find("span", {"class": "genre"}).text)

                #  print(i.find("p").find("span",{"class":"genre"}).text)
                imdbRange.append(i.find("strong").text)
                star = i.find_all("p")
                stars = star[2].find_all("a")
                # fatih = omer[0].text

                # print(tarihVerileri)  # append kullanılacak
                # print(star[2])
                # q  print(tur)

                # o1 = omer[0].text
                for j in stars:
                    kopru.append(j.text)

                actor.append(kopru)
                kopru = []

    baslangicT, bitisTarih = vt.tarihBelirleme(tarihVerileri)

    sezonSayisi, sezonDurumu = vt.sezonHesapla(baslangicT, bitisTarih)

    oyuncuPuan, aktorUniq = vt.aktorPuan(imdbRange, actor)

    aktorS = vt.castOyuncuKadro(actor)  # aktorString

    oyuncuKadroPuan = vt.diziKadroPuan(aktorUniq, actor, oyuncuPuan)

    turT = vt.satirTemizle(turT)  # aga tüm türleri bir arada dönderiyo
    tur = vt.tur(turT)  # tek türleri dönderiyo 0. index yani
    konuP = vt.dictionary(turT)

    # print(konuP)
    #
    # print(tur)

    # print(len(diziIsimleri))
    # print(type(tarihVerileri[0]))

    raw_data = {

        "isim": diziIsimleri,
        "baslangicT": baslangicT,
        "bitisTarih": bitisTarih,
        "tur": tur,

        "konuPuan": konuP,
        "aktorS": aktorS,
        "oyuncuKadroPuan": oyuncuKadroPuan,
        "imdb": imdbRange,
        "sezonSayisi": sezonSayisi,
        "sezonDurumu": sezonDurumu,

    }

    df = pd.DataFrame(raw_data,
                      columns=['isim', 'baslangicT', 'bitisTarih', 'tur', 'konuPuan',
                               'aktorS', 'oyuncuKadroPuan', 'imdb', 'sezonSayisi', 'sezonDurumu'])
    df.to_csv("DiziFaktor.csv")


def kullanicidanVeriAlma():
    count = input("kaç adet dizi verisi gireceğinizi belirleyiniz..\n")

    diziİsmi = []
    baslangicT = []
    bitisTarih = []
    sezonSayisi = []
    sezonDurumu = []
    tur = []
    turYek = []
    konuPuan = []
    aktorIsimleri = []
    imdb = []

    for i in range(int(count)):
        diziİsmi.append(input("dizi ismini giriniz :"))
        baslangicT.append(input("dizi baslangic tarihini giriniz :"))
        tur.append(input("dizi turunu giriniz :"))
        kopru = input("aktor isimlerini giriniz :")

        aktorIsimleri.append(kopru.split(","))

    temizTur = vt.satirTemizle(tur)

    kopru = vt.tur(temizTur)  # tek türleri dönderiyo 0. index yani
    turYek.append(kopru)
    konuPuan = vt.dictionary(temizTur)
    diziKadroPuan = vt.diziKadroPuanForUser(aktorIsimleri)

    print("Kullanıcıdan girilen veriler ve işlenecek olan veriler :\n")
    for i in range(int(count)):
        print(i + 1, ". dizinin verileri : ", "dizi ismi :", diziİsmi[i], "baslangic tarihi: ", baslangicT[i], "tur:",
              turYek[i], "Konu içeriği puanı :",
        konuPuan[i], "dizinin kadrosunun genel ortalama puanı :" ,diziKadroPuan[i],"\n")



        knn.knnHesaplama(turYek, konuPuan, diziKadroPuan)

kullanicidanVeriAlma()
