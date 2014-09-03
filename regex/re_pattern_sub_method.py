"""
re.sub(pattern, repl, string, count=0, flasg=0)

repl can be a string or a function;

if it is a string , any backslash escapes in it are processed.That is, \n is converted to a single newline character, \r is converted to a carriage return, and so forth. Unknown escapes such as \j are left alone. Backreferences, such as \6, are replaced with the substring matched by group 6 in the pattern

if it is a function,it is called for every non-overlapping occurrence of pattern.The function takes a single match object argument, and returns the replacement string
"""

import re 

p = re.compile(r'(\w+) (\w+)')

s = 'i say, hello world!'

print p.sub(r'\2 \1',s)

def func(m):
	return m.group(1).title() + ' ' + m.group(2).title()
	# str.title(): return a titlecased version of the string where words
	#              start an uppercase character and the remaining charac
	#              -ters are lowercase.
print p.sub(func, s)

