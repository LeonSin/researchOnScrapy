import urllib
import urllib2
url = 'http://www.xxx.com'
values = {'userid' : 'xxxx', 'passwd' : 'xxxx'}

data = urllib.urlencode(values) # encode
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
