import urllib.request

urls = [ 'https://api.saveadd.com.br/d/ping', 'https://api.saveadd.com.br/s/ping', 'https://api.saveadd.com.br/p/ping' ]
resp = "Resposta:"

for url in urls:
    web = urllib.request.urlopen(url)
    data = web.read()
    resp += str("\n") + url + " :: " + str(data)

print(resp)