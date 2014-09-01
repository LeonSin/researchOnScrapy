# -*- coding: utf-8 -*-
# a search method example
# diff between search() and match()

import re

# compilation of regex
pattern = re.compile(r'world')

# Try to match the substring with search()
# return None if unmatches
match = pattern.search('hello world!')

if match:
	print match.group()

