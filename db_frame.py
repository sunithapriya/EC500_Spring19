import pymongo
import json

class storage:
	'''
	class for storage of data from input module
	basic functions: CRUD(create, read, update, delete)
	'''
	def readJson(self, jsonFile):
		'''
			change json file to dictionary
		'''
		dict = json.loads(jsonFile)
		pass

	def connectMongob(self):
		'''
			connect to the mongodb
		'''
		self.client = pymongo.MongoClient()
		pass

	def add(self, data):
		'''
			add data to the mongodb
		'''
		pass

	def delete(self, patientID):
		'''
			delete data
		'''
		pass

	def update(self, patientID):
		'''
			update data
		'''
		pass

	def read(self, patientID):
		'''
			read data of patient
		'''
		pass
