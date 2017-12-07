#re_grouping.py
import re

from pattern_syntax import test_pattern
test_pattern(
'abbaabbba',
[ ('a(ab)', 'a followed by literal ab'),
('a(ab)*', 'a followed by 0 or more ab'),
('a(a*b*)', 'a followed by 0 or more a and 0 or more b'),
('a(ab)+', 'a followed by 1 or more literal ab'),
])