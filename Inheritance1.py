#!bin/python3
''' Saving your object data in dicitionay is a ggod practice and flexibility 
'''

class Animal :
	def talk(self):
		print("I am takling")
	def walk(self):
		print("Hey I am walking here")
	def clothes(self): print("I have nice clothes ")

class Duck(Animal):
	def __init__(self,**kwargs):
		self.variables=kwargs;
	def setVariables(self,k,v):
		self._variables[k]=v
	def getVariables(self,k):
		return self.variables.get(k,None)
	def quack(self):
		print("Quack quack !!!!!!!");
	def walk(self):
		print("Walk like a duck")
class Dog(Animal):
	pass

def main():
	donald = Duck(color="yellow",feet="55");
	donald.quack()
	donald.walk()
	donald.clothes();
	fiddo = Dog()
	fiddo.walk();
	fiddo.talk();
	fiddo.clothes();

if __name__=='__main__':
	main()
