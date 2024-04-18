from bs4 import BeautifulSoup
import requests

url = 'https://alifshop.uz/ru/categories/vse-noutbuki?gad_source=1&gclid=EAIaIQobChMIlNqZh6_GhQMVb0ZBAh0F5AsOEAAYASAAEgKK8PD_BwE'
data = requests.get(url).text

product_data = []
soup = BeautifulSoup(data,'html.parser')
main_block = soup.find('div', class_='grid')
block = main_block.find_all('div', class_='grid-cols-1')
for product in block:
    image = product.find('img', class_='h-full')['data-src']
    name = product.find('p', class_='text-sm').get_text()
    price = product.find('p', class_='text-grey-400').get_text()
    mounth = product.find('span',class_='bg-primary-100').get_text()

    product_data.append({
        'noutbuk_rasmi':image,
        'noutbuk_nomi':name,
        'noutbuk_narxi':price,
        'noutbuk_oy':mounth
    })
print(product_data)
