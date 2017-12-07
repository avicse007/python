#re_finditer
'''
finditer() returns an iterator that produces Match instances instead of the
strings returned by findall().
'''

import re

text = 'abbaaabbbbaaaaa'
pattern = 'ab'

for match in re.finditer(pattern,text):
	s = match.start()
	e = match.end()
	print("Found %s from %d to %d "%(text[s:e],s,e));
