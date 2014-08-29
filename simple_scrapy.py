# -*- coding: utf-8 -*-  
#---------------------------------------  
#   version：1.0  
#   Author：Leon  
#   Date：2013-05-14  
#   Lang：Python 2.7  
#   Operation：输入带分页的地址，去掉最后面的数字，设置一下起始页数和终点页数。  
#   Function：下载对应页码内的所有页面并存储为html文件。  
#---------------------------------------  

import string, urllib2

# define function for scrath of Destruction of Diablo Baidu post bar

def fetch_DD3_PostBar_novel(url, begin_page,end_page):
    '''
    for i in rang(begin_page, end_page+1):
        sName = string.zfill(i,5) + '.html'
        print 'Downloading No.' + str(i) + 'web page, transfer it to store as ' + sName + '......'
        f = open(sName, 'w+')
        m = urllib2.urlopen(url + str(i)).read() 
        f.write(m)
        f.close()
    '''
    pageContent = urllib2.urlopen(url).readlines()
    
    for line in pageContent:
        if '/p/' in line:
            print line
bdurl = 'http://tieba.baidu.com/f?kw=%B0%B5%BA%DA%C6%C6%BB%B5%C9%F1%D6%AE%BB%D9%C3%F0'

fetch_DD3_PostBar_novel(bdurl,0,0)
