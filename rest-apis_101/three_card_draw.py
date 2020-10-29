###Postman generated code:
import requests

url = "https://deckofcardsapi.com/api/deck/new/shuffle/"

payload = {}
headers = {
  'Accept': 'application/json',
}

response = requests.request("GET", url, headers=headers, data = payload)

#print(response.text.encode('utf8'))

###Build on top by grabbing the deck_id and creating:
deck = response.json()
#deck_id = deck['deck_id']
print(deck_id)

url = "https://deckofcardsapi.com/api/deck/" + deck_id + "/draw/?count=3"

response = requests.request("GET", url, headers=headers, data = payload)

three_cards = response.json()

print("You drew the following three cards:")
for card in three_cards['cards']:
    print("   ", card["value"], "of", card["suit"])