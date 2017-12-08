from docx import Document
import os
import re
from operator import itemgetter
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# insert the folder path in which the docx file contains
folderpath="/home/liferayapp/Documents/index/data/Index/David-Springer"

# path where the text file to be written
out= open('/home/liferayapp/Documents/index/data/Index/fulldavidfile.txt','w')

filelist=[]
pattern = re.compile('([0-9]*).docx')

for files in os.listdir(folderpath):
	if files.endswith('.docx'):
		templist=[]
		number = pattern.search(files).group(1)
		templist.append(int(number))
		templist.append(files)
		filelist.append(templist)

sortfilelist = sorted(filelist, key=itemgetter(0))

for i in sortfilelist:
	inputpath = str(folderpath)+str('/')+str(i[1])
	s= Document(inputpath)
	for i in s.paragraphs:
		print >>out, i.text.encode('utf-8').strip()
