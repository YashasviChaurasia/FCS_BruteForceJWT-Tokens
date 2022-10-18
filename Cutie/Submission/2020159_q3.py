import socket
from openpyxl import load_workbook
book=load_workbook("iiitd.xlsx")
sheet=(book.active)
rows=sheet.rows
# headers=next(rows)
header=[cell.value for cell in next(rows)]
# print(header)

all_rows=[]
for row in rows:
    data={}
    for hostname,cell in zip(header,row):
        data[hostname]=cell.value
    # print(data)
    all_rows.append(data)

print(len(all_rows))
file = open("subdomains.txt", "w")

for ib in range(len(all_rows)):
    try:
        hn=all_rows[ib].get("Hostname")
        addr1 = socket.gethostbyname(hn)
        print(hn,addr1)
        list=[hn,addr1,"\n"]
        # print(list)
        listToStr = ' '.join(map(str, list))

        file.write(listToStr)
    except:
        print("Could Not Find Private IP")
        continue

print("Thank you")
file.close()