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

	#将所有的段子都抓取出来，添加到列表中并且返回列表
	def GetPage(self, page):
		myUrl = "http://m.qiushibaike.com/hot/page/" + page
		user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		headers = {'User-Agent' : user_agent}
		req = urllib2.Request(myUrl, headers = headers)
		myResponse = urllib2.urlopen(req)
		myPage = myResponse.read()
		#encode的作用是将unicode编码转换成其他编码的字符串
		#encode的作用是将其他编码的字符串转换成unicode编码
		unicodePage = myPage.decode("utf-8")

		#找出所有class="content"的div标记
		#re.S是任意匹配模式，也就是.可以匹配换行
		myItems = re.findall('<div.*?class="content".*?title="(.*?)">(.*?)</div>',unicodePage, re.S)
		items = []
		for item in myItems:
			# item 中的第一个是div的标题，也就是时间
			# item 中的第二个是div的内容，也就是内容
			items.append([item[0].replace("\n",""), item[1].replace("\n", "")])
		return items


	# 用于加载新的段子
	def LoadPage(self):
		# 如果用户未输入quit则一直运行
		while self.enable:
			# 如果pages数组中的内容小于2个
			if len(self.pages) < 2:
				try:
					#获取新的页面中的段子
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

		# 新建一个线程在后台加载段子并存储
		thread.start_new_thread(self.LoadPage,())

		#----------加载处理糗事百科----------
		while self.enable:
			# 如果self的page数组中存有元素
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
