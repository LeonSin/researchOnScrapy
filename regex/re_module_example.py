# encoding: UTF-8
import re

# complile regex into a Pattern Object,attention to the letter 'r' which means 
# "original string"

pattern = re.compile(r'hello')

# matches the text with Pattern , return the a corresponding MatchObject instance
# return None if the string does not match the pattern

match1 = pattern.match('hello world')
match2 = pattern.match('helloo world')
match3 = pattern.match('helllo world')

# if match1 matches ok
if match1:
	# get group with match
	print match1.group()
else:
	print 'match1 unmatches' 

# if match2 matches ok
if match2:
	# get group with match
	print match2.group()
else:
	print 'match2 unmatches' 

# if match3 matches ok
if match3:
	# get group with match
	print match3.group()
else:
	print 'match3 unmatches' 
