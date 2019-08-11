# ЗАДАЧА 2
#
# Есть класс, который выводит информацию в консоль: Printer,
# у него есть метод: log(*values).
# Написать класс FormattedPrinter, который выводит в консоль информацию, окружая ее строками из *

class Printer(object):
	
	def __init__(self):
		self.values = []

	def log(self, *values)
		self.values = [random for random in values]
		print(self.values)

class FormattedPrinter(Printer)
	
	def formated_log(self, *values)
		print('************************')
		self.log(*values)
		print('************************')