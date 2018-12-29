
import VeriTemizleme as vt

test = "omer,o2,4"
a,b,c = test.split(",")
liste = [1,2,3,4,5,6]
aktor = [['Çagatay Ulusoy', 'Ayça Aysin Turan', 'Hazar Ergüçlü', 'Okan Yalabik'], ['Kivanç Tatlitug', 'Elçin Sangu', 'Alperen Duymaz', 'Melisa Pamuk'],['Kivanç Tatlitug', 'Elçin Sangu', 'Alperen Duymaz', 'Melisa Pamuk']]
dizi = ['(2018– )', '(2018– )', '(2017– )', '(2016–2017)', '(2014– )', '(2013–2015)', '(2009–2011)', '(2011–2014)', '(2018– )', '(2017–2018)', '(2014)', '(2016– )', '(2011–2012)', '(2011–2014)', '(2011–2013)', '(2008–2011)', '(2017–2018)', '(2015–2017)', '(2015–2017)', '(2017–2018)', '(2017– )', '(2016–2018)', '(2015–2017)', '(2017– )', '(2018– )', '(2017–2018)', '(2006– )', '(2017– )', '(2017– )', '(2012–2015)', '(2017)', '(2018– )', '(2013–2016)', '(2018)', '(2010–2013)', '(2018– )', '(2018)', '(2018– )', '(2011– )', '(2017–2018)', '(2016–2017)', '(2015–2017)', '(2016–2017)', '(2018– )', '(2015–2016)', '(2010–2012)', '(2018)', '(2012)', '(2007– )', '(2016)']

deneme = ["\n omer ali","\nomer ali","\nom  er alidd","\no me  r alsdadi"]

imdb = [1,2,3]

#print(a)
#print(vt.tarihBelirleme(dizi))

aaktor = [["omer ali", 4,0]]

vt.aktorPuan(imdb,aktor)

liste.extend("7")
print(liste)
