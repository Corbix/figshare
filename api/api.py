import requests
import json

def GET(request):
    response = requests.get(request)
    return (response.status_code, json.dumps(response.json(), indent=1)) # returnez o tupla ce contine codul HTTP status si textul din JSON-ul raspunsului


def POST(url,data):
    r = requests.post(url, data)
    return r.text


#print(GET("https://api.figshare.com/v2/articles?page_size=10&order=published_date&order_direction=desc")[1]) # public articles

#print(GET("https://api.figshare.com/v2/articles/13482372")[1]) # article details

# Token="01b151746e51a745289f454f1cc620ecd39150077d135928cea91e87aa96554f7cc446836bf064ce6887b4c49303ca5c3c8ef09185bdb834e9fb1cee4d682e64"

headers={"Host": "api.figshare.com", "Authorization": "token 01b151746e51a745289f454f1cc620ecd39150077d135928cea91e87aa96554f7cc446836bf064ce6887b4c49303ca5c3c8ef09185bdb834e9fb1cee4d682e64"} # datele de autentificare

print (requests.get("https://api.figshare.com/v2/account/articles?page_size=10",headers)) # private articles
