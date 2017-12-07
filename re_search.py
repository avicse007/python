#re_search.py

import re

pattern = 'this'
text = 'Does this text contais the pattern'
match = re.search(pattern,text)
print("Found \"%s\" in \"%s\" from \n %d to %d and is %s"%(match.re.pattern,match.string,match.start(),match.end(),match.string[match.start():match.end()]))


