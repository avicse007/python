#pattern_syntax.py
'''
Given source text and a list of patterns, look for
matches for each pattern within the text and print
them
'''



import re 

def test_pattern(text,patterns=[]):
	for pattern, desc in patterns:
		print("Pattern %r desc %s "%(pattern,desc))
		print ("%r is the text "%(text))
		for match in re.finditer(pattern,text): 
			s = match.start();
			e = match.end();
			subs_str= text[s:e]
			n_blackslash = text[:s].count("\\")
			prefix = '.' * (s+n_blackslash)
			print("%s %r"%(prefix,subs_str))
			#print("start is %d "%(s))
		print()
	return 

if __name__=='__main__' :
	test_pattern('abbaaabbbbaaaaa',[('ab', "'a' followed by 'b'")])
