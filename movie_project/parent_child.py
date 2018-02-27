# illustrate the inherence property in Python
class Parent():
 	def __init__(self, last_name, eye_color):
 		print("Parent Constructor Called")
 		self.last_name = last_name
 		self.eye_color = eye_color

 	def show_info(self):
 		print("Last Name - " + self.last_name)
 		print("Eye Color - " + self.eye_color)

lianingxu = Parent("Xu", "brown")
print(lianingxu.last_name)


class Child(Parent):
	def __init__(self, last_name, eye_color, no_of_toys):
		print("Child Constructor Called")
		Parent.__init__(self, last_name, eye_color)
		self.no_of_toys = no_of_toys

yihanxu = Child("Xu", "dark brown", 10)
print(yihanxu.no_of_toys)
print(yihanxu.eye_color)

lianingxu.show_info()
yihanxu.show_info()