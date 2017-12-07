#OrderedDictionary
from collections import OrderedDict
d = OrderedDict()
d['x']=1;
d['y']=10;
d['z']=7;
for key in d:
	print(key,d[key])
