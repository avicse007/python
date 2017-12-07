#Dictionay with multiple vlues in single key
d={};
d['a']=[1,2,3,4];
d['b']=[10,20,30,40];
d['c']=[11,21,31,41];
d['d']=[1.1,2.2,3.3,4.4];
d['e']=[100,200,300,400];
print(d);
for key in d :
	print("having values ",key,d[key])
#Different ways of iteration in python 
print("Using diectionary.items() method to loop over the dic \n\n\n")
for key,values in d.items():
	print("Keys: %s and values in dic is %s"%(key,values))
d['a'].append(5);
d['b'].append(50);
d['c'].append(51);
d['d'].append(5.5);
d['e'].append(500);
print ("After appeding the values to the keys of the dictionary\n\n\n")
for key,values in d.items():
	print("Keys: %s and values in dic is %s "%(key,values))
