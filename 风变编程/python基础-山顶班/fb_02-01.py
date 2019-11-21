file1 = open('abc.txt','r',encoding='utf-8')
filecontent = file1.read()
print(filecontent)
file1.close()

file1 = open('/Users/Administrator/Desktop/test/abc.txt','r',encoding='utf-8')
filecontent = file1.read()
print(filecontent)