from time import time
import uuid
import datetime
from datetime import date, timedelta

class Employee:
	def __init__(self,name,address,type, salary,commission=0,hourWage=0,payday='monthly',unionFee=0): 	#by default is a salaried an not filiated to the union
		self.name = name
		self.address = address
		self.type = type  													#salaried,commissioned,hourist
		self.paymentMethod = 'Depósito em conta bancária'   				#correios,cheque em mãos, depósito em conta bancária
		self.companyID = uuid.uuid4()
		self.unionID = None
		#self.hourWage = hourWage
		self.salary = salary
		self.unionStatus = False
		self.unionFee = unionFee
		self.commission = commission
		self.payday= payday
		self.createday = datetime.date.today()
		self.nextPayday = self.payCal(payday)
		print(f'Employee created. UUID: {self.companyID.hex}')

	def payCal(self,payday):
		today = datetime.date.today() #dia que foi criado
		true_payday = None
		if payday == 'weekly':
			payday = today + timedelta(days=7)
			if payday.weekday() != 4:
				time_left = payday.weekday() - 4
				true_payday = payday + timedelta(days=time_left)
		if payday == 'bi-weekly':
			payday = today + timedelta(days=14)
			if payday.weekday() != 4:
				time_left = payday.weekday() - 4
				if time_left < 0:
					true_payday = payday + timedelta(days=7-time_left)
				elif time_left > 0:
					true_payday = payday + timedelta(days=7+time_left)
		if payday == 'monthly':
			payday = today + timedelta(days=30)
			#time_left = payday.weekday() - 4
			if payday.weekday() != 4:
				time_left = payday.weekday()- 4
				if time_left <0:
					true_payday = payday + timedelta(days=7-time_left)
				elif time_left >0:
					true_payday = payday + timedelta(days=7+time_left)
		
		return true_payday

#getters 
	def getName(self):
		return self.name
	def getAddress(self):
		return self.address		
	def getType(self):
		return self.type
	def getID(self):
		return self.companyID
	def getPayment(self):
		return self.paymentMethod
	def getUnionStatus(self):
		return self.unionStatus
	def getUnionFee(self):
		return self.unionFee
	def getUnionID(self):
		return self.unionID
	def getCommission(self):
		return self.commission

#setters
	def setName(self, newName):
		self.name = newName
		print('Name changed successfully.')
	def setAddress(self, newAddress):
		self.address = newAddress
		print('Address changed successfully.')
	def setUnionID(self, newID):
		self.unionID = newID
		print('UnionID changed successfully.')
	def setHourWage(self, newWage):
		self.hourWage = newWage
		print('Hour wage changed successfully.')
	def setSalary(self,newSalary):
		self.salary = newSalary
		print('Salary changed successfully.')
	def setUnionStatus(self, status):
		if status:
			self.unionStatus = True
		else:
			self.unionStatus = False
		print('Union status changed successfully.')
	def setUnionFee(self, newTax):
		self.unionFee = newTax
		print('Union tax changed successfully')
	def setCommission(self, newCom):
		self.commission = newCom
		print('Commission changed successfully.')

	def setType(self,newType):
		self.type = newType

	def setPayment(self,newPayment):
		self.paymentMethod=newPayment
#type changers
	# def setType(self, newType, newSalary, newHourWage, newCommission):
	# 		self.salary = newSalary
	# 		self.commission = newCommission
	# 		self.hourWage = newHourWage
	# 		self.type = newType