def satirTemizle(liste):
    kopru = []
    for i in liste:
        deg = i.replace("\n", "")

        deg = deg.replace(" ", "")
        deg = deg.split(",")
        kopru.append(deg)


    return kopru


def sezonHesapla(basT,bitT):

    sezon = []

    for i in range(len(basT)):


        sezon.append(int(bitT[i]) - int(basT[i]) + 1)
    return sezon




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

        print(len(baslangicT), len(bitisT))
    return baslangicT, bitisT


def tur(dizi):
    kopru = []
   # for i in dizi:

    for i in range(len(dizi)):

        a = dizi[i][0]

        kopru.append(a)

    return kopru


def aktorPuan(imdbList, oyuncuList):
    aktor = []
    aktorler = []
    count = 0
    sonuc = []

    for i in range(len(oyuncuList)):
        for j in range(len(oyuncuList[i])):

            if (oyuncuList[i][j] not in aktor):

                aktor.append(oyuncuList[i][j])
                aktorler.append([oyuncuList[i][j], 0, 0])
                aktorler[count][1] = float(imdbList[i])
                aktorler[count][2] = 1

                count = count + 1


            else:
                count2 = aktor.index(oyuncuList[i][j])  # başkan ortalama almamışsın
                aktorler[count2][1] = aktorler[count2][1] + float(imdbList[i])
                aktorler[count2][2] = aktorler[count2][2] + 1

    # for k in range(len(aktorler)):
    #
    #     aktorler[k][1] = (aktorler[k][1] / aktorler[k][2])

    return aktorler


def dictionary(turList):
    sonuc = []
    flag = 0
    count = 0
    toplam = 0
    sozluk = {"action": 16, "fantasy": 14, "sci-fi": 12, "drama": 18, "thriller": 16, "mystery": 14, "crime": 15,
              "adventure": 17, "comedy": 16, "romance": 16, "history": 8, "war": 16, "family": 15, "sport": 12,
              "music": 6, "talk-show": 14, "biography": 6, "horror": 10, "reality-tv": 12, "short": 6, "game-show": 12,
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


