#re_constaring_search.py

import re

text = 'This is some text -- with some punctuation.'
'''pattern ='is'
print("Text : ",text)
print("Pattern : %s"%(pattern))
match_ = re.match(pattern,text)
print("The Match is : %s"%(match_))
search_ = re.search(pattern,text)
print("The search is : %s"%(search_))
'''
'''
Since the literal text is does not appear at the start of the input text, it is not
found using match(). The sequence appears two other times in the text, though, so
search() finds it.
'''





text = 'This is some text -- with some punctuation.'
pattern = re.compile(r'\b\w*is\w*\b')
print("Text:", text)
print(" ")
pos = 0
while True:
	match = pattern.search(text, pos)
	if not match:
		break
	s = match.start()
	e = match.end()
	print("%2d : %2d = \"%s\"" %(s, e-1, text[s:e]))
	# Move forward in text for the next search
	pos = e