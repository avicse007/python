#re_match_group_isNotalwaysEffective.py

'''
Ask for the match of a single group with group(). This is useful when grouping is
being used to find parts of the string, but some parts matched by groups are not needed
in the results.
'''




import re
text = 'This is some text -- with punctuation.'
print("Input text : ",text)
# word starting with ’t’ then another word
regex = re.compile(r'(\bt\w+)\W+(\w+)')
print('Pattern : ',regex.pattern)
match = regex.search(text)
print('Entire match : ', match.group(0))
print('Word starting with "t":', match.group(1))
print('Word after "t" word :', match.group(2))


