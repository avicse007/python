#!bin/python3
''' Saving your object data in dicitionay is a ggod practice and flexibility 
'''

class Duck:
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
def main():
	donald = Duck(color="yellow",feet="55");
	donald.quack()
	donald.walk()
	print("Now the donald color is ",donald.getVariables('color'))
	print("Now the donald feet is ",donald.getVariables('feet'))
	print("Now the donald head is ",donald.getVariables('head'))
if __name__=='__main__':
	main()
