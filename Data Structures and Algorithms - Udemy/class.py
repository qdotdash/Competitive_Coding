class Character:
	def __init__(self, name, character):
		self.name = name
		self.character = character
	def printProfile(self):
		print("My name is ", self.name, " & my character is ", self.character)

class Wizard(Character):
	def __init__(self, name, character, specialisation):
		super().__init__(name, character) #or Character.__init__ also works
		self.specialisation = specialisation
	def saySpec(self):
		print("I am a Wizard and I specialize in ", self.specialisation)

class King(Character):
	pass

char1 = Character("Akshay", "Lone Wolf")
char1.printProfile()
wizard1 = Wizard("Abbas", "Wizard", "Code Magic")
wizard1.printProfile()
wizard1.saySpec()
king1 = King("Alina", "Dragon Slayer")
king1.printProfile()
king1.name = "Agent 22"
king1.printProfile()
