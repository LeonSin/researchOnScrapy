# -*- coding: utf-8 -*-    

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
	
	def getBookURLList(self, bookList):
		bookURLList = []
		if(bookList):
			for bookInfo in bookList:
				bookURL = re.search(r'http://book\.douban\.com/subject/\d+/', bookInfo)
				# get the unicode String
				bookURLList.append(bookURL.group())
		return bookURLList

	def getBookDetailInfo(self, bookURL):
		bookInfoResponse = urllib2.urlopen(bookURL)
		bookDetailInfoPage = bookInfoResponse.read().decode("utf-8")
		reload(sys)
		sys.setdefaultencoding('utf-8')

		with open('python__book_'+bookURL.split("/")[-2]+'.html','w+') as f:
			f.write(bookDetailInfoPage.decode("utf-8"))

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
	bookURLList = bookSearch.getBookURLList(bookListInfo)
	for bookURL in bookURLList:
		bookSearch.getBookDetailInfo(bookURL)
