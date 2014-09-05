import urllib2
import sys
import re


book_search_response = urllib2.urlopen('http://book.douban.com/subject_search?search_text=python&cat=1001')

html = book_search_response.read()

response_page = html.decode("utf-8")

"""
# python default env encode format is 'ascii'
# reload sys module for UnicodeDecodeError
reload(sys)
sys.setdefaultencoding('utf-8')

with open('search_python_book.html','w+') as f:
	f.write(html.decode("utf-8"))
"""
# book list in <li> tag
bookItems = re.findall('<li class="subject-item">(.*?)</li>', response_page, re.S)

bookUrl = []
bookTitle = []

# 
for item in bookItems
	re.findall('<div class="info">(.*?)')
