# -*- coding: utf-8 -*-
# a search method example
# diff between search() and match()
# match()函数只检测re是不是在string的开始位置匹配
# search()会扫描整个string查找匹配

import re

# compilation of regex
pattern = re.compile(r'world')

# Try to match the substring with search()
# return None if unmatches
match = pattern.search('hello world!')

if match:
	print match.group()

