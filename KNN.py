import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix


def test():
    veriler = pd.read_csv("kocayurekk.csv")
    tur = veriler.iloc[:,6:7].values  # tarık hocaya sor
    konuPuan = veriler.iloc[:,7:8].values
    sezon = veriler.iloc[:,5:6].values

    sc = StandardScaler()
    le = LabelEncoder()# label encoder objesi oluşturuldu
    turNumeric = le.fit_transform(tur[:,0])





    sezonDataF = pd.DataFrame(data=sezon,index=range(868),columns=["sezon"])
    turDataF = pd.DataFrame(data=turNumeric,index=range(868),columns=["tur"])
    konuPuanDataF = pd.DataFrame(data=konuPuan,index=range(868),columns=["konuPuan"])
    birlesikData = pd.concat([turDataF,konuPuanDataF],axis=1)


    x_train,x_test,y_train,y_test = train_test_split(birlesikData,sezonDataF,test_size=0.33,random_state=0) # sezonları dene aga, dataFrame arasındaki farka bak

    X_train = sc.fit_transform(x_train)
    X_test    = sc.transform(x_test)

    knn = KNeighborsClassifier(n_neighbors=5,metric="minkowski")

    knn.fit(X_train,y_train)

    y_pred =knn.predict(X_test)
    print(type(x_test))

    cs = confusion_matrix(y_test,y_pred)
    print(cs)
    print()




def knnHesaplama(turYek,konuPuanları):
    veriler = pd.read_csv("kocayurekk.csv")
    tur = veriler.iloc[:, 6:7].values  # tarık hocaya sor
    konuPuan = veriler.iloc[:, 7:8].values
    sezon = veriler.iloc[:, 5:6].values

    sc = StandardScaler()
    le = LabelEncoder()  # label encoder objesi oluşturuldu
    turNumeric = le.fit_transform(tur[:, 0])
    turNumericTest = le.fit_transform(turYek)

    sezonDataF = pd.DataFrame(data=sezon, index=range(868), columns=["sezon"])
    turDataF = pd.DataFrame(data=turNumeric, index=range(868), columns=["tur"])
    konuPuanDataF = pd.DataFrame(data=konuPuan, index=range(868), columns=["konuPuan"])
    birlesikData = pd.concat([turDataF, konuPuanDataF], axis=1)


    #testSezonDataF =  pd.DataFrame(data=sezon, index=range(867), columns=["sezon"])
    testTurDataF = pd.DataFrame(data=turNumericTest, index=range(len(turYek)), columns=["tur"])
    testKonuPuanDataF = pd.DataFrame(data=konuPuanları, index=range(len(konuPuanları)), columns=["konuPuan"])
    birlesikDataTest = pd.concat([testTurDataF, testKonuPuanDataF], axis=1)

    X_train = sc.fit_transform(birlesikData)
    X_test = sc.transform(birlesikDataTest)

    knn = KNeighborsClassifier(n_neighbors=5, metric="minkowski")

    knn.fit(X_train, sezonDataF)

    y_pred = knn.predict(X_test)
    print(y_pred)




#print(len(turNumeric))
#print(turNumeric)

test()