# ЗАДАЧА 1
#
# Реализовать класс Person, у которого должно быть два публичных поля: age и name.
# Также у него должен быть следующий набор методов: know(person),
# который позволяет добавить другого человека в список знакомых.
# И метод is_known(person), который возвращает знакомы ли два человека

class Person:
	def __init__(self, age, name):
		self.age = age
		self.name = name
	    self.known_persons = []
	
	def know(self, person):
		if not person in self.is_known_person:
			self.person = self.known_persons + person
		    print ('We have added {} to your list.'.format(person))
		else:
		    print('This name is already been in your list.') 

	def is_known(self, person):
		boolen = {True : 'You know this user', False : 'You don\'t know this person'}
		is_known_person = person in self.known_persons
		print('{}{}{}'.format(self.name, boolen[is_known_person], person.name ))
