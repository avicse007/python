#!bin/python3
''' Here both the Dog and Duck share the same interface that is the set of methoods so the method call 
	by any of these objects automatically calls the correct one . This is called polymorphism. Because objects in bython does not checks what the class name is .It work on the set of function it has .
	This is also called is duck typing or lossely typing. Becasue of this python naturally comes with polymorphism.
'''
class Duck():
	def quack(self):
		print("Quack quack !!!!!!!");
	def walk(self):
		print("Walk like a duck")
	def feather(self): print("Ducks have no clothes they have feathers")
	def fur(self): print("Ducks have no fur")
	def bark(self):
		print("Duck does not bark ");
class Dog():
	def bark(self):
		print("Wol Wol Wollllll !!!!!!!");
	def walk(self):
		print("Walk like a dog")
	def fur(self): print("Dogs have fur")
	def feather(self): print("Dogs do nat have feathers")
	def quack(self):
		print("Dog Does not Quack ");

def main():
	donald = Duck()
	fiddo = Dog()
	for obj in (donald,fiddo):
		obj.quack();
		obj.walk();
		obj.feather();
		obj.bark();
		obj.fur();


if __name__=='__main__':
	main()
