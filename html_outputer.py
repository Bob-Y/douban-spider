class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('GoodBooks.html', 'w')

        fout.write('<html>')
        fout.write('<meta charset="GBK">')  # 告诉浏览器是utf-8编码
        fout.write('<title>GoodBooks_moverzp</title>')
        fout.write('<body>')

        for data in self.datas:
            print (data['bookName'], data['score'], data['author'], data['price'], data['publisher'], data['time'])
            print(data['intro'])
            fout.write("<h2><a href='%s' target=_blank>%s</a></h2>" % (data['url'].encode('utf-8').decode(encoding='utf-8'), data['bookName'].encode('utf-8').decode(encoding='utf-8')))
            fout.write('<table border="1">')
            fout.write('<tr><td>评分：</td><td><b>%s</b></td></tr>' % data['score'].encode('utf-8').decode(encoding='utf-8'))
            fout.write('<tr><td>作者：</td><td>%s</td></tr>' % data['author'].encode('utf-8').decode(encoding='utf-8'))
            fout.write('<tr><td>定价：</td><td>%s</td></tr>' % data['price'].encode('utf-8').decode(encoding='utf-8'))
            fout.write('<tr><td>出版社：</td><td>%s</td></tr>' % data['publisher'].encode('utf-8').decode(encoding='utf-8'))
            fout.write('<tr><td>出版时间：</td><td>%s</td></tr>' % data['time'].encode('utf-8').decode(encoding='utf-8'))
            fout.write('</table>')
            fout.write('<p>%s' % data['intro'].encode('utf-8').decode(encoding='utf-8'))
            fout.write('</p><hr>')  # 加上分割线

        fout.write('</body>')
        fout.write('</html>')