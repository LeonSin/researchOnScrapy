import urllib2
import sys
import re

class BookSearch:
	def getBookList(self):
		book_search_response = urllib2.urlopen('http://book.douban.com/subject_search?search_text=python&cat=1001')
		html = book_search_response.read()
		response_page = html.decode("utf-8")
		# book list in <li> tag
		bookList = re.findall('<li class="subject-item">(.*?)</li>', response_page, re.S)
		return bookList
	
"""
# python default env encode format is 'ascii'
# reload sys module for UnicodeDecodeError
reload(sys)
sys.setdefaultencoding('utf-8')

with open('search_python_book.html','w+') as f:
	f.write(html.decode("utf-8"))
"""

if __name__ == '__main__':
	bookSearch = BookSearch()
	bookListInfo = bookSearch.getBookList()
	print bookListInfo
	bookURLList = []
	if(bookListInfo):
		print 'bookListInfo is not null %d' % len(bookListInfo)
		for bookInfo in bookListInfo:
			bookURL = re.search(r'http://book\.douban\.com/subject/\d+/', bookInfo)
			bookURLList.append(bookURL.group())
	print bookURLList
