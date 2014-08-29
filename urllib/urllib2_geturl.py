# Test with method geturl()¡ª return the URL of the resource retrieved, commonly used to determine if a redirect was followed
from urllib2 import Request, urlopen, URLError, HTTPError

old_url = 'http://rrurl.cn/b1UZuP'
req = Request(old_url)
response = urlopen(req)
print 'Old url: ' + old_url
print 'Real url: ' + response.geturl()
