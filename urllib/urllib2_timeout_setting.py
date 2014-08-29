import urllib2  
import socket  
# before Python 2.6
#socket.setdefaulttimeout(10) # timeout in 10s
#urllib2.socket.setdefaulttimeout(10) # another manners
'''
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http" : "http://127.0.0.1:8086"})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
	opener = urllib2.build_opener(proxy_handler)
else:
	opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)
'''
# After Python 2.6
response = urllib2.urlopen('https://www.youtube.com/', timeout=10)
