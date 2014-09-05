# -*- coding: utf-8 -*-    

import urllib2    
import urllib    
import re    
import thread    
import time    


class Spider_Model:    
	def __init__(self):
		self.page = 1
		self.pages = []
		self.enable = False

	# scrawl the jokes from every page,
	# add them to the list and return
	def GetPage(self, page):
		myUrl = "http://m.qiushibaike.com/hot/page/" + page
		user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		headers = {'User-Agent' : user_agent}
		req = urllib2.Request(myUrl, headers = headers)
		myResponse = urllib2.urlopen(req)
		myPage = myResponse.read()
		#encode: unicode -> other encoding format
		#decode: the contrast to encode
		unicodePage = myPage.decode("utf-8")

		# find out all class="content" of div tag
		# re.S any-word Match pattern, that is 
		# .(dot) can match a linebreak
		myItems = re.findall('<div.*?class="content".*?title="(.*?)">(.*?)</div>',unicodePage, re.S)
		items = []
		for item in myItems:
			# first element of div in itme is time
			# 2nd element of div in item is content
			items.append([item[0].replace("\n",""), item[1].replace("\n", "")])
		return items


	# Load new page
	def LoadPage(self):
		# stop if user enter "quit"
		while self.enable:
			if len(self.pages) < 2:
				try:
					# Fetch jokes in new page
					myPage = self.GetPage(str(self.page))
					self.page += 1
					self.pages.append(myPage)
				except:
					print 'Can not link to qiushibaike.com'
			else:
				time.sleep(1)
	
	#
	def ShowPage(self, nowPage, page):
		for items in nowPage:
			print u'The %d page' % page, items[0], items[1]
			myInput = raw_input()
			if myInput == "quit":
				self.enable = False
				break
	#
	def Start(self):
		self.enable = True
		page = self.page

		print u'正在加载中请稍后......'

		# start new thread to load joke and store backward
		thread.start_new_thread(self.LoadPage,())

		#----------Load----------
		while self.enable:
			if self.pages:
				nowPage = self.pages[0]
				del self.pages[0]
				self.ShowPage(nowPage, page)
				page += 1


#-------entrance of program--------
print u"""
-----------------------------------
	program : qiubai spider
	version : 0.1
	Author  : Leon R.Sine
	Date    : 2014-09-03
	language: Python 2.7.3
	Oper    : input "quit" to exit
	Func    : press "Enter" to start 
			  browse hot news of today
			  in qiubai
-----------------------------------
"""

print u'Press Enter to fetch contents'
raw_input(' ')
myModel = Spider_Model()
myModel.Start()

