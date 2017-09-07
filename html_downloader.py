import urllib.request
import urllib.error
from urllib import error

class HtmlDownloader(object):
    def download(self, url):
        global response
        if url is None:
            return None
        try:
            request = urllib.request.Request(url)
            request.add_header('user-agent', 'Mozilla/5.0') #添加头信息，伪装成Mozilla浏览器
            response = urllib.request.urlopen(request) #访问这个url
        except error.URLError as e: #如果出错则打印错误代码和信息
            if hasattr(e,"code"):
                print (e.code) #错误代码，如403
            if hasattr(e,"reason"):
                print (e.reason) #错误信息，如Forbidden
        if response.getcode() != 200: #200表示访问成功
            return None
        return response.read() #返回该url的html数据
