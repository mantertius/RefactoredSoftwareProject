import calendar
from tkinter.constants import TRUE
from employee2 import *
from datetime import date
class CompanySystem:
	def __init__(self):
		self.employedList = {}
		self.accumulatedWage= {}
		self._paydays = ['semanal 1 sexta','semanal 2 sexta','mensal $']
		#self.employeePayday = {'dia' : [<empregado1>,emprega2]}

	def searchEmployeeByName(self, employeeName):
		if employeeName in self.employedList.name:
			return True
		else:
			return False
	
	def searchEmployeeByID(self, _employeeID):
		"""Returns the object if found. If not found, returns False"""
		if self.employedList.get(_employeeID) != None:
			return self.employedList[_employeeID]
		else:
			return False
	#recieves the object employee
	def addEmployee(self, newEmployeeObject):
		"""Adds an employee based on the EmployeeObject."""
		self.employedList[newEmployeeObject.companyID] = newEmployeeObject  #appends the whole object
		self.accumulatedWage[newEmployeeObject.companyID] = 0 # every new employee begins with zero money
		print(f'Employee {newEmployeeObject.getID()} added to the database')
	
	def removeEmployee(self, _employeeID):
		"""Removes an employee after searching for his name. DEPRECATED"""
		if self.searchEmployeeByID(_employeeID) != False:
			return self.employedList.pop(_employeeID)
		else:
			return False

	def removeEmployeeByID(self,employeeID):
		"""Removes an employee after searching for his ID."""
		if self.searchEmployeeByID(employeeID):
			print('Employee removed.')
			return self.employedList.pop(employeeID)
		else:
			return False

	def electronicData(self, arrival, leaving, employee) -> bool:
		"""Recieves arrival, leaving and the object Employee. Returns boolean."""
		if employee.type == 'hourist':
			workedHours = int(leaving) - int(arrival)
			print(f"Horas trabalhadas: {workedHours}")
			total = workedHours
			if workedHours > 8:
				extra = workedHours - 8
				total = int(employee.salary)*8 + int(employee.salary)*extra*1.5					
				print(f'Horas extras: {extra}. Total a ser pago: {total}')
				self.accumulatedWage[employee.companyID] += total
				print(f'{total} adicionado em sua carteira.')
				return True
		else:
			return False

	def saleData(self,employee,saleValue):
		"""Recieves employee Object and the Sale value. Returns boolean."""
		if employee.type == 'commissioned':
			commission = int(employee.commission)*int(saleValue)/100
			self.accumulatedWage[employee.companyID] += commission
			print(f'{commission} adicionado em sua carteira.')
			return int(commission)
		else:
			return False
	
	def feeData(self,employee,feeValue):
		"""Recieves employee Object and the Fee value. Returns boolean."""
		if employee.unionStatus:
			self.accumulatedWage[employee.companyID] -= int(feeValue)
			print(f'{feeValue} retirado de sua carteira.')
			return int(feeValue)
		else:
			return False

	#def runPayroll(self,selectedPayday):
		# employee in self.accumulatedWage:
			#if employee.payday == 'semanal 1 sexta' && date.today() ==

		#pass


CompanySystem = CompanySystem()

# print()
# print('--------------------------------------------------------')
# hourist = Employee('Nome1','Endereço1','hourist','10','weekly')
# salaried = Employee('Nome2','Endereço2','salaried','1132')
# commissioned = Employee('Nome3','Endereço3','commissioned','1132',commission=5,payday='bi-weekly')

# #id1 = test.getID()
# idh = hourist.getID()
# ids = salaried.getID()
# idc = commissioned.getID()

# print(f'\nHourist: {idh.hex} | {hourist.__dict__}')
# print(f'Salaried: {ids.hex} | {salaried.__dict__}')
# print(f'Commissioned: {idc.hex} | {commissioned.__dict__}\n')
# #CompanySystem.addEmployee(test)
# CompanySystem.addEmployee(hourist)
# CompanySystem.addEmployee(salaried)
# CompanySystem.addEmployee(commissioned)
# print('-------------------------------------------------------------')
# print()

