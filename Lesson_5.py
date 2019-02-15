#1. Создать класс корзина, у которого можно выставить разную 
#вместительность для разных объеток. 
#В объект класса корзина можно помещать объекты 
#2. Создать класс пакет в который тоже можно помещать предметы. 
#У него тоже есть вместимость 
#3. Создать любой класс, объекты которого можно было помещать в корзину и 
#пакет 
#4. Если вместимость недостаточно, сказать, что объект поместить нельзя.

capacity = 3
class basket(object):
	def __init__(self, spaciousness):
		self.spaciousness = spaciousness

class packet(basket):
	def put_in_packet(self, put):
		self.put = put

class product(basket):
	def check_product(self, check_product_in_cart):
		if check_product_in_cart > capacity:
			print('Недостаточно вместимости')
		else:
			print('Мы успешно положили ваш товар')

c = basket()
print(c.b)

