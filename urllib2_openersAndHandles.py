# -*- coding: utf-8 -*-  
import urllib2

# create a manager of password
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# add user and password
top_level_url = "http://example.com/foo/"

# if realm is known, We can replace it with "none"
# password_mgr.add_password(None, top_level_url, username, password)
password_mgr.add_password(None, top_level_url, 'why', '1223')

# create a handler
handler = urllib2.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)
opener = urllib2.build_opener(handler)

a_url = 'http://www.baidu.com'

# fetch a URL with opener
opener.open(a_url)

# install opener.
# opener will be available once urllib2.urlopen calls
urllib2.install_opener(opener)