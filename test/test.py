import requests
from bs4 import BeautifulSoup
import urllib3


response = requests.get('https://www.proveyourworth.net/level3')

def param(hash):
    name = {
        'statefulhash': hash,
        'name': 'Joel Cedeño'
    }



soup = BeautifulSoup(response.text, 'lxml')

hash = soup.body.form.div.input['value']

r = requests.post('https://www.proveyourworth.net/level3', name)

s = requests.Session()
s.post('https://www.proveyourworth.net/level3/start', name)
r2 = s.get('https://localhost/profile_data.json', ...)
print(r2)