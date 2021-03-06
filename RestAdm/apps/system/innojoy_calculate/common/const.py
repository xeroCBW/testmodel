# -*- coding: utf-8 -*-

import os
# 读取文件的地址
BASE_PATH = r'f:\test2.xls'

# 保存的列名:申请日期，申请人，发明人，分类号
APPLY_DATE = 'apply_date'
APPLICANT = 'applicant'
INVENTOR = 'inventor'
CLASS_NBR = 'class_nbr'

# 树状结构json文件以js的方式保存在项目路径下lib/js
#该文件的上上级目录
root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

JSON_PATH = root_path + '\\lib\\js\\test1.js'

"""
原始数据sheet1(从0开始计数)，申请日对应的为第2列，
 申请人为第6列，发明人为第8列，分类号为第10列
 """
BASE_MAP = {'SHEET_NBR': 0,
            APPLY_DATE: 2,
            APPLICANT: 6,
            INVENTOR: 8,
            CLASS_NBR: 10
            }


USELESS_STRING_LIST = ['有限公司',
                       '技术',
                       '显示',
                       '研究所',
                       '科技',
                       '股份',
                       '集团',
                       '公司',
                       '上饶',
                       '三沙',
                       '六安',
                       '文昌',
                       '铜川',
                       '合肥',
                       '钦州',
                       '大兴安岭',
                       '酒泉',
                       '昌都',
                       '邵阳',
                       '海口',
                       '乌海',
                       '六盘水',
                       '枣庄',
                       '湛江',
                       '厦门',
                       '毕节',
                       '三亚',
                       '安庆',
                       '保定',
                       '呼伦贝尔',
                       '汕头',
                       '保山',
                       '香港',
                       '昆明',
                       '珠海',
                       '三明',
                       '贵阳',
                       '黄山',
                       '黑河',
                       '达州',
                       '牡丹江',
                       '玉溪',
                       '天门',
                       '滁州',
                       '丽水',
                       '淮北',
                       '防城港',
                       '南京',
                       '日照',
                       '宜昌',
                       '长春',
                       '芜湖',
                       '晋城',
                       '娄底',
                       '长沙',
                       '玉树',
                       '曲靖',
                       '池州',
                       '嘉峪关',
                       '湘潭',
                       '延安',
                       '南阳',
                       '郴州',
                       '琼海',
                       '黄石',
                       '张掖',
                       '苏州',
                       '武汉',
                       '阿拉尔',
                       '重庆',
                       '黄冈',
                       '濮阳',
                       '澄迈',
                       '荆州',
                       '雅安',
                       '德州',
                       '阳江',
                       '东莞',
                       '焦作',
                       '拉萨',
                       '葫芦岛',
                       '广元',
                       '七台河',
                       '北海',
                       '揭阳',
                       '唐山',
                       '松原',
                       '荆门',
                       '平顶山',
                       '吕梁',
                       '临沧',
                       '台州',
                       '澳门',
                       '东营',
                       '铜陵',
                       '渭南',
                       '日喀则',
                       '肇庆',
                       '长治',
                       '邢台',
                       '资阳',
                       '张家口',
                       '攀枝花',
                       '保亭',
                       '朝阳',
                       '吉安',
                       '鞍山',
                       '双鸭山',
                       '景德镇',
                       '济源',
                       '梅州',
                       '沈阳',
                       '十堰',
                       '佳木斯',
                       '广安',
                       '韶关',
                       '咸宁',
                       '淮安',
                       '宣城',
                       '嘉兴',
                       '永州',
                       '绍兴',
                       '菏泽',
                       '营口',
                       '石河子',
                       '马鞍山',
                       '西安',
                       '临沂',
                       '盘锦',
                       '金华',
                       '来宾',
                       '烟台',
                       '包头',
                       '屯昌县',
                       '宝鸡',
                       '深圳',
                       '湖州',
                       '上海',
                       '吴忠',
                       '镇江',
                       '蚌埠',
                       '沧州',
                       '乌兰察布',
                       '梧州',
                       '吐鲁番',
                       '清远',
                       '亳州',
                       '西宁',
                       '莆田',
                       '通化',
                       '眉山',
                       '徐州',
                       '太原',
                       '绥化',
                       '九江',
                       '广州',
                       '驻马店',
                       '齐齐哈尔',
                       '南平',
                       '五家渠',
                       '鄂州',
                       '吉林',
                       '佛山',
                       '铜仁',
                       '林芝',
                       '潜江',
                       '云浮',
                       '昆玉',
                       '许昌',
                       '贵港',
                       '漯河',
                       '贺州',
                       '三门峡',
                       '可克达拉',
                       '河源',
                       '青岛',
                       '固原',
                       '甘南',
                       '宁德',
                       '赤峰',
                       '五指山',
                       '天水',
                       '常德',
                       '白银',
                       '琼中',
                       '滨州',
                       '普洱',
                       '衢州',
                       '临高县',
                       '庆阳',
                       '萍乡',
                       '安阳',
                       '济宁',
                       '宿州',
                       '舟山',
                       '桂林',
                       '南昌',
                       '南通',
                       '白城',
                       '鄂尔多斯',
                       '定西',
                       '漳州',
                       '伊春',
                       '孝感',
                       '阜阳',
                       '新余',
                       '巴中',
                       '辽阳',
                       '大连',
                       '自贡',
                       '鹤壁',
                       '兰州',
                       '百色',
                       '扬州',
                       '莱芜',
                       '开封',
                       '信阳',
                       '海东',
                       '衡水',
                       '忻州',
                       '岳阳',
                       '郑州',
                       '盐城',
                       '鸡西',
                       '金昌',
                       '泸州',
                       '商洛',
                       '潍坊',
                       '南充',
                       '铁岭',
                       '银川',
                       '抚州',
                       '惠州',
                       '丽江',
                       '宜宾',
                       '龙岩',
                       '锦州',
                       '聊城',
                       '山南',
                       '泉州',
                       '鹤岗',
                       '温州',
                       '陵水',
                       '杭州',
                       '茂名',
                       '淄博',
                       '咸阳',
                       '德阳',
                       '北京',
                       '内江',
                       '宜春',
                       '遵义',
                       '石家庄',
                       '哈尔滨',
                       '益阳',
                       '巴彦淖尔',
                       '大庆',
                       '邯郸',
                       '安康',
                       '河池',
                       '定安',
                       '成都',
                       '玉林',
                       '新乡',
                       '宁波',
                       '通辽',
                       '潮州',
                       '承德',
                       '儋州',
                       '临汾',
                       '赣州',
                       '廊坊',
                       '晋中',
                       '朔州',
                       '大同',
                       '昭通',
                       '抚顺',
                       '本溪',
                       '武威',
                       '济南',
                       '万宁',
                       '那曲',
                       '阜新',
                       '常州',
                       '泰州',
                       '中山',
                       '安顺',
                       '北屯',
                       '柳州',
                       '福州',
                       '襄阳',
                       '克拉玛依',
                       '洛阳',
                       '怀化',
                       '衡阳',
                       '延边',
                       '双河',
                       '崇左',
                       '江门',
                       '天津',
                       '乐东',
                       '随州',
                       '张家界',
                       '石嘴山',
                       '鹰潭',
                       '汉中',
                       '白沙',
                       '无锡',
                       '辽源',
                       '仙桃',
                       '秦皇岛',
                       '汕尾',
                       '哈密',
                       '淮南',
                       '乌鲁木齐',
                       '株洲',
                       '南宁',
                       '威海',
                       '陇南',
                       '图木舒克',
                       '周口',
                       '阳泉',
                       '呼和浩特',
                       '商丘',
                       '宿迁',
                       '运城',
                       '铁门关',
                       '白山',
                       '榆林',
                       '中卫',
                       '丹东',
                       '海南',
                       '遂宁',
                       '连云港',
                       '绵阳',
                       '乐山',
                       '泰安',
                       '平凉']