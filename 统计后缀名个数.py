
import os.path
nameLists=[]
dic = {}
# list1 =[]
dic2 ={}
def count_extnames(fileNames):
	for fileName in fileNames:
		extName = os.path.splitext(fileName)[1]
		nameLists.append(extName)
	# print(nameLists)
	for nameList in nameLists:
		dic[nameList] = nameLists.count(nameList)
	# print(dic)
	# dic1 = sorted(dic.items(),key = lambda x:x[1],reverse = True)
	#取出value相同的key并构建成字典
	for k,v in dic.items():
		dic2.setdefault(v,[]).append(k)
	print(dic2)
	# if dic1[0][1] == dic1[1][1]:
	# 	list1.append(dic1[0][0])
	# 	list1.append(dic1[1][0])
	# 	print(list1)
	# l1 = sorted(list(dic2),reverse=True)
	# print(l1)
	print(dic2[sorted(list(dic2),reverse=True)[0]])
# count_extnames(['2.py','1.mp3','a.py','e.txt','d.mp3','3.txt','4.mp3','b.py'])
# count_extnames(['2.py','1.mp3','a.py','e.txt','d.mp3','3.txt'])
count_extnames(['2.py','1.mp3','a.mp3','e.txt','d.mp3'])