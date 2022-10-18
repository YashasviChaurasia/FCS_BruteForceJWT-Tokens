import base64
import gmpy2
from nslookup import Nslookup 

p="iamyashasvi"
q=list(p.encode('utf8'))#encoded in list 

strn=""

estr=".".join(map(str,q))#made string for easy handling

for i in q:
    strn=strn+chr(i);
print(strn,estr)


x=5;
y=2;
m=20;
result=gmpy2.powmod(x, y, m)
print(result)
# domain="math.iiitd.ac.in"






# set optional Cloudflare public DNS server
import socket

addr1 = socket.gethostbyname(domain)
# addr2 = socket.gethostbyname()
print(addr1)

#1749343240116807117649823543576480140353607282475249
#1911611969616869896888891008001106890111609111180811



