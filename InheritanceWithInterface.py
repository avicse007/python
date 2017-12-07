#!bin/python3
class Animal :
	def talk(self):
		print("I am takling")
	def walk(self):
		print("Hey I am walking here")
	def clothes(self): print("I have nice clothes ")

class Duck(Animal):
	def talk(self):
		print("Quack quack !!!!!!!");
	def walk(self):
		print("Walk like a duck")
	def clothes(self): print("Ducks have no clothes they have feathers")
class Dog(Animal):
	def talk(self):
		print("Wol Wol Wollllll !!!!!!!");
	def walk(self):
		print("Walk like a dog")
	def clothes(self): print("Dogs have no clothes they have fur")

def main():
	donald = Duck()
	fiddo = Dog()
	for obj in (donald,fiddo):
		obj.talk();
		obj.walk();
		obj.clothes();


if __name__=='__main__':
	main()
