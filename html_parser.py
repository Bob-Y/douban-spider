from bs4 import BeautifulSoup
import re

class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='GBK') #创建一个beautifulsoup对象
        new_urls = self._get_new_urls(soup) #调用内部方法提取url
        new_data = self._get_new_data(page_url, soup) #调用内部方法提取有价值数据

        return new_urls, new_data

    def _get_new_urls(self, soup):
        new_urls = set()
        #同样喜欢区域：<div id="db-rec-section" class="block5 subject_show knnlike">
        recommend = soup.find('div', class_='block5 subject_show knnlike') #先找到推荐书籍的区域
        #<a href="https://book.douban.com/subject/11614538/" class="">程序员的职业素养</a>
        links = recommend.find_all('a', href=re.compile(r"https://book\.douban\.com/subject/\d+/$")) #在推荐区域中寻找所有含有豆瓣书籍url的结点
        for link in links: 
            new_url = link['href'] #从结点中提取超链接，即url
            new_urls.add(new_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        #url
        res_data['url'] = page_url
        # <span property="v:itemreviewed">代码大全</span>
        res_data['bookName'] = soup.find('span', property='v:itemreviewed').string
        # <strong class="ll rating_num " property="v:average"> 9.3 </strong>
        res_data['score'] = soup.find('strong', class_='ll rating_num ').string
        '''
        <div id="info" class="">
            <span>
              <span class="pl"> 作者</span>:
              <a class="" href="/search/Steve%20McConnell">Steve McConnell</a>
            </span><br>
            <span class="pl">出版社:</span> 电子工业出版社<br>
            <span class="pl">出版年:</span> 2007-8<br>
            <span class="pl">页数:</span> 138<br>
            <span class="pl">定价:</span> 15.00元<br>
        </div>
        '''
        info = soup.find('div', id='info')
        try: #有的页面信息不全
            res_data['author'] = info.find(text=' 作者').next_element.next_element.string
            res_data['publisher'] = info.find(text='出版社:').next_element
            res_data['time'] = info.find(text='出版年:').next_element
            res_data['price'] = info.find(text='定价:').next_element
            res_data['intro'] = soup.find('div', class_='intro').find('p').string
        except:
            return None
        if res_data['intro'] == None:
            return None

        return res_data