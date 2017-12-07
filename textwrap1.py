#textwrap1
import textwrap 

sample_text ='''
The textwrap module can be used to format text for output in
situations where pretty-printing is desired. It offers 
programmatic functionality similar to the paragraph wrapping
or filling features found in many text editors.
				'''
print("No indent: \n")
print(textwrap.fill(sample_text,width=50));

detentedText = textwrap.dedent(sample_text)
print("The dedent text is ")
print(detentedText)