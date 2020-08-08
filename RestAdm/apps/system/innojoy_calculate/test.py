# -*- coding: utf-8 -*-


import re
if __name__ == '__main__':
    d = {'a':1 , 'b':2}
    print(sum(d.values()))
    a = sorted(d.items(), key=lambda x: x[1], reverse=False)
    c = {i[0]:i[1] for i in  a}
    print(c)
    before_string = 'aaccd'
    translate_dict = {'aa':'b','cc':'e'}
    translate_dict = dict((re.escape(key), value) for key, value in translate_dict.items())
    pattern = re.compile("|".join(translate_dict.keys()))
    after_string = pattern.sub(lambda m: translate_dict[re.escape(m.group(0))], before_string)
    print(after_string)

