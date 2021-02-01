import json
import requests

# API TOTAL
url = "https://api.kawalcorona.com/indonesia"
response = requests.get(url)
data = response.json()
for covid in data:
    positif = (f"{covid['positif']}")
    sembuh = (f"- {covid['sembuh']}")
    meninggal = (f"- {covid['meninggal']}")
    dirawat = (f"- {covid['dirawat']}")
# END OF API TOTAL

# # API PROVINSI
url1 = "https://indonesia-covid-19.mathdro.id/api/provinsi"
response1 = requests.get(url1)
data1 = response1.json()
for covid1 in data1['data']:
    provinsi = (f"provinsi : {covid1['provinsi']}")
    posi_provinsi = (f"- kasus positif : {covid1['kasusPosi']}")
    semb_provinsi = (f"- kasus sembuh : {covid1['kasusSemb']}")
    meni_provinsi = (f"- kasus meninggal : {covid1['kasusMeni']}")
# END OF API PROVINSI
    print(provinsi)
    print(posi_provinsi)
    print(semb_provinsi)
    print(meni_provinsi + "\n")
print("Total kasus " + positif)
print("Total kematian " + meninggal)
