import requests

def init():
    # Postavljanje URL-a za lokalni poslužitelj
    url = 'http://localhost:8081/user/login'

    # Postavljanje podataka koje želite poslati na poslužitelj u obliku rječnika
    data = {'username': 'admin', 'password': 'admin'}

    # Slanje POST zahtjeva
    response = requests.post(url, json=data)

    # Ispisivanje odgovora poslužitelja
    print(response.text)



    # createGame
    url = 'http://localhost:8081/game/createGame'
    data = {
            'gameId': 1,
            'playerUsernames': [
            'player1',
            'player2'
        ]
        }
    bearer_token = response.json()["token"]
    headers = {"Authorization": f"Bearer {bearer_token}"}
    response = requests.post(url, headers=headers, json=data)
    print(response.text)

    # login player1
    url = 'http://localhost:8081/user/login'
    data = {'username': 'player1', 'password': 'sifra1'}
    response = requests.post(url, json=data)
    token_player1 = response.json()["token"]
    print("player1 login:" + response.text)

    # login player1
    data = {'username': 'player2', 'password': 'sifra2'}
    response = requests.post(url, json=data)
    token_player2 = response.json()["token"]
    print("player2 login:" + response.text)


    # join player1
    url = 'http://localhost:8081/game/joinGame'
    headers = {"Authorization": f"Bearer {token_player1}"}
    response = requests.get(url, headers=headers)
    print("player1 join:" + response.text)

    # join player2
    url = 'http://localhost:8081/game/joinGame'
    headers = {"Authorization": f"Bearer {token_player2}"}
    response = requests.get(url, headers=headers)
    print("player2 join:" + response.text)


    # doAction
    ##url = 'http://localhost:8081/game/doAction'
    ##headers = {"Authorization": f"Bearer {token_player1}"}
    ##data = {
    ##            'action': 'P-K-0-0'
    ##        }
    ##requests.post(url, headers=headers, json = data)

    



