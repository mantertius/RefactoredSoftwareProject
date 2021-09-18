from abc import ABC, abstractmethod

class ICommand():
    "The command interface, that all commands will implement"
    @staticmethod
    @abstractmethod
    def execute():
        """
        The required execute method that all command objects
        will use
        """

class Invoker:
    "The Invoker Class"    
    def __init__(self):
        self._commands = {}
    
    def register(self, command_name, command):
        "Register commands in the Invoker"
        self._commands[command_name] = command    
    
    def execute(self, command_name):
        "Execute any registered commands"
        if command_name in self._commands.keys():
            self._commands[command_name].execute()
            print(f'executando comando {command_name}')
        else:
            print(f"Command [{command_name}] not recognised")

class Receiver:
    "The Receiver"
    def __init__(cls,menu) -> None:
        cls._menu=menu

    def run_command_1(cls):
        "adds employee"
        menu = cls._menu
        return menu.addEmployee()  
    
    def run_command_2(cls):
        "removes employee"
        menu = cls._menu
        return menu.rmvEmployee()
    
        
    def run_command_3(cls):
        "changes employee attributes"
        menu = cls._menu
        return menu.changeEmployee()
    
    
    def run_command_4(cls):
        "sends electronic point"
        menu = cls._menu
        return menu.sendPoint()

    
    def run_command_5(cls):
        "sends Sale"
        menu = cls._menu
        return menu.sendSale()

    
    def run_command_6(cls):
        "sends union fee"
        menu = cls._menu
        return menu.sendTax()

    
    def run_command_7(cls):
        "changes Payday"
        menu = cls._menu
        return menu.changePayday()

    
    def run_command_8(cls):
        "creates payday"
        menu = cls._menu
        return menu.createPayday()


class Command1(ICommand):  
    """
    A Command object, that implements the ICommand interface and
    runs the command on the designated receiver
    """    
    def __init__(self, receiver):
        self._receiver = receiver    
        
    def execute(self):
        self._receiver.run_command_1()

class Command2(ICommand):  
    """
    A Command object, that implements the ICommand interface and
    runs the command on the designated receiver
    """    
    def __init__(self, receiver):
        self._receiver = receiver    
        
    def execute(self):
        self._receiver.run_command_2()

class Command3(ICommand):  
    """
    A Command object, that implements the ICommand interface and
    runs the command on the designated receiver
    """    
    def __init__(self, receiver):
        self._receiver = receiver    
        
    def execute(self):
        self._receiver.run_command_3()

class Command4(ICommand):  
    """
    A Command object, that implements the ICommand interface and
    runs the command on the designated receiver
    """    
    def __init__(self, receiver):
        self._receiver = receiver    
        
    def execute(self):
        self._receiver.run_command_4()

class Command5(ICommand):  
    """
    A Command object, that implements the ICommand interface and
    runs the command on the designated receiver
    """    
    def __init__(self, receiver):
        self._receiver = receiver    
        
    def execute(self):
        self._receiver.run_command_5()

class Command6(ICommand):  
    """
    A Command object, that implements the ICommand interface and
    runs the command on the designated receiver
    """    
    def __init__(self, receiver):
        self._receiver = receiver    
        
    def execute(self):
        self._receiver.run_command_6()

class Command7(ICommand):  
    """
    A Command object, that implements the ICommand interface and
    runs the command on the designated receiver
    """    
    def __init__(self, receiver):
        self._receiver = receiver    
        
    def execute(self):
        self._receiver.run_command_7()

class Command8(ICommand):  
    """
    A Command object, that implements the ICommand interface and
    runs the command on the designated receiver
    """    
    def __init__(self, receiver):
        self._receiver = receiver    
        
    def execute(self):
        self._receiver.run_command_8()