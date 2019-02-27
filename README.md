
Bu proje yeni çıkmış bir dizinin oyuncu kadrosu, başlangıç yılını, dizinin tür verilerini  alarak dizinin sektörde tutulmasını puanlamakta çıktı olarak 
olgun(2 yıl ve üzerinde yayında kalacak anlamına gelmektedir), başarılı(2 yıl  yayında kalacak anlamına gelmektedir) başarısız(1 yıl  veya daha az yayında kalacağı anlamına gelmektedir) sonucunu üretmektedir.
Sistem KNN algoritması üzerine inşa edilmiştir. Gerekli öğrenme verisi DiziFaktor.csv dosyasında bulunmaktadır. Bu verilerin eldesi internetten veri çekme sonucu elde edilmiştir. 
Sistemin başarısının testi için KNN.py dosyasındaki test() metodu çalıştırılabilir, elde edilen başarının % 70 olduğu görülebilinir. Öğrenme verileri aynı formatta kalmak şartı ile genişletilebilir.

Sistem dizilerin oyuncu kadrosuna, türüne ve konusuna göre bir puanlama sistemi oluşturarak dizinin sektördeki durumunu tahmin etmeye çalışmaktadır.


sistemin çalışması için eklenmesi gereken kütüphaneler:

------> bs4
------> requests
------> sklearn.preprocessing
------> sklearn.model_selection
------> sklearn.neighbors
------> sklearn.metrics