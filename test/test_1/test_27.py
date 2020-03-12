import requests

proxies = {"http":"https://183.147.214.86:8118"}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
url = 'https://icanhazip.com/'
res = requests.get(url, headers = headers, proxies = proxies)
res.encoding='utf-8'
print(res.status_code)
print(res.text)