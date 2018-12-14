# coding=gbk
import urllib.request, urllib.parse

# 1. urlopen ʹ��
url = 'http://localhost:5000'  # ��ҳ��ַ
dic = {  # ������
    'name': 'domain',
    'age': 18
}
data = bytes(urllib.parse.urlencode(dic), encoding='utf-8')
response = urllib.request.urlopen(url)
print(response.read().decode('utf-8'))

# 2. Request
url = 'http://localhost:5000'  # ��ҳ��ַ
dic = {  # ������
    'name': 'domain',
    'age': 18
}
headers = {
    'User-Agent':'Mozilla/4.0(compatible;MSIE 5.5; Windows NT)',
}
data = bytes(urllib.parse.urlencode(dic), encoding='utf-8')
req=urllib.request.Request(url=url,headers=headers,method='GET')
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))
