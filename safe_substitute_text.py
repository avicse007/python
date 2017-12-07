import string
values = {'var':'foo' }
t = string.Template("$var is here but $missing is not provided")
try :
	print("Substitute ",t.substitute(values))
except KeyError as err:
	print("The Error is "+str(err));
print("Now we will print the template using safe_substitute method so that Exception is not raise and handle automatically")
print("safe Substitute ",t.safe_substitute(values))