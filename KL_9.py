"""
import requests
response = requests.get('https://httpbin.org/get')
print(type(response.content))
print(response.content.decode("utf-8"))
print(response.text)
response = requests.post('https://httpbin.org/post', data='TEST DATA 123', headers={'h1': 'Test title'})
print(response.text)
"""
import requests
result = []
response = requests.get('https://coinmarketcap.com/')
response_text = response.text
response_parse = response_text.split('<span>')
for element1 in response_parse:
    if element1.startswith('$'):
        for element2 in element1.split('</span>'):
            if element2.startswith('$') and element2[1].isdigit():
                result.append(element2)
bitcoin_exchange_rate = result[0]
print(bitcoin_exchange_rate)