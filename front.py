from tkinter import *
import backend

def get_selected_row(event):
    try:
         global selected_tuple
         index=list1.curselection()[0]
         selected_tuple=list1.get(index)
         e1.delete(0,END)
         e1.insert(END,selected_tuple[0])
         e2.delete(0,END)
         e2.insert(END,selected_tuple[1])
         e3.delete(0,END)
         e3.insert(END,selected_tuple[2])
         e4.delete(0,END)
         e4.insert(END,selected_tuple[3])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for things in backend.view():
        list1.insert(END,things)

def search_command():
    list1.delete(0,END)
    for things in backend.search(e1.get(),e2.get(),e3.get(),e4.get()):
        list1.insert(END,things)

def add_command():
    backend.insert(e1.get(),e2.get(),e3.get(),e4.get())
    list1.delete(0,END)
    list1.insert(END,(e1.get(),e2.get(),e3.get(),e4.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],e2.get(),e3.get(),e4.get())


window=Tk()
window.wm_title("Logistic Tracker")

#Grid.rowconfigure(window, 0, weight=1)
#Grid.columnconfigure(window, 0, weight=1)

l1=Label(window,text= "Date")
l1.grid(row=0,column=0,sticky=N+S+E+W)

l2=Label(window,text="Material Reciept Report")
l2.grid(row=0,column=2,sticky=N+S+E+W)

l3=Label(window,text="Vehicle No.")
l3.grid(row=0,column=4,sticky=N+S+E+W)

l4=Label(window,text="Owner's Name")
l4.grid(row=0,column=6,sticky=N+S+E+W)

l5=Label(window,text="Delivery Challan No.")
l5.grid(row=0,column=8,sticky=N+S+E+W)

l6=Label(window,text="Loading Point")
l6.grid(row=0,column=10,sticky=N+S+E+W)

l7=Label(window,text="Unloading Point")
l7.grid(row=1,column=0,sticky=N+S+E+W)

l8=Label(window,text="RST No.")
l8.grid(row=1,column=2,sticky=N+S+E+W)

l9=Label(window,text="Loading Date")
l9.grid(row=1,column=4,sticky=N+S+E+W)

l10=Label(window,text="Loading Weight")
l10.grid(row=1,column=6,sticky=N+S+E+W)

l11=Label(window,text="Unloading Weight")
l11.grid(row=1,column=8,sticky=N+S+E+W)

l12=Label(window,text="Material Reciept Date")
l12.grid(row=1,column=10,sticky=N+S+E+W)

l13=Label(window,text="Advance")
l13.grid(row=2,column=0,sticky=N+S+E+W)

l14=Label(window,text="Diesel(Ltr)")
l14.grid(row=2,column=2,sticky=N+S+E+W)

l15=Label(window,text="Diesel(Rs)")
l15.grid(row=2,column=4,sticky=N+S+E+W)

l16=Label(window,text="Unloading Charges")
l16.grid(row=2,column=6,sticky=N+S+E+W)

l17=Label(window,text="Other Amount")
l17.grid(row=2,column=8,sticky=N+S+E+W)

l18=Label(window,text="Remark")
l18.grid(row=2,column=10,sticky=N+S+E+W)

l19=Label(window,text="Rate")
l19.grid(row=3,column=0,sticky=N+S+E+W)

l20=Label(window,text="Freight")
l20.grid(row=3,column=2,sticky=N+S+E+W)

l21=Label(window,text="Comm")
l21.grid(row=3,column=4,sticky=N+S+E+W)

l22=Label(window,text="Balance")
l22.grid(row=3,column=6,sticky=N+S+E+W)

date=StringVar()
e1=Entry(window,textvariable="date")
e1.grid(row=0,column=1,sticky=N+S+E+W)

mrr=StringVar()
e2=Entry(window,textvariable="mrr")
e2.grid(row=0,column=3,sticky=N+S+E+W)

vehicle=StringVar()
e3=Entry(window,textvariable="vehicle")
e3.grid(row=0,column=5,sticky=N+S+E+W)

owner=StringVar()
e4=Entry(window,textvariable="owner")
e4.grid(row=0,column=7,sticky=N+S+E+W)

delno=StringVar()
e5=Entry(window,textvariable="delno")
e5.grid(row=0,column=9,sticky=N+S+E+W)

loadp=StringVar()
e6=Entry(window,textvariable="Loadp")
e6.grid(row=0,column=11,sticky=N+S+E+W)

Unloadp=StringVar()
e7=Entry(window,textvariable="Unloadp")
e7.grid(row=1,column=1,sticky=N+S+E+W)

rst=StringVar()
e8=Entry(window,textvariable="rst")
e8.grid(row=1,column=3,sticky=N+S+E+W)

ld=StringVar()
e9=Entry(window,textvariable="ld")
e9.grid(row=1,column=5,sticky=N+S+E+W)

lw=StringVar()
e10=Entry(window,textvariable="lw")
e10.grid(row=1,column=7,sticky=N+S+E+W)

uw=StringVar()
e11=Entry(window,textvariable="uw")
e11.grid(row=1,column=9,sticky=N+S+E+W)

mrd=StringVar()
e12=Entry(window,textvariable="mrd")
e12.grid(row=1,column=11,sticky=N+S+E+W)

ad=StringVar()
e13=Entry(window,textvariable="ad")
e13.grid(row=2,column=1,sticky=N+S+E+W)

dltr=StringVar()
e14=Entry(window,textvariable="dltr")
e14.grid(row=2,column=3,sticky=N+S+E+W)

drs=StringVar()
e15=Entry(window,textvariable="drs")
e15.grid(row=2,column=5,sticky=N+S+E+W)

uc=StringVar()
e16=Entry(window,textvariable="uc")
e16.grid(row=2,column=7,sticky=N+S+E+W)

oa=StringVar()
e17=Entry(window,textvariable="oa")
e17.grid(row=2,column=9,sticky=N+S+E+W)

remark=StringVar()
e18=Entry(window,textvariable="remark")
e18.grid(row=2,column=11,sticky=N+S+E+W)

rate=StringVar()
e19=Entry(window,textvariable="rate")
e19.grid(row=3,column=1,sticky=N+S+E+W)

fr=StringVar()
e20=Entry(window,textvariable="fr")
e20.grid(row=3,column=3,sticky=N+S+E+W)

comm=StringVar()
e21=Entry(window,textvariable="comm")
e21.grid(row=3,column=5,sticky=N+S+E+W)

bal=StringVar()
e22=Entry(window,textvariable="bal")
e22.grid(row=3,column=7,sticky=N+S+E+W)


list1=Listbox(window,height=20,width=35)
list1.grid(row=6,rowspan=20,columnspan=12,sticky=N+S+E+W)

sb1=Scrollbar(window)
sb1.grid(row=6,column=12,rowspan=20,sticky=N+S+E+W)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

sb2=Scrollbar(window, orient = HORIZONTAL)
sb2.grid(row=30,column=0,columnspan=12,sticky=N+S+E+W)

list1.configure(xscrollcommand=sb2.set)
sb2.configure(command=list1.xview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b2=Button(window,text="view products",width=12,command=view_command)
b2.grid(row=5,column=3,sticky=N+S+E+W)

b3=Button(window,text="search product",width=12,command=search_command)
b3.grid(row=5,column=4,sticky=N+S+E+W)

b4=Button(window,text="Add new",width=12,command=add_command)
b4.grid(row=5,column=5,sticky=N+S+E+W)

b5=Button(window,text="update list",width=12,command=update_command)
b5.grid(row=5,column=6,sticky=N+S+E+W)

b6=Button(window,text="delete selected",width=12,command=delete_command)
b6.grid(row=5,column=7,sticky=N+S+E+W)

b7=Button(window,text="close manager",width=12,command=window.destroy)
b7.grid(row=5,column=8,sticky=N+S+E+W)

window.mainloop()
