from Tkinter import *
import sqlite3
import Tkinter
import  tkMessageBox
import ttk

def add_c():
    root = Tk()
    root.title("Balaji Pakaging")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 900
    height = 600
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)

    # ==================================METHODS============================================
    def Database():
        global conn, cursor
        conn = sqlite3.connect('pythontut.db')
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `company` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Name TEXT, GSTIN TEXT, Address1 TEXT, Address2 TEXT, Address3 TEXT,Address4 TEXT,Address5 TEXT, State Address VARCHAR(15), p_terms INT)")

    def Create():
        if Name.get() == "" or Address1.get() == "" or state.get() == "" or p_terms.get() == "":
            txt_result.config(text="Please complete the required field!", fg="red")
        else:
            Database()
            cursor.execute(
                "INSERT INTO `company` (Name, GSTIN, Address1,Address2,Address3,Address4,Address5, state, p_terms) VALUES(?, ?, ?, ?, ?, ?,?,?,?)",
                (str(Name.get()), str(GSTIN.get()), str(Address1.get()), str(Address2.get()), str(Address3.get()),
                 str(Address4.get()), str(Address5.get()), str(state.get()), str(pterms.get()),
                 ))
            conn.commit()
            """Name.set("")
            GSTIN.set("")
            Address1.set("")
            #state.set("")
            #pterms.set("")
            cursor.close()"""
            conn.close()
            txt_result.config(text="Created a data!", fg="green")

    def Read():
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `company` ORDER BY `Name` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end',
                        values=(data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]))
        cursor.close()
        conn.close()
        txt_result.config(text="Successfully read the data from database", fg="black")

    def select(event):
        Database()
        dat1=tree.selection()[0]
        data = tree.item(tree.selection())['values'][0]
        cursor.execute("DELETE FROM company WHERE Name=(?)", (data,))
        print data
        conn.commit()
        cursor.close()
        # deleta campo da lista
        tree.delete(dat1)

    def Exit():
        result = tkMessageBox.askquestion('Balaji packging', 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            root.destroy()
            exit()

    # ==================================VARIABLES==========================================
    Name = StringVar()
    GSTIN = StringVar()
    Address1 = StringVar()
    Address2 = StringVar()
    Address3 = StringVar()
    Address4 = StringVar()
    Address5 = StringVar()
    p_terms = StringVar()
    state = StringVar()
    PASSWORD = StringVar()

    # ==================================FRAME==============================================
    Top = Frame(root, width=900, height=50, bd=8, relief="raise")
    Top.pack(side=TOP)
    Left = Frame(root, width=300, height=700, bd=8, relief="raise")
    Left.pack(side=LEFT)
    Right = Frame(root, width=600, height=500, bd=8, relief="raise")
    Right.pack(side=RIGHT)
    Forms = Frame(Left, width=300, height=450)
    Forms.pack(side=TOP)
    Buttons = Frame(Left, width=300, height=100, bd=8, relief="raise")
    Buttons.pack(side=BOTTOM)
    # RadioGroup = Frame(Forms)
    # Male = Radiobutton(RadioGroup, text="Male", variable=GENDER, value="Male", font=('arial', 16)).pack(side=LEFT)
    # Female = Radiobutton(RadioGroup, text="Female", variable=GENDER, value="Female", font=('arial', 16)).pack(side=LEFT)

    # ==================================LABEL WIDGET=======================================
    txt_title = Label(Top, width=900, font=('arial', 24), text="Balaji Pakaging")
    txt_title.pack()
    txt_firstname = Label(Forms, text="Name:", font=('arial', 16), bd=15)
    txt_firstname.grid(row=0, stick="e")
    txt_lastname = Label(Forms, text="GSTIN:", font=('arial', 16), bd=15)
    txt_lastname.grid(row=1, stick="e")
    txt_gender = Label(Forms, text="Address:", font=('arial', 16), bd=15)
    txt_gender.grid(row=2, stick="e")
    txt_address = Label(Forms, text="Payment Terms", font=('arial', 16), bd=15)
    txt_address.grid(row=7, stick="e")
    txt_username = Label(Forms, text="State", font=('arial', 16), bd=15)
    txt_username.grid(row=8, stick="e")
    # txt_password = Label(Forms, text="Payment terms:", font=('arial', 16), bd=15)
    # txt_password.grid(row=9, stick="e")
    txt_result = Label(Buttons)
    txt_result.pack(side=TOP)

    # ==================================ENTRY WIDGET=======================================
    firstname = Entry(Forms, textvariable=Name, width=30)
    firstname.grid(row=0, column=1)
    lastname = Entry(Forms, textvariable=GSTIN, width=30)
    lastname.grid(row=1, column=1)
    # RadioGroup.grid(row=2, column=1)
    address1 = Entry(Forms, textvariable=Address1, width=30)
    address1.grid(row=2, column=1)
    address2 = Entry(Forms, textvariable=Address2, width=30)
    address2.grid(row=3, column=1)
    address3 = Entry(Forms, textvariable=Address3, width=30)
    address3.grid(row=4, column=1)
    address4 = Entry(Forms, textvariable=Address4, width=30)
    address4.grid(row=5, column=1)
    address5 = Entry(Forms, textvariable=Address5, width=30)
    address5.grid(row=6, column=1)
    state = Entry(Forms, textvariable=state, width=30)
    state.grid(row=7, column=1)
    pterms = Entry(Forms, textvariable=p_terms, width=30)
    pterms.grid(row=8, column=1)

    # ==================================BUTTONS WIDGET=====================================
    btn_create = Button(Buttons, width=10, text="Create", command=Create)
    btn_create.pack(side=LEFT)
    btn_read = Button(Buttons, width=10, text="Read", command=Read)
    btn_read.pack(side=LEFT)
    btn_update = Button(Buttons, width=10, text="Update", command=apagar)
    btn_update.pack(side=LEFT)
    btn_delete = Button(Buttons, width=10, text="Delete", state=DISABLED)
    btn_delete.pack(side=LEFT)
    btn_exit = Button(Buttons, width=10, text="Exit", command=Exit)
    btn_exit.pack(side=LEFT)

    # ==================================LIST WIDGET========================================
    scrollbary = Scrollbar(Right, orient=VERTICAL)
    scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
    tree = ttk.Treeview(Right, columns=(
    "Name", "GSTIN", "Address", "Address2", "Address3", "Address4", "Address5", "State", "Payment Terms"),
                        selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.bind("<KeyPress-Delete>", select)
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('GSTIN', text="GSTIN", anchor=W)
    tree.heading('Address', text="Address", anchor=W)
    tree.heading('Address2', text="Address", anchor=W)
    tree.heading('Address3', text="Address", anchor=W)
    tree.heading('Address4', text="Address", anchor=W)
    tree.heading('Address5', text="Address", anchor=W)
    tree.heading('State', text="State", anchor=W)
    tree.heading('Payment Terms', text="Payment Terms", anchor=W)
    # tree.heading('Password', text="Password", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=80)
    tree.column('#2', stretch=YES, minwidth=0, width=120)
    tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=80)
    tree.column('#5', stretch=NO, minwidth=0, width=80)
    tree.column('#6', stretch=NO, minwidth=0, width=80)
    tree.column('#7', stretch=NO, minwidth=0, width=80)
    tree.column('#8', stretch=NO, minwidth=0, width=80)
    # tree.column('#9', stretch=NO, minwidth=0, width=80)
    # tree.column('#6', stretch=NO, minwidth=0, width=120)
    tree.pack()

    # ==================================INITIALIZATION=====================================
    if __name__ == '__main__':
        root.mainloop()
def add_cc():
    root = Tk()
    root.title("Balaji Pakaging")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 900
    height = 600
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)

    # ==================================METHODS============================================
    def Database():
        global conn, cursor
        conn = sqlite3.connect('pythontut.db')
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `product` (Name1 TEXT,Price INTEGER, product_id VARCAHR)")

    def Create():
        if Name1.get() == "" or Price.get() == "" or product_id.get() == "" :
            txt_result.config(text="Please complete the required field!", fg="red")
        else:
            Database()
            cursor.execute(
                "INSERT INTO `product` (Name1, Price,product_id) VALUES(?, ?, ?)",
                (str(Name1.get()), str(Price.get()), str(product_id.get())))
            conn.commit()
            """Name.set("")
            GSTIN.set("")
            Address1.set("")
            #state.set("")
            #pterms.set("")
            cursor.close()"""
            conn.close()
            txt_result.config(text="Created a data!", fg="green")

    def Read():
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `product` ORDER BY `Name1` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end',
                        values=(data[0], data[1], data[2]))
        cursor.close()
        conn.close()
        txt_result.config(text="Successfully read the data from database", fg="black")

    def select(event):
        Database()
        dat1=tree.selection()[0]
        data = tree.item(tree.selection())['values'][0]
        cursor.execute("DELETE FROM product WHERE Name1=(?)", (data,))
        print data
        conn.commit()
        cursor.close()
        # deleta campo da lista
        tree.delete(dat1)

    def Exit():
        result = tkMessageBox.askquestion('Balaji packging', 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            root.destroy()
            exit()

    # ==================================VARIABLES==========================================
    Name1 = StringVar()
    Price = StringVar()
    product_id = StringVar()
    Address2 = StringVar()
    Address3 = StringVar()
    Address4 = StringVar()
    Address5 = StringVar()
    p_terms = StringVar()
    state = StringVar()
    PASSWORD = StringVar()

    # ==================================FRAME==============================================
    Top = Frame(root, width=900, height=50, bd=8, relief="raise")
    Top.pack(side=TOP)
    Left = Frame(root, width=300, height=700, bd=8, relief="raise")
    Left.pack(side=LEFT)
    Right = Frame(root, width=600, height=500, bd=8, relief="raise")
    Right.pack(side=RIGHT)
    Forms = Frame(Left, width=300, height=450)
    Forms.pack(side=TOP)
    Buttons = Frame(Left, width=300, height=100, bd=8, relief="raise")
    Buttons.pack(side=BOTTOM)
    # RadioGroup = Frame(Forms)
    # Male = Radiobutton(RadioGroup, text="Male", variable=GENDER, value="Male", font=('arial', 16)).pack(side=LEFT)
    # Female = Radiobutton(RadioGroup, text="Female", variable=GENDER, value="Female", font=('arial', 16)).pack(side=LEFT)

    # ==================================LABEL WIDGET=======================================
    txt_title = Label(Top, width=900, font=('arial', 24), text="Balaji Pakaging")
    txt_title.pack()
    txt_firstname = Label(Forms, text="Custommer Name:", font=('arial', 16), bd=15)
    txt_firstname.grid(row=0, stick="e")
    txt_lastname = Label(Forms, text="PRICE :", font=('arial', 16), bd=15)
    txt_lastname.grid(row=1, stick="e")
    txt_gender = Label(Forms, text="Product ID:", font=('arial', 16), bd=15)
    txt_gender.grid(row=2, stick="e")

    # txt_password = Label(Forms, text="Payment terms:", font=('arial', 16), bd=15)
    # txt_password.grid(row=9, stick="e")
    txt_result = Label(Buttons)
    txt_result.pack(side=TOP)

    # ==================================ENTRY WIDGET=======================================
    firstname = Entry(Forms, textvariable=Name1, width=30)
    firstname.grid(row=0, column=1)
    lastname = Entry(Forms, textvariable=Price, width=30)
    lastname.grid(row=1, column=1)
    # RadioGroup.grid(row=2, column=1)
    address1 = Entry(Forms, textvariable=product_id, width=30)
    address1.grid(row=2, column=1)
    """address2 = Entry(Forms, textvariable=Address2, width=30)
    address2.grid(row=3, column=1)
    address3 = Entry(Forms, textvariable=Address3, width=30)
    address3.grid(row=4, column=1)
    address4 = Entry(Forms, textvariable=Address4, width=30)
    address4.grid(row=5, column=1)
    address5 = Entry(Forms, textvariable=Address5, width=30)
    address5.grid(row=6, column=1)
    state = Entry(Forms, textvariable=state, width=30)
    state.grid(row=7, column=1)
    pterms = Entry(Forms, textvariable=p_terms, width=30)
    pterms.grid(row=8, column=1)"""

    # ==================================BUTTONS WIDGET=====================================
    btn_create = Button(Buttons, width=10, text="Create", command=Create)
    btn_create.pack(side=LEFT)
    btn_read = Button(Buttons, width=10, text="Delete", command=Read)
    btn_read.pack(side=LEFT)

    btn_exit = Button(Buttons, width=10, text="Exit", command=Exit)
    btn_exit.pack(side=LEFT)

    # ==================================LIST WIDGET========================================
    scrollbary = Scrollbar(Right, orient=VERTICAL)
    scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
    tree = ttk.Treeview(Right, columns=(
    "Name1", "Price", "product_id"),
                        selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.bind("<KeyPress-Delete>", select)
    tree.heading('Name1', text="Name", anchor=W)
    tree.heading('Price', text="Price", anchor=W)
    tree.heading('product_id', text="product_id", anchor=W)
    """tree.heading('Address2', text="Address", anchor=W)
    tree.heading('Address3', text="Address", anchor=W)
    tree.heading('Address4', text="Address", anchor=W)
    tree.heading('Address5', text="Address", anchor=W)
    tree.heading('State', text="State", anchor=W)
    tree.heading('Payment Terms', text="Payment Terms", anchor=W)
    # tree.heading('Password', text="Password", anchor=W)"""
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=80)
    tree.column('#2', stretch=YES, minwidth=0, width=120)
    """tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=80)
    tree.column('#5', stretch=NO, minwidth=0, width=80)
    tree.column('#6', stretch=NO, minwidth=0, width=80)
    tree.column('#7', stretch=NO, minwidth=0, width=80)
    tree.column('#8', stretch=NO, minwidth=0, width=80)
    # tree.column('#9', stretch=NO, minwidth=0, width=80)
    # tree.column('#6', stretch=NO, minwidth=0, width=120)"""
    tree.pack()

    # ==================================INITIALIZATION=====================================
    if __name__ == '__main__':
        root.mainloop()
add_cc()
