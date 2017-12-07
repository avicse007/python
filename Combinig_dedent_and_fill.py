#Combinig dedent and fill 
import textwrap 

sample_text ='''
The textwrap module can be used to format text for output in
situations where pretty-printing is desired. It offers 
programmatic functionality similar to the paragraph wrapping
or filling features found in many text editors.
'''

dedentted_text = textwrap.dedent(sample_text).strip()
for width in [45,75,95] : 
	print("Column :: ",width)
	print(textwrap.fill(dedentted_text,width))
