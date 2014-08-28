'''
urlib2 will act on redirect automatically in response to the HTTP 3XX response code,
Compare URL in repsonse with URL in request.
'''

import urllib2

my_url = 'http://www.google.cn'
response = urllib2.urlopen(my_url)
redirected = response.geturl() ==  my_url
print redirected

my_url = 'http://rrurl.cn/b1UZuP'
response = urllib2.urlopen(my_url)
redirected = response.geturl() == my_url
print redirected
