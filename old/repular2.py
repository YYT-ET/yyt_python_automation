import requests
import re
from requests.exceptions import RequestException

# url = 'http://service.shmetro.com/czxx/index.htm'
#获取当前网页方法
def get_url(url):
 try:
    response = requests.get(url)
    if response==200:
        return response.text
    return None
 except RequestException:
     return None

#方法
def get_sp(html):
    pattern=re.compile('<div class="name" id="lineName">.*?<a class onclick=".*?".*?>(.*?)</a>.*?</div>',re.S)
    result=re.findall(pattern,html)
    for item in result:
        yield{
            'station':item[0]
        }
    print(result)

def main():
    url = 'http://service.shmetro.com/czxx/index.htm'
    html=get_url(url)
    for item in get_sp(html):
        print(item)


if __name__=='__main__':
        main()
