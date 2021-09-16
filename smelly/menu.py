import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from employee2 import *
from companySystem import *
asciiTitle ="""           
                                   _   _ 
  _ __   __ _   _  _   _ _   ___  | | | |
 | '_ \ / _` | | || | | '_| / _ \ | | | |
 | .__/ \__,_|  \_, | |_|   \___/ |_| |_|
 |_|            |__/            
 """           
class checkbar(Frame):
    """It's the checkbar's class!"""
    def __init__(self, parent=None, picks=[],side=LEFT,anchor=W):
        Frame.__init__(self,parent)
        self.vars = []
        for pick in picks:
            var = IntVar()
            chk = Checkbutton(self, text=pick, variable=var)
            chk.pack(side=side,anchor=anchor,expand=YES)
            self.vars.append(var)
    def state(self):
        return map(lambda var:var.get(),self.vars)

def ContainerCombobox(master, labelText, optionList) -> StringVar:
    """Creates a Combobox and a Label. Adds it to master. Returns the selected."""
    containerCombobox = Frame(master)
    containerCombobox.pack()
    options = optionList
    _paymentLabel = Label(containerCombobox,text=labelText)
    _paymentLabel.pack(side=LEFT,padx=30)
    _payment = StringVar(master)
    _payment.set(options[0])
    _paymentChooser = ttk.Combobox(containerCombobox,state='readonly',values=options,textvariable=_payment)
    _paymentChooser.pack(side=RIGHT)
    return _payment

def Container(master,txt):

    """Creates a Frame that holds a label and an entry. Returns the entry input

    Is attatched to master and shows txt on the label."""

    container = Frame(master,pady=0)
    container.pack()
    lbl = Label(container, text=txt) 
    lbl.pack(padx=25,side=LEFT)
    entry = Entry(container,width=25) #input
    entry.pack(side=RIGHT)
    
    return entry

def destroyWin(self):
    quit(self)

def submit(win,name,address,type,salary,commission):
    #print([name+salary+address])
    if name != '' and address !='' and salary!="":
        if type == 'commissioned':
            newemployee = Employee(name=name, salary=salary, address=address, type=type, commission=commission,payday='Bi-Weekly')
            CompanySystem.addEmployee(newemployee)
            
            employeeID = newemployee.getID()
            print(employeeID.hex)
            str = f"""
            Successfully added the new employee!
                                ID:{employeeID.hex}"""
            #send the data to the database?
            a = mb.showinfo(title='Success!',message=str)
        
        elif type == 'hourist':
            newemployee = Employee(name=name,salary=salary,address=address,type=type,commission=commission,payday="Weekly")
            CompanySystem.addEmployee(newemployee)
            
            employeeID = newemployee.getID()
            print(employeeID.hex)
            str = f"""
            Successfully added the new employee!
                                ID:{employeeID.hex}"""
            #send the data to the database?
            a = mb.showinfo(title='Success!',message=str)
        else:
            newemployee = Employee(name=name,salary=salary,address=address,type=type,commission=commission,payday="Monthly")
            CompanySystem.addEmployee(newemployee)
            
            employeeID = newemployee.getID()
            print(employeeID.hex)
            str = f"""
            Successfully added the new employee!
                                ID:{employeeID.hex}"""
            #send the data to the database?
            a = mb.showinfo(title='Success!',message=str)

    else:
        mb.showerror(title='Failure.',message='Could not create an employee. Try again, but remember to fill everything.')

def windowTitleAndSearch(master,txt) -> None:
    """Creates a Frame with a Title and a Entry to search Employee. Creates a separator too. Returns the Entry object"""
    titleContainer = Frame(master)
    titleContainer.pack()
    title = Label(titleContainer,text=txt,font=('Arial','11','bold'))
    title.pack()
    idTxt = Frame(master)
    _id = Entry(idTxt)
    idTxt.pack(fill=X,expand=True,padx=5)
    _id.pack(fill=X,expand=True)
    searchBtn = Button(idTxt,text='Search',command=lambda arg1=_id.get(),arg2=idTxt,arg3=True : employeeSearcher(idTxt,_id.get(),True))
    searchBtn.pack(side=RIGHT)
    sep = ttk.Separator(master,orient='horizontal')
    sep.pack(fill=BOTH,pady=5)
    return _id

def showComission(container,lbl,entry,type):
    selected = type.get()
    if selected == 'commissioned':
        container.pack()
        lbl.pack(side=LEFT)
        entry.pack(side=RIGHT)
    else:
        container.pack_forget()
        lbl.pack_forget()
        entry.pack_forget()

def employeeSearcher(master,id,showEmployee) -> Employee:
    """Search for an employee by it's ID and return the found employee (if found)."""
    if id != '':
        realID = uuid.UUID(id)
        a = CompanySystem.searchEmployeeByID(realID) #object Employee
        if a != False:
            name = a.getName()
            address = a.getAddress()
            payment = a.getPayment()
            status = a.getUnionStatus()
            uID = a.getUnionID()
            commission = a.getCommission()
            uFee = a.getUnionFee()
            type = a.getType()
            #TODO #6 FIX this container and fix the change button
            if showEmployee:
                container=Frame(master)
                txt1 = Label(container,text=f'Name: {name} | Address: {address} | Type: {type} | Payment: {payment} | Union Status: {status} | Union ID: {uID} | Union Fee: {uFee} | Commision: {commission} | Salary: {a.salary}')
                container.pack(side=TOP,padx=5,pady=5)
                txt1.pack()
                master.update()
            return a
        else:
            mb.showerror(title="Employee not found",message='Employee not found.')
    else:
        mb.showerror(title='Failure',message='Something went wrong. Maybe you forgot to fill the field?')
        return False

def employeeRemover(id) -> bool:
    if id != "":
        a = CompanySystem.removeEmployeeByID(uuid.UUID(id))
        if a != False:
            b=mb.showinfo(title='Success!',message=f'Employee with ID: {id} removed.')
        else:
            c=mb.showerror(title="Failure.",message="Employee could not be removed.")
    else:
        mb.showerror(title='Fill the ID!',message="Don't forget to fill the ID field.")

def employeeChanger(master,name,type,salary,commission,payment,unionStatus,unionID,unionFee,address, employeeID) -> bool:
    print(f'+++++++++++++[{master,name,type,salary,commission,payment,unionStatus,unionID,unionFee,address, employeeID}]+++++++++++')
    if employeeID != '': 
        realID = uuid.UUID(employeeID)
        employee = CompanySystem.searchEmployeeByID(realID)
        if employee != False:
            if name != '':
                employee.setName(name)
            if type != '':
                employee.setType(type)
            if salary != '':
                employee.setSalary(salary)
            if commission != '':
                employee.setCommission(commission)       
            if payment != '':
                employee.setPayment(payment)
            if unionStatus != '0':
                employee.setUnionStatus(unionStatus)
            if unionID != '':
                employee.setUnionID(unionID)
            if unionFee != '':
                employee.setUnionFee(unionFee)
            if address != '':
                employee.setAddress(address)       
            mb.showinfo(title='Success',message="Successfully changed employee's attributes.")
        else:
            mb.showerror(title='Failure',message='Employee not found')
            return False
    else:
        mb.showerror(title='Failure',message='Invalid UUID')
        return False

def pointSender(master, employeeID,arrival,leaving) -> bool:
    """Sends Electronic Point Data to the Company System. Returns boolean"""
    if employeeID != '':
        realID = uuid.UUID(employeeID)
        employee = CompanySystem.searchEmployeeByID(realID)
        if employee != False:
            sent = CompanySystem.electronicData(arrival,leaving,employee)
            if sent:
                mb.showinfo(title='Success',message='Electronic point data sent to the system.')
                return True
            else:
                mb.showerror(title='Failure',message='Employee is not hourist')
                return False
        else:
            mb.showerror(title='Failure',message='Employee not found.')
            return False
    else:
        mb.showerror(title='Failure',message='Employee ID missing.')
        return False

def saleSender(master, employeeID, sale) -> bool:
    """Sends Sale Data to the Company System. Returns boolean"""
    if employeeID != '':
        realID = uuid.UUID(employeeID)
        employee = CompanySystem.searchEmployeeByID(realID)
        if employee != False:
            sent = CompanySystem.saleData(employee,sale)
            if sent:
                mb.showinfo(title='Success',message=f'Sale data sent to the system. {sent} added to the wallet')
                return True
            else:
                mb.showerror(title='Failure',message='Employee is not commissioned')
                return False
        else:
            mb.showerror(title='Failure',message='Employee not found.')
            return False
    else:
        mb.showerror(title='Failure',message='Employee ID missing.')
        return False

def feeSender(master,employeeID,fee) -> bool:
    """Sends Sale Data to the Company System. Returns boolean"""
    if employeeID != '':
        realID = uuid.UUID(employeeID)
        employee = CompanySystem.searchEmployeeByID(realID)
        if employee != False:
            sent = CompanySystem.feeData(employee,fee)
            if sent:
                mb.showinfo(title='Success',message=f'Fee data sent to the system. {sent} removed from the wallet.')
                return True
            else:
                mb.showerror(title='Failure',message='Employee does not belongs to Union')
                return False
        else:
            mb.showerror(title='Failure',message='Employee not found.')
            return False
    else:
        mb.showerror(title='Failure',message='Employee ID missing.')
        return False

def paydayChanger(master,employeeID, payday) -> bool:
    """Changes the Payday. Returns boolean"""
    if employeeID != '':
        realID = uuid.UUID(employeeID)
        employee = CompanySystem.searchEmployeeByID(realID)
        if employee != False:
            sent = CompanySystem.feeData(employee,payday)
            if sent:
                mb.showinfo(title='Success',message='Fee data sent to the system.')
                return True
            else:
                mb.showerror(title='Failure',message='Employee is not hourist')
                return False
        else:
            mb.showerror(title='Failure',message='Employee not found.')
            return False
    else:
        mb.showerror(title='Failure',message='Employee ID missing.')
        return False

def rollthePay(master):
    #for employee in CompanySystem.employedList:
        #if employee.payday ==
    pass

class Menu(Frame):
    """ It's the class that shows the MENU."""
    def __init__(self,master=None):
        self.root = Frame.__init__(self,master)
        # ---- default settings ----
        timeNow = datetime.datetime.now()
        self.defaultFont = ("Arial", "10")
        self.titleFont = ("Arial",'10','bold')
# MENU      #######################################################################
    # ---- title ----
        self.titleContainer = Frame(master,pady=20)
        self.titleContainer.pack(fill='x')
        self.title = Label(self.titleContainer,justify=LEFT, text=asciiTitle,font=('Courier','10','bold'))
        self.title.pack()

    # ----- date -----       
        self.dateContainer = Frame(master,pady=20).pack()
        self.date = Label(self.dateContainer,text=f'Today is {timeNow.strftime("%x")}',pady=20).pack()
        
    # ----- add employee -----
        self.addEmployeeContainer = Frame(master).pack(pady=0)
        self.btnAddEmployee = Button(self.addEmployeeContainer,text='Add Employee', command=self.addEmployee).pack()
        
    # ----- remove employee -----       
        self.removeEmployeeContainer = Frame(master,pady=0)
        self.removeEmployeeContainer.pack()
        self.btnRemoveEmployee = Button(self.removeEmployeeContainer,text='Remove Employee', command=self.rmvEmployee)
        self.btnRemoveEmployee.pack()

    # ----- change employee -----       
        self.changeEmployeeContainer = Frame(master, pady=0).pack()
        self.btnChangeEmployee = Button(self.changeEmployeeContainer, text='Change Employee', command=self.changeEmployee).pack(pady=0)

    # ----- placeholder -----
        self.spacer=Frame(master,pady=20).pack()
        self.spacerLbl=Label(self.spacer,text='').pack()

    # ----- send point ----      
        self.sendPointContainer = Frame(master,pady=20).pack()
        self.btnSendPoint = Button(self.sendPointContainer,text='Send Electronic Point Data',command=self.sendPoint).pack()
        
    # ----- send Sale ----       
        self.sendSaleContainer = Frame(master,pady=20).pack()
        self.btnSendSale = Button(self.sendSaleContainer,text='Send Sale Data',command=self.sendSale).pack()
        
    # ----- send tax -----       
        self.sendTaxContainer = Frame(master,pady=20).pack()
        self.btnSendTax = Button(self.sendTaxContainer,text='Send Union Service Fee',command=self.sendTax).pack()
    
    # ----- spacer -----
        self.spacerLbl=Label(self.spacer,text='').pack()

    # ----- change payday -----       
        self.changePaydayContainer = Frame(master,pady=20).pack()
        self.btnChangePayday = Button(self.changePaydayContainer,text='Change Payday',command=self.changePayday).pack()

    # ----- create payday -----       
        self.createPaydayContainer = Frame(master,pady=20).pack()
        self.btnCreatePayday = Button(self.createPaydayContainer, text='Create Payday',command=self.createPayday).pack()
        
    # ----- run payroll -----       
        self.runPayrollContainer = Frame(master,pady=20)
        self.runPayrollContainer.pack()
        self.btnRunPayroll = Button(self.runPayrollContainer,text='Run Payroll',font=('Arial','11','bold'),command=self.runPayroll).pack()

    # ----- exit -----       
        self.exitButtonContainer = Frame(master,pady=20,borderwidth=2,relief=RAISED)
        self.exitButtonContainer.pack(side=BOTTOM,fill=BOTH,expand=TRUE)
        self.btnExit = Button(self.exitButtonContainer,text='Exit',command=self.destroy)
        self.btnExit.pack(side=BOTTOM)     
# FEATURES  #######################################################################

    def addEmployee(self):
        win = Toplevel(menu)
        #menu.withdraw()
        master = win
        # ----- settings -----
        win.title("Add Employee")
        options = ['hourist', 'salaried', 'commissioned']
        # ----- brief explanation of the function
        container1 = Frame(win,pady=20)
        container1.pack()
        title = Label(container1,text='Fill the data of the new employee then press the button.',font=self.titleFont)
        title.pack()


        # ----- name ------
        container2 = Frame(win,pady=0)
        container2.pack()
        lbl1 = Label(container2, text='Name')
        lbl1.pack(padx=25,side=LEFT)
        entry1 = Entry(container2,width=25)
        entry1.pack(side=RIGHT)
        entry1.get()

        # ----- address -----   
        container3 = Frame(win,pady=0)
        container3.pack()
        lbl2 = Label(container3,text='Address')
        lbl2.pack(padx=25,side=LEFT)
        entry2 = Entry(container3,width=25)
        entry2.pack(side=RIGHT)

        # ----- type dropdown ------
        container4 = Frame(win,pady=0)
        container4.pack()
        lbl3 = Label(container4,text='Type')
        lbl3.pack(side=LEFT,pady=5)
        type = StringVar(master)
        type.set(options[0])
        typeChooser = ttk.Combobox(container4,state='readonly',values=options,textvariable=type)
        typeChooser.pack(side=RIGHT)
        #----- salary ------
        salarycontainer = Frame(win,pady=0)
        salarytxt   = Label(salarycontainer,text='Salary')
        salaryentry = Entry(salarycontainer)
        salaryentry.pack(side=RIGHT)
        salarycontainer.pack()
        salarytxt.pack(side=LEFT)
        
        # ------ comission or not ------
        container5 = Frame(win,pady=0)
        lbl4=Label(container5,text='Commission')
        entry4=Entry(container5,width=25)
        entry4.insert(END,'')
        type.trace_add('write',lambda arg1=container5,arg2=lbl4,arg3=entry4,arg4=type:showComission(container5,lbl4,entry4,type))
        
        # ----- exit ------
        exitButtonContainer = Frame(master,pady=5,borderwidth=1)
        exitButtonContainer.pack(side=BOTTOM,fill=X)
        btnExit = Button(exitButtonContainer,text='Back',command=win.destroy)
        btnExit.pack(side=LEFT)
        
        # ----- submit -----
        
        # data= {}
                                                                                                                                                                                        # data['salaryentry'] = salaryentry.get()
                                                                                                                                                                                        # data['address'] = entry2.get()
                                                                                                                                                                                        # data['type'] = type.get()
                                                                                                                                                                                        # data['name'] = entry1.get()
                                                                                                                                                                                        # data['commission'] = entry4.get()
                                                                                                                                                                                        # master.after(1000,master.update)
        
        # data = {'salary': salaryentry.get(),'name':entry1.get(), 'address':entry2.get(), 'type': type.get()}
        #btnSubmit = Button(exitButtonContainer, text='Submit',command=lambda arg1=win,arg2=data: submit(win,data))
        btnSubmit = Button(exitButtonContainer, text='Submit', command=lambda arg1=salaryentry.get(), arg2=entry2.get(),arg3=type.get(), arg4=entry1.get(),arg5=master : submit(name=entry1.get(),address=entry2.get(),type=type.get(),commission=entry4.get(),win=master,salary=salaryentry.get()))
        btnSubmit.pack(side=RIGHT)

        #'commission':entry4.get()
        # print([entry4.get()])
        # print([entry1.get()])

    def rmvEmployee(self):
        win = Toplevel(menu) #creates a new window
        master = win
        win.title("Remove Employee")
        win.geometry('300x150')
        win.resizable(False,False)


        titleContainer = Frame(win)
        titleContainer.pack()
        title = Label(titleContainer,text='Insert employee ID',font=('Arial','11','bold'))
        title.pack()
        idTxt = Frame(win)
        _id = Entry(idTxt)
        idTxt.pack(pady=5,fill=X)
        _id.pack(fill=X,expand=TRUE,padx=5)
        #print([_id.get()])

        exitButtonContainer = Frame(master,pady=5,borderwidth=1)
        exitButtonContainer.pack(side=BOTTOM,fill=X)
        btnExit = Button(exitButtonContainer,text='Back',command=win.destroy)
        btnExit.pack(side=LEFT)
        #menu.wm_deiconify()

        #TODO #2 show who has been removed
        # ----- submit -----
        btnSubmit = Button(exitButtonContainer, text='Remove',command=lambda arg1=_id.get(): employeeRemover(_id.get()))
        #btnSubmit = Button(exitButtonContainer, text='Remove',command=lambda arg1=_id.get(): print(_id.get()))
        btnSubmit.pack(side=RIGHT)
        pass
    
    def changeEmployee(self):
        win = Toplevel(menu)
        master = win
        win.title("Change Employee")
        win.resizable(TRUE,False)
        
        #title + idsearch
        titleContainer = Frame(win)
        titleContainer.pack()
        title = Label(titleContainer,text=' Insert employee ID',font=('Arial','11','bold'))
        title.pack()
        idContainer = Frame(win)
        _id = Entry(idContainer)
        idContainer.pack(side=TOP,fill=X)
        _id.pack(padx=5,fill=X,expand=TRUE)
        searchBtn = Button(idContainer,text='Search',command=lambda arg1 = master,arg2=_id.get(),arg3=True : employeeSearcher(master,_id.get(),True))
        searchBtn.pack(side=RIGHT)
        
        # ----- checkbar -----
            # numbers                   0      1        2           3              4             5              6
            #chk = checkbar(master,['Name','Address','Type,'Method of Payment','Union Status','Union ID','Union Fee'])
            #chk.pack()
            #chk.state()
        sep = ttk.Separator(master,orient='horizontal')
        sep.pack(fill=BOTH,pady=5)


        lbl1 = Label(master,text='Type what you want to change and leave the rest blank',font=('Arial','10','bold'))
        lbl1.pack(pady=5,padx=5)
        _name = Container(master,'Name')
        _address = Container(master,'Address')
        _type = ContainerCombobox(master,'Type    ',['hourist','salaried','commissioned'])
        _salary = Container(master,'Salary' )
        _commission = Container(master,'Commission')
        
        containerCombobox = Frame(master)
        containerCombobox.pack()
        options=['Bank account deposit','Postal Service','Check on hands']
        _paymentLabel = Label(containerCombobox,text='Payment   ')
        _paymentLabel.pack(side=LEFT,padx=30)
        _payment = StringVar(master)
        _payment.set(options[0])
        _paymentChooser = ttk.Combobox(containerCombobox,state='readonly',values=options,textvariable=_payment)
        _paymentChooser.pack(side=RIGHT)

        _unionStatus = ContainerCombobox(master,'Union Status  ',[False, True] )
        #_unionStatus = Container(master,'Union Status')
        _unionID = Container(master,'Union ID')
        _unionFee = Container(master,'Union Fee')
        #arg1=master, arg2= _name, arg3= _type, arg4=_salary, arg5=_commission, arg6=_payment, arg7=_unionStatus, arg8=_unionID, arg9=_unionFee, arg10= _address
        
    
        # ----- exit button ------
        exitButtonContainer = Frame(master,pady=5,borderwidth=1)
        exitButtonContainer.pack(side=BOTTOM,fill=X)
        btnExit = Button(exitButtonContainer,text='Back',command=win.destroy)
        btnExit.pack(side=LEFT)

        #TODO #3 show what has been changed
        # ----- submit -----
        
        btnSubmit = Button(exitButtonContainer, text='Change',
        command=lambda  arg1= master, 
                        arg2= _name.get(),
                        arg3= _type.get(),
                        arg4=_salary.get(), 
                        arg5=_commission.get(), 
                        arg6=_payment.get(), 
                        arg7=_unionStatus.get(), 
                        arg8=_unionID.get(),
                        arg9=_unionFee.get(), 
                        arg10=_address.get(),
                        arg11=_id.get(): 
                        employeeChanger(master=master,name=_name.get(),type=_type.get(),
                                        salary=_salary.get(),commission=_commission.get(),
                                        payment=_payment.get(),unionStatus=_unionStatus.get(),
                                        unionID=_unionID.get(),unionFee=_unionFee.get(),
                                        address=_address.get(),employeeID=_id.get()))
        btnSubmit.pack(side=RIGHT)

    def sendPoint(self):
        master = Toplevel(menu)
        master.title('Send Electronic Point Data')
        master.resizable(False,False)

        _id = windowTitleAndSearch(master,'Insert ID of the employee')

        arrival = Container(master,"Arrival")
        leaving = Container(master,"Leaving")

        exitButtonContainer = Frame(master,pady=5,borderwidth=1)
        exitButtonContainer.pack(side=BOTTOM,fill=X)
        btnExit = Button(exitButtonContainer,text='Back',command=master.destroy)
        btnExit.pack(side=LEFT)

        # ----- submit -----
        #TODO #4 create a button that commands a function to send the point data
        btnSubmit = Button(exitButtonContainer, text='Send',command=lambda arg1=_id.get(),arg2=master,arg3=arrival.get(),arg4=leaving.get(): pointSender(master,_id.get(),arrival.get(),leaving.get()))
        btnSubmit.pack(side=RIGHT)
    
    def sendSale(self):
        master = Toplevel(menu)
        master.title('Send Sale Data')
        master.resizable(False,False)

        _id = windowTitleAndSearch(master,'Insert ID of the employee')

        sale = Container(master,"Sale Price")

        exitButtonContainer = Frame(master,pady=5,borderwidth=1)
        exitButtonContainer.pack(side=BOTTOM,fill=X)
        btnExit = Button(exitButtonContainer,text='Back',command=master.destroy)
        btnExit.pack(side=LEFT)

        # ----- submit -----
        #TODO config submit button
        btnSubmit = Button(exitButtonContainer, text='Send',command=lambda arg1=_id.get(),arg2=master,arg3=sale.get(): saleSender(master,_id.get(),sale.get()))
        btnSubmit.pack(side=RIGHT)
    
    def sendTax(self):
        master = Toplevel(menu)
        master.title('Send Union Service Fee')
        master.resizable(False,False)

        _id = windowTitleAndSearch(master,'Insert ID of the employee')

        fee = Container(master,"Fee")

        exitButtonContainer = Frame(master,pady=5,borderwidth=1)
        exitButtonContainer.pack(side=BOTTOM,fill=X)
        btnExit = Button(exitButtonContainer,text='Back',command=master.destroy)
        btnExit.pack(side=LEFT)

        # ----- submit -----
        #TODO config submit button
        btnSubmit = Button(exitButtonContainer, text='Send Fee',command=lambda arg1=_id.get(),arg2=fee.get(): feeSender(master,_id.get(),fee.get()))
        btnSubmit.pack(side=RIGHT)
    
    def changePayday(self):
        master = Toplevel(menu)
        master.title('Change Payday')
        master.resizable(False,False)
        master.geometry('300x250+30+30')

        title = windowTitleAndSearch(master,'Insert ID of the employee')

        container4 = Frame(master)
        container4.pack()
        #TODO #5 add new options dinamically using some sort of database
        options = ['Weekly','Monthly','Bi-Weekly']
        payday = StringVar()
        payday.set(options[0])
        paydayChooser = ttk.Combobox(container4,state='readonly',values=options,textvariable=payday)
        paydayChooser.pack(side=RIGHT)

        exitButtonContainer = Frame(master,pady=5,borderwidth=1)
        exitButtonContainer.pack(side=BOTTOM,fill=X)
        btnExit = Button(exitButtonContainer,text='Back',command=master.destroy)
        btnExit.pack(side=LEFT)

        # ----- submit -----
        #todo config submit button
        #btnSubmit = Button(exitButtonContainer, text='Change',command=lambda arg1=_id.get(): employeeChanger(_id.get()))
        #btnSubmit.pack(side=RIGHT)pass

    def createPayday(self):
        master = Toplevel(menu)
        master.title('Create Payday')
        master.resizable(False,False)

        title = windowTitleAndSearch(master,'Insert ID of the employee')

        sale = Container(master,"New Payday")

        exitButtonContainer = Frame(master,pady=5,borderwidth=1)
        exitButtonContainer.pack(side=BOTTOM,fill=X)
        btnExit = Button(exitButtonContainer,text='Back',command=master.destroy)
        btnExit.pack(side=LEFT)

        # ----- submit -----
        #todo config submit button
        #btnSubmit = Button(exitButtonContainer, text='Change',command=lambda arg1=_id.get(): employeeChanger(_id.get()))
        #btnSubmit.pack(side=RIGHT)

    def runPayroll(self):
        master = Toplevel(menu)
        master.title('Make Payments')
        master.resizable(False,False)

        container1 = Frame(master)
        lbl1 = Label(master,text='Here are the employees that are to recieve today:')
        container1.pack()
        lbl1.pack()
        
        exitButtonContainer = Frame(master,pady=5,borderwidth=1)
        exitButtonContainer.pack(side=BOTTOM,fill=X)
        btnExit = Button(exitButtonContainer,text='Back',command=master.destroy)
        btnExit.pack(side=LEFT)

        # ----- submit -----
        #todo config submit button
        btnSubmit = Button(exitButtonContainer, text='Pay')#command=lambda arg1=_id.get(): employeeChanger(_id.get())
        btnSubmit.pack(side=RIGHT)

menu = Tk()
app = Menu(menu)
menu.title("Payroll System")
menu.geometry('340x620+600+40')
#print(a)
menu.resizable(False,True)
menu.mainloop()