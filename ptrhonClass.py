#!bin/python3
class Duck:
	def __init__(self,color='white'):
		self._color=color;
	def setColor(self,color):
		self._color=color
	def getColor(self):
		return self._color
	def quack(self):
		print("Quack quack !!!!!!!");
	def walk(self):
		print("Walk like a duck")
def main():
	donald = Duck();
	donald.quack()
	donald.walk()
	print("Color of donal is ",donald._color)
	donald._color='red'
	print("Color of donal is ",donald._color)
	donald.setColor("Green")
	print("Now the donald color is ",donald.getColor())
if __name__=='__main__':
	main()
