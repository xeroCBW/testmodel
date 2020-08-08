# from system.models import Patent
from igraph import *
def handler():

    pass

    # patent_list = Patent.objects.all()
    #
    # print(patent_list)





res = {
    "items": [
        {
            "id": 1,
            "desc": None,
            "state": True,
            "create_time": "2020-08-05T19:18:17.339338",
            "update_time": "2020-08-05T19:18:17.339393",
            "document_no": "CN201810956507.2",
            "apply_no": "CN201810956507.2",
            "apply_time": "2018.08.21",
            "public_no": "CN109031760A",
            "public_time": "2018.12.18",
            "name": "一种3D液晶显示面板、显示装置和驱动方法",
            "apply_user": "京东方科技集团股份有限公司",
            "address": "100015 北京市朝阳区酒仙桥路10号",
            "inventor": "李忠孝",
            "priority": "-----",
            "category_no": "G02F1/1335(2006.01);G02F1/1343(2006.01);G02B27/22(2006.01)",
            "main_category_no": "G02F1/1335(2006.01)I",
            "nation_province": "北京;11",
            "internation_publish": "-----",
            "internation_publish_time": "-----",
            "phrator_date": "1",
            "quote_number": 0,
            "quote_patent": "-----",
            "abstract": "本发明实施例公开了一种3D液晶显示面板、显示装置和驱动方法。3D液晶显示面板包括：对盒设置的第一基板和第二基板，第二基板的出光侧设置有用于实现3D显示的第一光栅层，该第一光栅层包括阵列排布的光栅开口，第一基板接近第二基板的一侧依次设置有电极层、液晶层和CF层；CF层包括阵列排布的滤光单元、设置于相邻滤光单元之间的黑矩阵、以及设置于每个滤光单元内部的至少一个遮光条；3D液晶显示面板用于对电极层施加电压在液晶层形成液晶光栅，使得入射到液晶层的准直光线穿过液晶光栅后改变方向通过滤光单元形成单色光后从光栅开口射出。本发明实施例能够在提高裸眼3D显示器件的观看范围的同时，兼顾较高的显示亮度。",
            "abstract_pic": "无图"
        },
        {
            "id": 2,
            "desc": None,
            "state": True,
            "create_time": "2020-08-05T19:18:17.477507",
            "update_time": "2020-08-05T19:18:17.477549",
            "document_no": "CN201810897823.7",
            "apply_no": "CN201810897823.7",
            "apply_time": "2018.08.08",
            "public_no": "CN109031757A",
            "public_time": "2018.12.18",
            "name": "显示装置及电子设备",
            "apply_user": "京东方科技集团股份有限公司",
            "address": "100015 北京市朝阳区酒仙桥路10号",
            "inventor": "谭纪风;王维;赵文卿;孟宪东;孟宪芹;王方舟;高健;梁蓬霞;陈小川",
            "priority": "-----",
            "category_no": "G02F1/1335(2006.01);G02F1/1343(2006.01);G02F1/13357(2006.01)",
            "main_category_no": "G02F1/1335(2006.01)I",
            "nation_province": "北京;11",
            "internation_publish": "-----",
            "internation_publish_time": "-----",
            "phrator_date": "1",
            "quote_number": 0,
            "quote_patent": "-----",
            "abstract": "本申请实施例提供了一种显示装置及电子设备，该显示装置包括：背光模组和位于背光模组出光面上的显示面板，显示面板包括：位于背光模组上方的基板，位于基板和背光模组之间的闪耀光栅结构；基板包括若干阵列排列的像素单元，每一像素单元包括透光区和遮光区；闪耀光栅结构，用于调节背光模组出射的光线的传播方向，以使得光线能够从透光区射出。通过闪耀光栅结构对入射准直光线的衍射，调节背光模组出射的光线的传播方向，将衍射角集中在较大的角度，并从基板侧的透光区出射，达到大幅增加出光效率的技术效果。",
            "abstract_pic": "无图"
        },
        {
            "id": 3,
            "desc": None,
            "state": True,
            "create_time": "2020-08-05T19:18:17.619035",
            "update_time": "2020-08-05T19:18:17.619094",
            "document_no": "CN201710458594.4",
            "apply_no": "CN201710458594.4",
            "apply_time": "2017.06.16",
            "public_no": "CN109031752A",
            "public_time": "2018.12.18",
            "name": "一种反射式液晶显示面板及显示装置",
            "apply_user": "京东方科技集团股份有限公司",
            "address": "100015 北京市朝阳区酒仙桥路10号",
            "inventor": "祝明;张世玉;王英涛;王美丽",
            "priority": "-----",
            "category_no": "G02F1/1335(2006.01);G02F1/13357(2006.01)",
            "main_category_no": "G02F1/1335(2006.01)I",
            "nation_province": "北京;11",
            "internation_publish": "-----",
            "internation_publish_time": "-----",
            "phrator_date": "2",
            "quote_number": 0,
            "quote_patent": "-----",
            "abstract": "本发明公开了一种反射式液晶显示面板及显示装置，通过增加光转换结构和反射型偏光结构，可以将入射光转换为与像素电极所在的像素单元对应颜色的光，与现有技术中只反射特定波长的光而发光的结构相比，大大增加了光的利用率；并且，利用反射型偏光结构，将光转换结构发出的光通过反射型偏光结构的偏振选择后再进入液晶层，有效避免了因光转换结构引起的光偏振状态改变而导致的画面不能正常显示的问题，不仅保证了显示面板的正常显示，还提高了显示画面的质量。",
            "abstract_pic": "http://books.daweisoft.com/abstphoto/FM/20181218/201710458594.4/201710458594.gif"
        },
        {
            "id": 4,
            "desc": None,
            "state": True,
            "create_time": "2020-08-05T19:18:17.729485",
            "update_time": "2020-08-05T19:18:17.729533",
            "document_no": "CN201810834939.6",
            "apply_no": "CN201810834939.6",
            "apply_time": "2018.07.26",
            "public_no": "CN109031742A",
            "public_time": "2018.12.18",
            "name": "显示基板的制造方法、显示基板及显示装置",
            "apply_user": "京东方科技集团股份有限公司",
            "address": "100015 北京市朝阳区酒仙桥路10号",
            "inventor": "卢江楠;舒适;郭康;姚琪",
            "priority": "-----",
            "category_no": "G02F1/1333(2006.01);G02F1/1335(2006.01)",
            "main_category_no": "G02F1/1333(2006.01)I",
            "nation_province": "北京;11",
            "internation_publish": "-----",
            "internation_publish_time": "-----",
            "phrator_date": "1",
            "quote_number": 0,
            "quote_patent": "-----",
            "abstract": "本发明公开了一种显示基板的制造方法、显示基板及显示装置，属于显示技术领域。该显示基板的制造方法包括：在形成有平坦层前膜层的衬底基板上形成第一平坦层；在第一平坦层远离衬底基板的一侧形成第一缓冲层；在第一缓冲层远离衬底基板的一侧形成第二缓冲层；在第二缓冲层远离衬底基板的一侧形成线栅偏振器WGP。本发明改善了第一平坦层的平坦性能。本发明用于显示基板的制造。",
            "abstract_pic": "无图"
        },
        {
            "id": 5,
            "desc": None,
            "state": True,
            "create_time": "2020-08-05T19:18:17.815971",
            "update_time": "2020-08-05T19:18:17.816013",
            "document_no": "CN201811026805.8",
            "apply_no": "CN201811026805.8",
            "apply_time": "2018.09.04",
            "public_no": "CN109031736A",
            "public_time": "2018.12.18",
            "name": "准直背光源、显示装置及其驱动方法",
            "apply_user": "京东方科技集团股份有限公司",
            "address": "100015 北京市朝阳区酒仙桥路10号",
            "inventor": "孟宪东;王维;谭纪风;孟宪芹;陈小川;高健;王方舟;凌秋雨",
            "priority": "-----",
            "category_no": "G02F1/133(2006.01);G02F1/13357(2006.01);G02F1/1343(2006.01);G09G3/36(2006.01)",
            "main_category_no": "G02F1/133(2006.01)I",
            "nation_province": "北京;11",
            "internation_publish": "-----",
            "internation_publish_time": "-----",
            "phrator_date": "1",
            "quote_number": 0,
            "quote_patent": "-----",
            "abstract": "本发明涉及显示领域，公开了一种准直背光源、显示装置及其驱动方法。所述准直背光源包括导光板和多个不同颜色的光源，在导光板的表面上设置有位于每一取光区域的取光光栅组件。对于采用上述准直背光源的显示装置的驱动方法，其通过分时控制不同颜色的光源发出光线，使得不同颜色的光线依次入射至导光板内以全反射的方式传输，所述取光光栅组件能够通过衍射作用将在所述导光板内传输的所有颜色的光线投射至彩膜基板上对应的照射区域，从而每一取光区域都能够向对应的像素区域提供彩色的准直光线，提升产品的显示品质。",
            "abstract_pic": "无图"
        }
    ]
}


def test01():
    '''
        只是按年来切割
    '''

    for x in res['items']:
        apply_time = x['apply_time']
        print(apply_time)


def test02():
    g = Graph(
        [(0, 1), (0, 2), (2, 3), (3, 4), (4, 2), (2, 5), (5, 0), (6, 3), (5, 6)]
    )

    vertex_list = g.vs.indices
    adj_list = g.get_adjlist()

    print(vertex_list)
    print(adj_list)


    ans = []

    for i in range(len(vertex_list)):
        ans.append(
            {
                'name':i,
                'category':1,
                'draggable':True
            }
        )



    res = []
    # {
    #     source: 0,
    #     target: 1,
    #     value: '夫妻'
    # }

    for i in range(len(adj_list)):
        for x in adj_list[i]:
            res.append(
                {
                    'source':i,
                    'target':x,
                    'value':'父母'
                }
            )


    print(ans)
    print(res)


    # g.vs["name"] = ["Alice", "Bob", "Claire", "Dennis", "Esther", "Frank", "George"]
    layout = g.layout("kk")

    plot(g,layout = layout)

    pass


if __name__ == '__main__':

    test02()

    pass

