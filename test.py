from urllib import request
from bs4 import BeautifulSoup
import time
a=''
c='.html'
for i in range(1,33):
	url=a+str(i)+c
	req=request.Request(url)
	response=request.urlopen(req)
	html=response.read()
	soup=BeautifulSoup(html,'lxml')
	soup_texts = soup.find('ul', type = '1')
	for link in soup_texts.children:
		if link != '\n':
			try:
				f=open(link.text+'.txt','w',encoding='utf-8')
			except FileNotFoundError:
				continue
			except PermissionError:
				continue
			except OSError:
				continue
			urltemp=link.a.get('href')
			urltemp=''+urltemp
			reqtemp=request.Request(urltemp)
			responsetemp=request.urlopen(reqtemp)
			htmltemp=responsetemp.read()
			souptemp=BeautifulSoup(htmltemp,'lxml')
			soup_textstemp=souptemp.find('div', id = 'content')
			download_soup_texts=soup_textstemp.text
			f.write(download_soup_texts)
			f.close()
			print(i)
			print('\n')
			print('ok')
