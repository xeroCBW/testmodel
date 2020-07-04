class CusRole:
    def __init__(self,id,name,desc,code,state,pages):
        self.id = id
        self.name = name
        self.desc = desc
        self.code = code
        self.state = state
        self.pages = pages

class CusPage:

    def __init__(self,id,name,desc,code,state,selected,options):
        self.id = id
        self.name = name
        self.desc = desc
        self.code = code
        self.state = state
        self.selected = selected
        self.options = options

class CusButton:
    def __init__(self,id,name,desc,code,state):
        self.id = id
        self.name = name
        self.desc = desc
        self.code = code
        self.state = state

