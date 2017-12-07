'''
In this example, the substitution rules are changed so that the delimiter is % instead
of $ and variable names must include an underscore. The pattern %notunderscored
is not replaced by anything because it does not include an underscore character.
'''

import string
template_text ='''
Delimiter : %%
Replaced : %with_underscore
Ignored : %notunderscored
'''
d = { 'with_underscore':'replaced',
'notunderscored':'not replaced',
}
class MyTemplate(string.Template):
	delimiter = '%'
	idpattern = '[a-z]+_[a-z]+'
t = MyTemplate(template_text)
print("Modified ID pattern:")
print(t.safe_substitute(d))