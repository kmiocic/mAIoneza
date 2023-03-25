import requests
import multiprocessing

token_player1 = 'eyJhbGciOiJIUzUxMiJ9.eyJ1c2VybmFtZSI6InBsYXllcjEiLCJwYXNzd29yZCI6InNpZnJhMSJ9.4Me9JQvkH_PQoBGDu1UBlIWqnDawhpDFAMxN35HYcz33tQdvIRALg6DxxmIc4fipREJw6RnlI__ANtm_dTFicQ'
token_player2 = 'eyJhbGciOiJIUzUxMiJ9.eyJ1c2VybmFtZSI6InBsYXllcjIiLCJwYXNzd29yZCI6InNpZnJhMiJ9.dgNpo4HhxuoqihuSrGMsS85aMvxTv4PLJbAjuOLx3KjW6VCMtZA0cmd4xAoEGvD9Hn5RRIgfEpBkQov8LNuZFw'

def init():
    # Postavljanje URL-a za lokalni poslužitelj
    url = 'http://localhost:8080/user/login'

    # Postavljanje podataka koje želite poslati na poslužitelj u obliku rječnika
    data = {'username': 'admin', 'password': 'admin'}

    # Slanje POST zahtjeva
    response = requests.post(url, json=data)

    # Ispisivanje odgovora poslužitelja
    print(response.text)

    

    # createGame
    url = 'http://localhost:8080/game/createGame'
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
    url = 'http://localhost:8080/user/login'
    data = {'username': 'player1', 'password': 'sifra1'}
    response = requests.post(url, json=data)
    token_player1 = response.json()["token"]
    #print("player1 login:" + response.text)

    # login player1
    data = {'username': 'player2', 'password': 'sifra2'}
    response = requests.post(url, json=data)
    token_player2 = response.json()["token"]
    #print("player2 login:" + response.text)




    p1 = multiprocessing.Process(target=joinPlayer, args=(1,))
    p2 = multiprocessing.Process(target=joinPlayer, args=(2,))

    # start the processes
    p1.start()
    p2.start()

    # wait for the processes to finish
    p1.join()
    p2.join()



    # # join player1
    # url = 'http://localhost:8080/game/joinGame'
    # headers = {"Authorization": f"Bearer {token_player1}"}
    # response = requests.get(url, headers=headers)
    # #print("player1 join:" + response.text)

    # # join player2
    # url = 'http://localhost:8080/game/joinGame'
    # headers = {"Authorization": f"Bearer {token_player2}"}
    # response = requests.get(url, headers=headers)
    # #print("player2 join:" + response.text)

    # print("prije prvog poteza")

    # # doAction
    # url = 'http://localhost:8080/game/doAction'
    # headers = {"Authorization": f"Bearer {token_player2}"}
    # data = {
    #             'action': 'P-K-0-0'
    #         }
    # response = requests.post(url, headers=headers, json = data)
    # print(response.text)
    
    # print("prvi potez")

    # # doAction
    # url = 'http://localhost:8080/game/doAction'
    # headers = {"Authorization": f"Bearer {token_player2}"}
    # data = {
    #             'action': 'P-N-0-1'
    #         }
    # response = requests.post(url, headers=headers, json = data)
    # print(response.text)

    # print("drugi potez")


    #  # doAction
    # url = 'http://localhost:8080/game/doAction'
    # headers = {"Authorization": f"Bearer {token_player2}"}
    # data = {
    #             'action': 'P-N-0-1'
    #         }
    # response = requests.post(url, headers=headers, json = data)
    # print(response.text)


def getPlayerToken(player):
    if player == 1:
        return token_player1
    else:
        return token_player2
    
def joinPlayer(player):
    url = 'http://localhost:8080/game/joinGame'
    headers = {"Authorization": f"Bearer {getPlayerToken(player)}"}
    response = requests.get(url, headers=headers)
    #print(response.text + "uspio igrac" + str(player))

    



