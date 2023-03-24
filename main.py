import requests

# Postavljanje URL-a za lokalni poslužitelj
url = 'http://localhost:8081/user/login'

# Postavljanje podataka koje želite poslati na poslužitelj u obliku rječnika
data = {'username': 'admin', 'passwork': 'admin'}

# Slanje POST zahtjeva
response = requests.post(url, data=data)

# Ispisivanje odgovora poslužitelja
print(response.text)
