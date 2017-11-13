class Users(object):

	def __init__(self, person_factory=None):
		self.user_factory = person_factory

	def show_user(self):
        """Creates and shows a user using the abstract factory"""

        user = self.user_factory.get_user()
        print("Hey I am {}".format(user))
        print("My soft skills are {}".format(user.speak()))
        print("My Professional skills are {}".format(self.user_factory.get_pskills()))
		

class analizer(object):
	"""User Analizer"""
	def __init__(self, aspect_factory=None):
		self.characteristic_factory = aspect_factory

	def show_characteristic(self):
		characteristic = self.characteristic_factory.get_characteristic()
		print("Characteristic: {}".format(characteristic))

	def calculate_log_frecuency(user_logs_per_month):
		
		if user_logs_per_month >= 30:
			print("The user is very frecuent in the application")

		if user_logs_per_month >= 20:
			print("The user is frecuent in the application")

	def calculate_activity_per_day:
		