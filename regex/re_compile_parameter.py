# -*- coding: utf-8 -*-  
# identical matcher of re : matches a decimal
import re

a = re.compile(r"""\d +   # the integer part
                   \.     # the decimal point
                   \d *   # some fractional digits""" ,re.X)
b = re.compile(r"\d+\.\d*")

match_a1 = a.match('3.1415')
match_a2 = a.match('33')
match_b1 = b.match('3.1415')
match_b2 = b.match('33')

if match_a1:
	print match_a1.group()
else:
	print u'match_a1 is not a decimal'

if match_a2:
	print match_a2.group()
else:
	print u'match_a2 is not a decimal'

if match_b1:
	print match_b1.group()
else:
	print u'match_b1 is not a decimal'

if match_b2:
	print match_b2.group()
else:
	print u'match_b2 is not a decimal'






