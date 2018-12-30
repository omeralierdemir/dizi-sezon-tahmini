from bs4 import BeautifulSoup
import requests
import VeriTemizleme as vt
import pandas as pd


# url = 'https://www.imdb.com/search/title?title_type=tv_series&countries=tr&ref_=adv_prv'
# url2 = "https://www.imdb.com/search/title?title_type=tv_series&countries=tr&sort=year,asc"
# url3 = "https://www.imdb.com/search/title?title_type=tv_series&countries=tr&sort=year,asc"
# url4 = "https://www.imdb.com/search/title?title_type=tv_series&countries=tr&sort=year,asc&start=51&ref_=adv_nxt"
# reps = requests.get(url)
# soup = BeautifulSoup(reps.content,'html.parser')
#
# contentVerileri = soup.find_all('div',{"class":"lister-item-content"})

counter = 0

#print(len(contentVerileri))
diziIsimleri = []
tarihVerileri = []
tur = []
turT = []
imdbRange = []
actor = []
kopru = []

for urlDeger in range(1,1301,50):

    if (urlDeger == 1):
        url = "https://www.imdb.com/search/title?title_type=tv_series&countries=tr&sort=year,asc&ref_=adv_prv"

    else:
        url = "https://www.imdb.com/search/title?title_type=tv_series&countries=tr&sort=year,asc&start=" + str(urlDeger) + "&ref_=adv_nxt"

    reps = requests.get(url)
    soup = BeautifulSoup(reps.content, 'html.parser')
    contentVerileri = soup.find_all('div', {"class": "lister-item-content"})

    for i in contentVerileri:

        if((i.find("strong")) != None and (i.find("p").find("span",{"class":"genre"})) != None and  i.find_all("p")[2].find_all("a") != None  and (i.find("p").find("span",{"class":"genre"}))):
            diziIsimleri.append(i.find("h3").find('a').text)
            tarihVerileri.append(i.find("h3").find('span',{"class":"lister-item-year text-muted unbold"}).text)

            turT.append(i.find("p").find("span",{"class":"genre"}).text)

          #  print(i.find("p").find("span",{"class":"genre"}).text)
            imdbRange.append(i.find("strong").text)
            star = i.find_all("p")
            stars = star[2].find_all("a")
           # fatih = omer[0].text

            #print(tarihVerileri)  # append kullanılacak
            #print(star[2])
          #q  print(tur)



            # o1 = omer[0].text
            for j in stars:
                kopru.append(j.text)

            actor.append(kopru)
            kopru = []



baslangicT,bitisTarih = vt.tarihBelirleme(tarihVerileri)

sezon = vt.sezonHesapla(baslangicT,bitisTarih)

#print(actor)

oyuncuKadro = vt.aktorPuan(imdbRange,actor)
aktorS = vt.castOyuncuKadro(actor)# aktorString
print(aktorS)



turT = vt.satirTemizle(turT) # aga tüm türleri bir arada dönderiyo
tur = vt.tur(turT) # tek türleri dönderiyo 0. index yani
konuP = vt.dictionary(turT)



# print(konuP)
#
# print(tur)
# print(turT)
# print(len(diziIsimleri))
# print(type(tarihVerileri[0]))

raw_data = {

    "isim":diziIsimleri,
    "baslangicT":baslangicT,
    "bitisTarih":bitisTarih,
    "sezon":sezon,
    "tur":tur,
    "konuPuan":konuP,
    "aktorS":aktorS,
    "imdb":imdbRange



}

df = pd.DataFrame(raw_data,columns= ['isim', 'baslangicT', 'bitisTarih', 'sezon', 'tur','konuPuan','aktorS','imdb'])
df.to_csv("kocayurek.csv")
t1 = pd.DataFrame(data=diziIsimleri,index=range(867),columns=["isim"])
t2 = pd.DataFrame(data=baslangicT,index=range(867),columns=["baslangicT"])
t3 = pd.DataFrame(data=bitisTarih,index=range(867),columns=["bitisT"])
t4 = pd.DataFrame(data=sezon,index=range(867),columns=["sezon"])
t5 = pd.DataFrame(data=tur,index=range(867),columns=["tur"])
t6 = pd.DataFrame(data=konuP,index=range(867),columns=["konuPuan"])
t7 = pd.DataFrame(data=aktorS,index=range(867),columns=["oyuncuKadro"])
t8 = pd.DataFrame(data=imdbRange,index=range(867),columns=["imdb"])


print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)
print(t7)
print(t8)


print(type(t1))
