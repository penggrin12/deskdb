from pathlib import Path

class DataStoreItem():
	def __init__(self, name, db_name):
		self.name = name
		self.db_name = db_name
		self.path = Path(f"{self.db_name}//{self.name}")

		self.path.mkdir(exist_ok = True)

	def read(self, value_name):
		with open(f"{self.db_name}/{self.name}/{value_name}.data", "r") as file:
			result = file.readlines()[0]

			if result.isdigit():
				return int(result)
			else:
				return result

	def write(self, value_name, value):
		with open(f"{self.db_name}/{self.name}/{value_name}.data", "w") as file:
			file.write(str(value))

class DataStore():
	def __init__(self, name):
		self.name = name
		self.path = Path(self.name)

		self.path.mkdir(exist_ok = True)

	def get_item(self, item_name):
		return DataStoreItem(item_name, self.name)
