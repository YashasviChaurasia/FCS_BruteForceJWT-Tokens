from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
url = "https://crt.sh/?q="
link="iiitd.edu.in"
url=url+link
page=urlopen(url)
html_bytes=page.read()
html=html_bytes.decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
# gfg=BeautifulSoup(soup.get_text("td"),"html.parser")
# ch=gfg.find_all('iiitd.edu.in')
table = soup.findAll('table')[1]
values=[]

# print(tr)
# pat=re.compile("iiitd.edu.in$")
tr = table.findAll(['tr'])
print(tr)


file = open("subdomains.txt", "w")

file.close()
print("Success")
