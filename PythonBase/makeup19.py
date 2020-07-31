import re,sys
from rules18 import *
from handler17 import *
from util import *


class Parser:

    '''
    读取文本文件,应用规则并控制处理程序的解析器
    '''

    def __init__(self,handler):

        self.handler = handler
        self.rules = []
        self.filters = []

    def addRule(self,rule):
        self.rules.append(rule)
    def addFilter(self,pattern,name):
        def filter(block,handler):
            return re.sub(pattern,handler.sub(name),block)

        # 这里直接调用 filter方法
        self.filters.append(filter)

    def parse(self,file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block,self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block,self.handler)
                    if last:break
        self.handler.end('document')



class BasicTextParser(Parser):

    def __init__(self,handler):
        Parser.__init__(self,handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())

        # 对于 *_* 这种进行加粗
        self.addFilter(r'\*(.+?)\*','emphasis')
        # \. 是. 的转义符号
        self.addFilter(r'(http://[\.a-zA-Z/])','url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)','mail')


def test01():

    print('<html><head><title>...</title><body>')
    title = True
    for block in blocks(sys.stdin):
        print('------')
        block = re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)
        if title:
            print('<h1>')
            print(block)
            print('</h1>')
            title = False
        else:
            print('<p>')
            print(block)
            print('</p>')

    print('</body></html>')


def test02():

    handler = HTMLRender()
    parser = BasicTextParser(handler)
    parser.parse(sys.stdin)

    # with open('test_input.txt') as f:
    #     res = f.read()
    #     print(res)



if __name__ == '__main__':

    # test01()
    test02()




#     运行代码
#   python makeup19.py < test_input.txt > test_output.html





