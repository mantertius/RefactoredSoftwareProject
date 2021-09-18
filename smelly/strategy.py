from __future__ import annotations

import datetime
import uuid
import companySystem as cs
from abc import ABC, abstractmethod
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from typing import Any

from employee2 import *


class Context():
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, strategy: Strategy) -> None:
        """
        Usually, the Context accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.
        """

        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self._strategy = strategy

    def checkValid(self,parameterList:list) -> Any:
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """

        return self._strategy.checkValid(parameterList)


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def checkValid(self, list : list):
        pass


"""
Concrete Strategies implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Context.
"""


class initialData(Strategy): #check id valid
    """Checks if there are enough data to create an employee."""
    @classmethod
    def checkValid(cls, list) -> bool:
        if '' in list:
            mb.showerror(title='Failure.',message='Could not create an employee. Try again, but remember to fill everything.')
            return False
        return True

class employeeExists(Strategy): #check if employee exists
    """Checks if employee exists in the Company System."""
    @classmethod
    def checkValid(cls, list : list):
        id = list[0]
        if '' not in list:
            realID = uuid.UUID(id)
            employee = cs.CompanySystem.searchEmployeeByID(realID)
            #print(CompanySystem)
            #print(employee)
            return cls.returnsEmployee(employee)
        else:   
            mb.showerror(title='Failure',message='Something went wrong. Maybe you forgot to fill the field?')
            return False
    @staticmethod
    def returnsEmployee(employee):
        if employee != False:
            return employee
        else: 
            return False

class employeeHourist(Strategy):
    """Boolean to if an employee is hourist or not."""
    @classmethod
    def checkValid(cls, list):
        employee = list[0]
        if employee.type == 'hourist': return True
        return False

class employeeChangerChecker(Strategy):
    """Checks which field should be changed"""
    @classmethod
    def checkValid(cls, list):
        employee = list[0]
        employeeChangerChecker.changeSender(list, employee)
        mb.showinfo(title='Success',message="Successfully changed employee's attributes.")    
        return True       

    @staticmethod
    def changeSender(list, employee):
        """Sends the Change."""
        if list[1] != '':
            employee.setName(list[1])
        if list[2] != '':
            employee.setType(list[2])
        if list[3] != '':
            employee.setSalary(list[3])
        if list[4] != '':
            employee.setCommission(list[4])       
        if list[5] != '':
            employee.setPayment(list[5])
        if list[6] != '0':
            employee.setUnionStatus(list[6])
        if list[7] != '':
            employee.setUnionID(list[7])
        if list[8] != '':
            employee.setUnionFee(list[8])
        if list[9] != '':
            employee.setAddress(list[9])

class employeeCommissioned(Strategy):
    """Boolean to if an employee is COMMISSIONED or nah"""
    @classmethod
    def checkValid(cls, list):
        employee = list[0]
        if employee.type == 'commissioned': return True
        return False

class employeeUnionStatusCheck(Strategy):
    """Boolean to if an employee is part of UNION or nah"""
    @classmethod
    def checkValid(cls, list):
        employee = list[0]
        if employee.unionStatus: return True
        return False
