
# test1 = ['hello', 'world', 'java', 'automaton']
def middle_upper(testList):
    newList = []  # 定义一个空的list
    for temp in testList:
        # 取余判断奇数
        s = len(temp) % 2 #取余判断奇数
        a = len(temp) // 2 #取整
        if s == 1:
            # 拼接字符串,将最中间字母大写
            str = temp[:a]+temp[a:a+1].upper()+temp[a+1:]
            newList.append(str)
        else:
            newList.append(temp)
    return newList
# print(middle_upper(test1))

if __name__ == '__main__':
    testList = ['hello', 'world', 'java', 'automaton']
    print(middle_upper(testList))

# testList = ['hello', 'world', 'java', 'automaton']
# def middle_upper(list):
#     for i in range(0,len(list)):
#         if len(list[i])%2 == 1:
#             #将中间字母大写
#             mid = len(list[i])//2
#             str = list[i][:mid]+list[i][mid:mid+1].upper()+list[i][mid+1:]
#             list[i] = str
#         else:
#             print('null')
#
#     return list
#
# print(middle_upper(testList))










