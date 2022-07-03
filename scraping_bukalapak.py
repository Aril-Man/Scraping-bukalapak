
import csv
import keyword
import re
import requests

# ambil URL Pada web
URL = 'https://api.bukalapak.com/multistrategy-products'

# Input keword yang akan dicari
keyword = str(input('Keyword: '))

# Menulis header ke file CSV
write = csv.writer(open('hasil_scraping_bukalapak/hasil_scraping_{}.csv'.format(keyword), 'w', newline=''))
header = ['No','Name', 'Price', 'Kondisi', 'Stok']
write.writerow(header)

# untuk menghitung jumlah data yang akan di scraping
count = 0

# loop untuk ambil data tiap halaman
for page in range(1, 40):
    # Parameter untuk mengambil data dari API
    param = {
        'keywords': keyword,
        'limit': '50',
        'offset': '50',
        'facet': True,
        'page': page,
        'shouldUseSeoMultistrategy': False,
        'access_token': 't49fDHDg0mSpT2IRssV0GEBp9A5YGFtvFphJv0OlXS56UQ'
    }

    # variabel res unruk ambil data dari API 
    res = requests.get(URL, params=param).json()

    # print(res.status_code)

    products = res['data']
    
    # looping untuk mengambil data dari API
    for p in products:
        name = p['name']
        price = p['original_price']
        condition = p['condition']
        stock = p['stock']
        count += 1
        
        print('No :', count, '\nNama Produk:', name, '\nHarga:', price, '\nKondisi:', condition, '\nStok:', stock)
        
        # Memasukan data yang udah di ambil ke dalam file CSV
        write = csv.writer(open('hasil_scraping_bukalapak/hasil_scraping_{}.csv'.format(keyword), 'a', newline=''))
        header = [count ,name, price, condition, stock]
        write.writerow(header)