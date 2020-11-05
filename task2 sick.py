#Importing everything from tkinter
from tkinter import *

window = Tk()
#Giving my window a title
window.title("StudentNo: 9912225158085")
#Giving my window a size
window.configure(width=500, height=500)
window.configure(background="cyan")

sick_code = Label(text="Sickness Code:", padx="21", pady="20")
window.configure(background="cyan")
#Setting my label to be in the middle
sick_code.grid(row=0, column=0)
sick_code_entry = Entry(window)
#Setting my entry textbox to be in the middle
sick_code_entry.grid(row=0,column=3)

#Making a label
treatment_duration = Label(text="Duration Of Treatment:", padx="21", pady="20")
window.configure(background="cyan")
#Setting my label to be in the middle
treatment_duration.grid(row=2, column=0)
treatment_duration_entry = Entry(window)
#Setting my entry textbox to be in the middle
treatment_duration_entry.grid(row=2,column=3)
#Making a label
treatment_duration = Label(text="Weeks/Months", padx="21", pady="20")
window.configure(background="cyan")
#Setting my label to be in the middle
treatment_duration.grid(row=2, column=5)
#Making a label
doc_Prac_Num = Label(text="Doctors Practical Number:", padx="21", pady="20")
#Setting my label to be in the middle
doc_Prac_Num.grid(row=4, column=0)
doc_Prac_entry = Entry(window)
#Setting my entry textbox to be in the middle
doc_Prac_entry.grid(row=4,column=3)
window.configure(background="cyan")
#Making a label
scan_fee = Label(text="Scan/Consultation Fee:", padx="21", pady="20")
window.configure(background="cyan")
#Setting my label to be in the middle
scan_fee.grid(row=6, column=0)
scan_fee_entry = Entry(window)
#Setting my entry textbox to be in the middle
scan_fee_entry.grid(row=6,column=3)

#Making a label
treatment_amount = Label(text="Amount Paid For Treatment:", padx="21", pady="20")
window.configure(background="cyan")
#Setting my label to be in the middle
treatment_amount.grid(row=12, column=0)

class Sick:
    pass

class influenza(Sick):
    def __init__(self, med, consultation):
        self.med =med
        self.consultation=consultation

    def treatment_amount(self,med,consultation):
        if self.consultation>600:
            self.amount=self.med+self.consultation*0.98
            print(self.amount)
obj_gd1=influenza(0,0)

obj_gd1.med=350.50
obj_gd1.consultation=800
obj_gd1.treatment_amount(6,5)


class cancer(Sick):
    def __init__(self,scanfee,med):
        self.scanfee =scanfee
        self.med = 400
        x = 600
        if self.scanfee > x:
            print("we can't help")
        else:
            amount= self.med+self.scanfee
            print(amount)

object = cancer(0,0)
print(cancer)


choose = IntVar()
Radiobutton(window,text="Cancer",padx = 20,variable=choose,value=1).grid(row=14,column=0)
Radiobutton(window,text="Influenza",padx = 20,variable=choose,value=2).grid(row=16,column=0)

def calc 









 calc_button = Button(window, text="Calculate", bg="grey",command=calc)
 calc_button.grid(row=18,column=0)
def clear():
  sick_code_entry.delete(0,END)
  treatment_duration_entry.delete(0,END)
  doc_Prac_entry.delete(0, END)
  scan_fee_entry.delete(0, END)


#Button to Clear the program
clear_button = Button(window, text="Clear", bg="grey", command=clear)
clear_button.grid(row=18,column=3)

window.mainloop()
