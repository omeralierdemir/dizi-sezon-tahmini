from bs4 import BeautifulSoup
import requests

#htmltxt = "<p>Hello World!</p>"

'''
mytxt = """
<h1>Hello World</h1>
<p>This is a <a href="http://example.com">link</a></p>
"""

soup = BeautifulSoup(mytxt, 'html.parser')
print(soup.find('a').text)
'''

url = 'https://www.imdb.com/search/title?title_type=tv_series&countries=tr&ref_=adv_prv'
reps = requests.get(url)
soup = BeautifulSoup(reps.content,'html.parser')

contentVerileri = soup.find_all('div',{"class":"lister-item-content"})
counter = 0

for i in contentVerileri:
    baslikVerileri = i.find('h3')
    diziIsimleri = baslikVerileri.find('a').text
    tarihVerileri = baslikVerileri.find('span',{"class":"lister-item-year text-muted unbold"}).text
    #print(tarihVerileri)
    print(diziIsimleri)
    counter = counter + 1
for urlDeger in range(1,1301,50):

    if(urlDeger == 1):
        url = "https://www.imdb.com/search/title?title_type=tv_series&countries=tr&sort=year,asc&ref_=adv_prv"

    else:
        url = "https://www.imdb.com/search/title?title_type=tv_series&countries=tr&sort=year,asc&start=" + str(urlDeger) +"&ref_=adv_nxt"
    reps = requests.get(url)
    soup = BeautifulSoup(reps.content,'html.parser')
    ustSayfaVerileri = soup.find_all('div',{"class":"lister-item-content"})
    for i in ustSayfaVerileri:
        baslikVerileri2 = i.find('h3')
        diziIsimleri2 = baslikVerileri2.find('a').text
       # print(diziIsimleri2)
        counter = counter +1

print(counter)
    #print(diziIsimleri)