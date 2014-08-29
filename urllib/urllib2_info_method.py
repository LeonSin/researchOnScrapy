#info() ¡ª return the meta-information of the page, such as headers, in the form of an mimetools.Message instance
from urllib2 import Request, urlopen, URLError, HTTPError

old_url = 'http://www.baidu.com'
req = Request(old_url)
response = urlopen(req)
print 'Info(): '
print response.info()