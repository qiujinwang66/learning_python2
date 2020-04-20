import requests
data = {'name': 'test', 'age': 18}
r = requests.get("https://www.baidu.com")
print(r.text)
print(r.status_code)
print(r.cookies)
r = requests.get("http://httpbin.org/get", params=data)
print(r.text)
r = requests.post("http://httpbin.org/post", data=data)
print(r.text)
r = requests.get('https://www.zhihu.com/explore')
print(r.text)

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}
r = requests.get('https://www.zhihu.com/explore', headers=headers)

print(r.text)
