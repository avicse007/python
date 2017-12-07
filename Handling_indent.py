#Handling_indent 

import textwrap 

sample_text ='''
The textwrap module can be used to format text for output in
situations where pretty-printing is desired. It offers 
programmatic functionality similar to the paragraph wrapping
or filling features found in many text editors.
'''

print(textwrap.fill(sample_text,initial_indent=' ',subsequent_indent=' '*4,width=50))
#indent characher in not necessarily to be white spaces
print(textwrap.fill(sample_text,initial_indent='***',subsequent_indent='->'*4,width=50))