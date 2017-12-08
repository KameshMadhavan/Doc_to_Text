from docx import Document
import os
import re
from operator import itemgetter
import sys

reload(sys)
sys.setdefaultencoding('utf8')


folderpath="/home/liferayapp/Documents/index/data/Index/David-Springer"
# folderpath="/home/liferayapp/Documents/index/data/Index/Mcdonald-JBL"


out= open('/home/liferayapp/Documents/index/data/Index/fulldavidfile.txt','w')


filelist=[]
pattern = re.compile('([0-9]*).docx')

for files in os.listdir(folderpath):
	if files.endswith('.docx'):
		templist=[]
		print files
		number = pattern.search(files).group(1)
		print number
		templist.append(int(number))
		templist.append(files)
		filelist.append(templist)

print filelist

sortfilelist = sorted(filelist, key=itemgetter(0))
print sortfilelist

for i in sortfilelist:
	inputpath = str(folderpath)+str('/')+str(i[1])
	s= Document(inputpath)
	for i in s.paragraphs:
		print >>out, i.text.encode('utf-8').strip()