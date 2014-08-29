import urllib2
class RedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        print "301"
        pass
    def http_error_302(self, req, fp, code, msg, headers):
        print "303"
        pass

opener = urllib2.build_opener(RedirectHandler)
opener.open('http://rrurl.cn/b1UZuP')
