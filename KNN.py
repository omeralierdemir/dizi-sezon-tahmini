import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

veriler = pd.read_csv("kocayurekk.csv")
tur = veriler.iloc[:,6:7].values  # tarık hocaya sor
konuPuan = veriler.iloc[:,7:8].values
sezon = veriler.iloc[:,5:6].values

sc = StandardScaler()
le = LabelEncoder()# label encoder objesi oluşturuldu
turNumeric = le.fit_transform(tur[:,0])





sezonDataF = pd.DataFrame(data=sezon,index=range(867),columns=["sezon"])
turDataF = pd.DataFrame(data=turNumeric,index=range(867),columns=["tur"])
konuPuanDataF = pd.DataFrame(data=konuPuan,index=range(867),columns=["konuPuan"])
birlesikData = pd.concat([turDataF,konuPuanDataF],axis=1)


x_train,x_test,y_train,y_test = train_test_split(birlesikData,sezonDataF,test_size=0.33,random_state=0) # sezonları dene aga, dataFrame arasındaki farka bak

X_train = sc.fit_transform(x_train)
X_test    = sc.transform(x_test)

knn = KNeighborsClassifier(n_neighbors=5,metric="minkowski")

knn.fit(X_train,y_train)

y_pred =knn.predict(X_test)
print(type(y_pred))

cs = confusion_matrix(y_test,y_pred)
print(cs)
print()



#print(len(turNumeric))
#print(turNumeric)