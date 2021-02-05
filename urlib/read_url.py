
import urllib.request
import urllib.parse

url = "https://pythonprogramming.net/"

values = {'q':'basic',
          'submit': 'search'
          }

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')

req = urllib.request.Request(url, data)
res = urllib.request.urlopen(req)
res_data = res.read()
print(res_data)