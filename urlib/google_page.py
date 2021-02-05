import urllib.request


try:
    url = 'https://www.google.com/search?q=test'
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'

    res = urllib.request.Request(url, headers=headers)

    res = urllib.request.urlopen(res)
    res_data = res.read()
    print(res_data)

except Exception as e:
    print(str(e))


file = open("google.txt", 'w')
file.write(str(res_data))
file.close()



