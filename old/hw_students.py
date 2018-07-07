class Students:
    name = 'firstStudent'
    age = 18
    score = {'chinese': '80', 'math': '85','english': '90'}
    def getname(self,name):
        print(name)


    # def get_age()



#定义一个字典类：dictClass,完成一下功能
#1.删除一个Key pop() dict1.pop()
#2.判断某个键是否再字典里，有返回值，么有返回None has_key()
#3.
#4.
class operate_dict:
    def __init__(self,dict):
        self.dict=dict

    def get__dect(self,key):
        if self.dict.has_key(key):
            return self.dict(key)
        return None

    def del_key(self,key):
        if self.dict.has_key(key):
            self.dict.pop(key)
        else:
            return 'No this key'

    def get_key(self):
        return self.dict.keys()

    def update_dict(self,dict2):
        self.dict=dict(self.dict,**dict2)
        return self.dict.values()

dict1={1:'a',2:'d',3:'e'}
dictos=operate_dict()
dictos.del_key(1)
print(dictos.get__dect)