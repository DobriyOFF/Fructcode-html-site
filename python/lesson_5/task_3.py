# ЗАДАЧА 3
#
# Написать класс Animal и Human,
# сделать так, чтобы некоторые животные были опасны для человека (хищники, ядовитые).
# Другие - нет. За что будет отвечать метод is_dangerous(animal)

# Слегка дополнил задачу:
# Человек наследуется от животного.
# И у животных и у людей добавлен параметр агрессии.
# У животного и у человека есть метод Атаковать человека.
# Если параметр агрессии у нападающего и жертвы совпадает считается,
# что жертва отбилась и не считает нападавшего опасным.
# В противном случае жертва добавляет нападающего в перечень опасных для себя существ

class Animal(object):
	
	def __init__(self, name, aggressive):
		self.name = name
		self.aggressive = int(aggressive)

	def attack_human(self, human):
		if self.aggressive > human.aggressive:
			self.dangerous_animals.append(self.name)
			print ('This {} add in your list'.format(self.animal))
		else self.aggressive < human.aggressive:
			print ('Dangerously!')

class Human(Animal):
	
	def __init__(self, name, aggressive, dangerous_animals)
		self.name = name
		self.aggressive = aggressive
		self.dangerous_animals = []

	def is_dangerous(self, animal):
        answers = {True : 'Yes', False : 'No'}
        return answers[animal in self.dangerous_animals]



def main()
