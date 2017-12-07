#!bin/python3
class Duck:
	def __init__(self,**kwargs):
		self._color=kwargs.get('color','white');
	def setColor(self,color):
		self._color=color
	def getColor(self):
		return self._color
	def quack(self):
		print("Quack quack !!!!!!!");
	def walk(self):
		print("Walk like a duck")
def main():
	donald = Duck(color="yellow");
	donald.quack()
	donald.walk()
	print("Now the donald color is ",donald.getColor())
if __name__=='__main__':
	main()
