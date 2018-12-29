def satirTemizle(liste):
    kopru = []
    for i in liste:


        deg = i.replace("\n","")
        kopru.append(deg.replace(" ", ""))



    return kopru


def tarihBelirleme(tarihList):
    baslangicT = []
    bitisT = []

    bitT = "a"
    for i in tarihList:

        kopru = i.replace("(", "")
        kopru = kopru.replace(")", "")
        if("–" in i):

            basT,bitT = kopru.split("–")

            if(bitT == ' ' and 2018-int(basT) >= 10):

                bitT =str(int(basT) + 4)

            elif(bitT == ' ' and 2018-int(basT) < 10):

                bitT =str( int(basT) + (2018 - int(basT)))

        else:

            basT,bitT = kopru,kopru


        baslangicT.append(basT)
        bitisT.append(bitT)

        print(len(baslangicT),len(bitisT))
    return  baslangicT,bitisT


def tur(dizi):

    kopru = []
    for i in dizi:
        a= i.split(",")

        kopru.append(a[0])


    return kopru

def aktorPuan(imdbList,oyuncuList):

    aktor = []
    aktorler = []
    count = 0

    for i in range(len(oyuncuList)):
        for j in range(len(oyuncuList[i])):

            if(oyuncuList[i][j] not in aktor):

                aktor.append(oyuncuList[i][j])
                aktorler.append([oyuncuList[i][j],0,0])
                aktorler[count][1] = imdbList[i]
                aktorler[count][2] = 1

                count = count + 1


            else:
                count2 = aktor.index(oyuncuList[i][j])
                aktorler[count2][1] = aktorler[count2][1] + imdbList[i]
                aktorler[count2][2] = aktorler[count2][2] + 1

