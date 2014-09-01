import re

p = re.compile(r'\d+')
print p.split('one1two2three3four4')

print p.split('one1two2three3four4',2)

