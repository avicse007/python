#re_characterset.py
import re

from pattern_syntax import test_pattern
test_pattern(
'abbaabbba',
[ ('[ab]', 'either a or b'),
('a[ab]+', 'a followed by 1 or more a or b'),
('a[ab]+?', 'a followed by 1 or more a or b not greedy'),
])

'''
Patterns with no punctuations 
'''

test_pattern(
'This is some text -- with punctuation.',
[ ('[^-. ]+', 'sequences without -, ., or space')])


'''
Patterns with escape codes 

'''

print("Patterns with Escape codes \n\n")

test_pattern(
'A prime #1 example!',
[ (r'\d+', 'sequence of digits'),
(r'\D+', 'sequence of nondigits'),
(r'\s+', 'sequence of whitespace'),
(r'\S+', 'sequence of nonwhitespace'),
(r'\w+', 'alphanumeric characters'),
(r'\W+', 'nonalphanumeric'),
])

'''
Patterns with ancoring 
=======================
Code 	Meaning
^ 		Start of string, or line
$ 		End of string, or line
\A 		Start of string
\Z 		End of string
\b 		Empty string at the beginning or end of a word
\B 		Empty string not at the beginning or end of a word
'''

print("\n\n Anchoring the search")

test_pattern(
'This is some text -- with punctuation.',
[ (r'^\w+', 'word at start of string'),
(r'\A\w+', 'word at start of string'),
(r'\w+\S*$', 'word near end of string, skip punctuation'),
(r'\w+\S*\Z', 'word near end of string, skip punctuation'),
(r'\w*t\w*', 'word containing t'),
(r'\bt\w+', 't at start of word'),
(r'\w+t\b', 't at end of word'),
(r'\Bt\B', 't, not start or end of word'),
])
