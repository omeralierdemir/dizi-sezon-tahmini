import pandas as pd
import numpy as np


from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix


def test():
    veriler = pd.read_csv("DiziFaktor.csv")
    tur = veriler.iloc[:, 4:5].values  # tarık hocaya sor
    konuPuan = veriler.iloc[:, 5:6].values
    sezon = veriler.iloc[:, 10:11].values
    oyuncuKadroPuann = veriler.iloc[:, 7:8]

    print(oyuncuKadroPuann)

    sc = StandardScaler()
    le = LabelEncoder()# label encoder objesi oluşturuldu
    turNumeric = le.fit_transform(tur[:,0])

    oyuncuKadroPuan = pd.DataFrame(data=oyuncuKadroPuann, index=range(868), columns=["oyuncuKadroPuan"])
    sezonDataF = pd.DataFrame(data=sezon,index=range(868),columns=["sezon"])
    turDataF = pd.DataFrame(data=turNumeric,index=range(868),columns=["tur"])
    konuPuanDataF = pd.DataFrame(data=konuPuan,index=range(868),columns=["konuPuan"])
    birlesikData = pd.concat([turDataF,konuPuanDataF,oyuncuKadroPuan],axis=1)


    x_train,x_test,y_train,y_test = train_test_split(birlesikData,sezonDataF,test_size=0.33,random_state=0) # sezonları dene aga, dataFrame arasındaki farka bak

    X_train = sc.fit_transform(x_train)
    X_test    = sc.transform(x_test)

    knn = KNeighborsClassifier(n_neighbors=3,metric="minkowski")

    knn.fit(X_train,y_train)

    y_pred =knn.predict(X_test)
    print(y_pred)
    print(y_test)

    cs = confusion_matrix(y_test,y_pred)

    print(cs)


def knnHesaplama(turYek,konuPuanları,testKadroPuan):
    veriler = pd.read_csv("DiziFaktor.csv")
    tur = veriler.iloc[:, 4:5].values  # tarık hocaya sor
    konuPuan = veriler.iloc[:, 5:6].values
    sezon = veriler.iloc[:, 10:11].values
    oyuncuKadroPuann = veriler.iloc[:, 7:8]


   # myarray2 = np.ndarray(turYek,dtype=str)
    myarray = np.asarray(turYek)

    sc = StandardScaler()
    le = LabelEncoder()  # label encoder objesi oluşturuldu
    turNumeric = le.fit_transform(tur[:, 0])
    turNumericTest = le.fit_transform(myarray[:,0])

    oyuncuKadroPuan = pd.DataFrame(data=oyuncuKadroPuann,index=range(868),columns=["oyuncuKadroPuan"])
    sezonDataF = pd.DataFrame(data=sezon, index=range(868), columns=["sezon"])
    turDataF = pd.DataFrame(data=turNumeric, index=range(868), columns=["tur"])
    konuPuanDataF = pd.DataFrame(data=konuPuan, index=range(868), columns=["konuPuan"])
    birlesikData = pd.concat([turDataF, konuPuanDataF,oyuncuKadroPuan], axis=1)

    testKadroDataF = pd.DataFrame(data=testKadroPuan, index=range(len(testKadroPuan)), columns=["oyuncuKadroPuan"])
    testTurDataF = pd.DataFrame(data=turNumericTest, index=range(len(turYek)), columns=["tur"])
    testKonuPuanDataF = pd.DataFrame(data=konuPuanları, index=range(len(konuPuanları)), columns=["konuPuan"])
    birlesikDataTest = pd.concat([testTurDataF, testKonuPuanDataF,testKadroDataF], axis=1)

    X_train = sc.fit_transform(birlesikData)
    X_test = sc.fit_transform(birlesikDataTest)

    knn = KNeighborsClassifier(n_neighbors=3, metric="minkowski")

    knn.fit(X_train, sezonDataF)

    y_pred = knn.predict(X_test)
    print(y_pred)




#print(len(turNumeric))
#print(turNumeric)

