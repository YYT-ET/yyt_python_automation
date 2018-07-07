import re
# zifuchuan = "java<h1>python<h1>htmLlajfl"
# xuanquZiduan='<h1>.+h'
# patten=re.compile(xuanquZiduan)#(括号里以后写正则表达式)
# matcher=re.search(patten,zifuchuan)
# print(matcher.group(0))

string1 = "32131@qq.com.qp.ali.amaz.com"
zhuaqu = '32131@qq\.com'
patten1=re.compile(zhuaqu)
matcher1 =re.search(patten1,string1)
print(matcher1.group(0))

string2 = "http://www.nsfbuhwe.com and https://www.auhfisna.com"
p2="https*://"
pattent2=re.compile(p2)
matcher2 = re.search(pattent2,string2)
print(matcher2.group(0))

# print("????????????????findall???????/")
# string3 ="lalala<hTml>hello</Html>he <xml>jj</Xml>"
# p3 = "<[HhTt],[Xx][Mm][Ll]>.+?</[HhTt],[Xx][Mm][Ll]>"
# pattern3 = re.compile(p3)
# matcher3=re.findall(pattern3,string3)
# print(matcher3.group(0))

string4 = "chuxiuhong@hit.edu.cn"
p4="@.+?\."
pattent4=re.compile(p4)
matcher4 = re.search(pattent4,string4)
print(matcher4.group(0))

# +可以匹配+号前的字符多次
# .可以匹配.后面的任意字符一次
# *可以匹配*前面字符0次或多次
# ？解除一直匹配多次的模式，只匹配一次
# {1,3}大括号，对大括号前面的字符匹配1到3次

string4 = "saas and sas and saaas"
p4="sa{1,3}s"#对a匹配1到3次
pattent4=re.compile(p4)
matcher4 = re.findall(pattent4,string4)
print(matcher4)

string6 = "jjhee jhhhee jheeeeeee"
p6="j{1,2}h{1,3}e{1,7}"
pattent6=re.compile(p6)
matcher6 = re.findall(pattent6,string6)
print(matcher6)

# string5 = "192.168.1.1"
# p5="(\d+{1,3}\.){3}\d+{1,3}\."
# pattent5=re.compile(p5)
# matcher5 = re.findall(pattent5,string5)
# print(matcher5)
#p6="(?<=<h([1-6])>).+?(?=</h1>)"

string6 = "ava<h1>python</h3>htmLlajfl"
p6="<h([1-6])>.*?</h\1>"
pattent6=re.compile(p6)
matcher6 = re.findall(pattent6,string6)
print(matcher6)