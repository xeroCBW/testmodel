import sys, re
from handler17 import *
from util import *
from rules18 import *

class Parser:

    def __init__(self, handler):
        # 这个是一个类的对象
        self.handler = handler
        self.rules = []
        self.filters = []



    def addRule(self, rule):
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        # 这里会调用 start_document方法 ,生成<html><title>
        self.handler.start('document')
        for block in blocks(file):
            # 记性filter处理
            for filter in self.filters:
                block = filter(block, self.handler)
            # 进行rule 处理
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last: break
        # 这里会调用end_document 方法,生成</html>
        self.handler.end('document')

class BasicTextParser(Parser):
    """
    A specific Parser that adds rules and filters in its constructor.
    """
    def __init__(self, handler):
        # Parser.__init__(self, handler)
        super().__init__(handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())

        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')



def test02():

    # 这个handler 一个对象
    handler = HTMLRenderer()
    parser = BasicTextParser(handler)

    parser.parse(sys.stdin)



def test01():


    print('<html><head><title>...</title><body>')
    title = True

    for block in blocks(sys.stdin):

        block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)

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


def test03():




    pass

if __name__== '__main__':

    # test01()
    # test02()
    test03()
#     python makeup19.py < test_input.txt > test_output.html
