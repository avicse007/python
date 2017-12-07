#MoreAdvanceTemplate
'''
This example defines a new pattern to create a new type of template using
{{var}} as the variable syntax.


For more complex changes, override the pattern attribute and define an entirely
new regular expression. The pattern provided must contain four named groups for capturing
the escaped delimiter, the named variable, a braced version of the variable name,
and any invalid



'''


import re
import string

#Our custom template class extends basic Template class 

class MyTemplate(string.Template):
	delimiter = '{{'
	pattern = r'''
	\{\{(?:
	(?P<escaped>\{\{)|						# two delimeters
	(?P<named>[_a-z][_a-z0-9]*)\}\}|		# identifiers
	(?P<braced>[_a-z][_a-z0-9]*)\}\}|		# braced identifiers
	(?P<invalid>)							# ill formed delimeters exprs
	)
	'''

t = MyTemplate('''
	{{{{
	{{var}}
	''')
value = {'var' : 'Avinash'}
print("SUBSTUTION IS ")
print(t.safe_substitute(value))
print("MATCHES: ", t.pattern.findall(t.template))
