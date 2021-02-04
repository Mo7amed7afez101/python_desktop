from tkinter import *
import math, random
from tkinter import messagebox

window = Tk()
window.geometry("1220x675+0+0")
window.title("billing software".capitalize())

# **************************************************
# *****================= Code =================*****
# **************************************************
# =====> Variables For All Entry In Design

bg_color = "#074463"
fg_color = "white"

# prices of products
red_meat_price = 120
lean_meat_price = 120
cold_meat_price = 120
calf_liver_price = 130
head_meat_price = 60
calf_tripe_price = 30
vasha_price = 40
fats_price = 10
calf_trotters_price = 50

red_meat = IntVar()
lean_meat = IntVar()
cold_meat = IntVar()
calf_liver = IntVar()
head_meat = IntVar()
calf_tripe = IntVar()
vasha = IntVar()
fats = IntVar()
calf_trotters = IntVar()

# Customers Details
c_name = StringVar()
c_phone = StringVar()
bill_no = StringVar()
x = random.randint(1000, 9999)
bill_no.set(str(x))

total_meat_price = IntVar()
meat_tax = IntVar()
total_new_meat_price = IntVar()
new_meat_tax = IntVar()


# =============================================================
# ======================= Functions ===========================
# =============================================================
def total():
    meat_price = float(
        (red_meat.get() * red_meat_price) +
        (lean_meat.get() * lean_meat_price) +
        (cold_meat.get() * cold_meat_price) +
        (calf_liver.get() * calf_liver_price)
    )
    new_meat_price = (
            (head_meat.get() * head_meat_price) +
            (calf_tripe.get() * calf_tripe_price) +
            (vasha.get() * vasha_price) +
            (fats.get() * fats_price) +
            (calf_trotters.get() * calf_trotters_price)
    )
    total_meat_price.set(str(meat_price))
    total_new_meat_price.set(new_meat_price)


# welcome Billing Area
def welcome_bill():
    txtarea.delete(1.0, END)
    txtarea.insert(END, "\twelcome Billing Area\n")
    txtarea.insert(END, f"Bill No: {bill_no.get()}\n")
    txtarea.insert(END, f"Customer Name: {c_name.get()}\n")
    txtarea.insert(END, f"Customer Phone: {c_phone.get()}\n")
    txtarea.insert(END, "=" * 45 + "\n")
    # txtarea.insert(END, "Products".center(25).lstrip() + "Price".center(25).lstrip() + "QTY".center(25).lstrip() + "Price\n")
    txtarea.insert(END, "Products\tPrice\tQTY\tTotal Price\n")
    txtarea.insert(END, "=" * 45 + "\n")

def bill_area():
    if c_name.get() == "" or c_phone.get() == "" :
        messagebox.showerror("Error", "please fill customer details".title())
    elif total_meat_price.get() == 0 and total_new_meat_price.get == 0:
        messagebox.showerror("Error", "the user don't select product".title())
    else:
        # Generate Bill
        welcome_bill()
        if red_meat.get() != 0:
            txtarea.insert(END, f"Red Meat\t{red_meat_price}\t{red_meat.get()}\t{red_meat.get() * red_meat_price}\n")
        if lean_meat.get() != 0:
            txtarea.insert(END, f"Lean Meat\t{lean_meat_price}\t{lean_meat.get()}\t{lean_meat.get() * lean_meat_price}\n")
        if cold_meat.get() != 0:
            txtarea.insert(END, f"Cold Meat\t{cold_meat_price}\t{cold_meat.get()}\t{cold_meat.get() * cold_meat_price}\n")
        if calf_liver.get() != 0:
            txtarea.insert(END, f"Calf Liver\t{calf_liver_price}\t{calf_liver.get()}\t{calf_liver.get() * calf_liver_price}\n")
        if head_meat.get() != 0:
            txtarea.insert(END, f"Head Meat\t{head_meat_price}\t{head_meat.get()}\t{head_meat.get() * head_meat_price}\n")
        if calf_tripe.get() != 0:
            txtarea.insert(END, f"Calf Tripe\t{calf_tripe_price}\t{calf_tripe.get()}\t{calf_tripe.get() * calf_tripe_price}\n")
        if vasha.get() != 0:
            txtarea.insert(END, f"Vasha\t{vasha_price}\t{vasha.get()}\t{vasha.get() * vasha_price}\n")
        if fats.get() != 0:
            txtarea.insert(END, f"Fats\t{fats_price}\t{fats.get()}\t{fats.get() * fats_price}\n")
        if calf_trotters.get() != 0:
            txtarea.insert(END, f"Calf Trotters\t{calf_trotters_price}\t{calf_trotters.get()}\t{calf_trotters.get() * calf_trotters_price}\n")
        if total_meat_price.get() != 0:
            txtarea.insert(END, "-" * 45 + "\n")
            txtarea.insert(END, f"Total Meat Price: {total_meat_price.get()}\n")
            txtarea.insert(END, f"Total New Meat Price: {total_new_meat_price.get()}\n")
            txtarea.insert(END, f"Total Price: {total_new_meat_price.get() + total_meat_price.get()}\n")
            txtarea.insert(END, "-" * 45 + "\n")
        save_bill()

def save_bill():
    op = messagebox.askyesno("Save Bill", "Do You Want To Save The Bill?")
    if op > 0:
        bill_data = txtarea.get(1.0, END)
        f = open("bills/" + str(c_name.get()) + str(bill_no.get()) + ".txt", 'w')
        f.write(bill_data)
        f.close()

def clear_data():
    check_data = messagebox.askokcancel("info", "Do you clear all data?")
    if check_data > 0:
        red_meat.set(0)
        lean_meat.set(0)
        cold_meat.set(0)
        calf_liver.set(0)
        head_meat.set(0)
        calf_tripe.set(0)
        vasha.set(0)
        fats.set(0)
        calf_trotters.set(0)

        # Customers Details
        c_name.set("")
        c_phone.set("")
        bill_no.set("")

        total_meat_price.set(0)
        meat_tax.set(0)
        total_new_meat_price.set(0)
        new_meat_tax.set(0)
        # clear bill area
        txtarea.delete(1.0, END)
        welcome_bill()



# **************************************************
# ****================= Design =================****
# **************************************************

# Add widget here
title = Label(window, text="billing software", bg=bg_color, fg=fg_color, font=("times new roman",30,"bold"), pady=2, bd=12, relief=GROOVE)
title.pack(fill=X)

# ======> Add customer details
f1 = LabelFrame(window, text="Customer Details", bg=bg_color, fg="gold", font=("times new roman", 15, "bold"), bd=12, relief=GROOVE)
f1.place(x=0,y=80,relwidth=1)

cname_lbl = Label(f1, text="Customer Name", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=20, pady=5)
cname_entry = Entry(f1, width=15, font=("arial 15"), bd=7, relief=SUNKEN, textvariable=c_name).grid(row=0, column=1, pady=5)

cnumber_lbl = Label(f1, text="Phone no.", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold")).grid(row=0, column=2, padx=20, pady=5)
cnumber_entry = Entry(f1, width=15, font=("arial 15"), bd=7, relief=SUNKEN, textvariable=c_phone).grid(row=0, column=3, pady=5)

c_bill_lbl = Label(f1, text="Bill Number", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold")).grid(row=0, column=4, padx=20, pady=5)
c_bill_entry = Entry(f1, width=15, font=("arial 15"), bd=7, relief=SUNKEN, textvariable=bill_no).grid(row=0, column=5, pady=5)

# =====================================> End customer details
# ======> meats Frame
f2 = LabelFrame(window, text="Meats", bg=bg_color, fg="gold", font=("times new roman", 15, "bold"), bd=12, relief=GROOVE)
f2.place(x=5, y=170, width=400, height=350)

m1_lbl = Label(f2, text="Red Meat", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=20, pady=10)
m1_enter = Entry(f2, width=15, bg="#999", fg=fg_color, font=("arial 15"), bd=7, relief=SUNKEN, textvariable=red_meat).grid(row=0, column=1, pady=10)

m2_lbl = Label(f2, text="Lean Meat", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold")).grid(row=1, column=0, padx=20, pady=10)
m2_enter = Entry(f2, width=15, bg="#999", fg=fg_color, font=("arial 15"), bd=7, relief=SUNKEN, textvariable=lean_meat).grid(row=1, column=1, pady=10)

m3_lbl = Label(f2, text="Cold Meat", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold")).grid(row=2, column=0, padx=20, pady=10)
m3_enter = Entry(f2, width=15, bg="#999", fg=fg_color, font=("arial 15"), bd=7, relief=SUNKEN, textvariable=cold_meat).grid(row=2, column=1, pady=10)

m4_lbl = Label(f2, text="Calf Liver", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold")).grid(row=3, column=0, padx=20, pady=10)
m4_enter = Entry(f2, width=15, bg="#999", fg=fg_color, font=("arial 15"), bd=7, relief=SUNKEN, textvariable=calf_liver).grid(row=3, column=1, pady=10)
# =========================================> End Meats frame
# ====> New meats frame
f3 = LabelFrame(window, text="New Meats", bg=bg_color, fg="gold", font=("times new roman", 15, "bold"), bd=12, relief=GROOVE)
f3.place(x=410, y=170, width=400, height=350)

nm1_lbl = Label(f3, text="Head Meat", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=20, pady=10)
nm1_enter = Entry(f3, width=15, bg="#999", fg=fg_color, font=("arial 15"), bd=7, relief=SUNKEN, textvariable=head_meat).grid(row=0, column=1, pady=10)

nm2_lbl = Label(f3, text="Calf Tripe", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold")).grid(row=1, column=0, padx=20, pady=10)
nm2_enter = Entry(f3, width=15, bg="#999", fg=fg_color, font=("arial 15"), bd=7, relief=SUNKEN, textvariable=calf_tripe).grid(row=1, column=1, pady=10)

nm3_lbl = Label(f3, text="Vasha", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold")).grid(row=2, column=0, padx=20, pady=10)
nm3_enter = Entry(f3, width=15, bg="#999", fg=fg_color, font=("arial 15"), bd=7, relief=SUNKEN, textvariable=vasha).grid(row=2, column=1, pady=10)

nm4_lbl = Label(f3, text="Fats", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold")).grid(row=3, column=0, padx=20, pady=10)
nm4_enter = Entry(f3, width=15, bg="#999", fg=fg_color, font=("arial 15"), bd=7, relief=SUNKEN, textvariable=fats).grid(row=3, column=1, pady=10)

nm5_lbl = Label(f3, text="Calf Trotters", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold")).grid(row=4, column=0, padx=20, pady=10)
nm5_enter = Entry(f3, width=15, bg="#999", fg=fg_color, font=("arial 15"), bd=7, relief=SUNKEN, textvariable=calf_trotters).grid(row=4, column=1, pady=10)
# ===============================> End Meats
# =====> Bill Area
f4 = Frame(window,bd=12, relief=GROOVE)
f4.place(x=815, y=170, width=400, height=350)

bill_title = Label(f4, text="Bill Area", font=("arial 15 bold"), bd=7, relief=GROOVE).pack(fill=X)
txtarea = Text(f4)
txtarea.pack()


# ====================================> End Bill Area Frame
# ==========> Billing Menu
f5 = LabelFrame(window, text="Billing Menu", bg=bg_color, fg="gold", font=("times new roman", 15, "bold"), pady=15, bd=12, relief=GROOVE)
f5.place(x=0, y=525, relwidth=1, height=150)

total_meat_price_lbl = Label(f5, text="Total Meat Price", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=20, pady=10)
total_meat_price_enter = Entry(f5, width=10, bg="#999", fg=fg_color, font=("arial 15"), bd=7, relief=SUNKEN, textvariable=total_meat_price).grid(row=0, column=1)

total_new_meat_price_lbl = Label(f5, text="Total New Meat Price", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold")).grid(row=1, column=0, padx=20, pady=10)
total_new_meat_price_enter = Entry(f5, width=10, bg="#999", fg=fg_color, font=("arial 15"), bd=7, relief=SUNKEN, textvariable=total_new_meat_price).grid(row=1, column=1)

meat_tax_lbl = Label(f5, text="Meat Tax", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold")).grid(row=0, column=2, padx=20, pady=10)
meat_tax_enter = Entry(f5, width=10, bg="#999", fg=fg_color, font=("arial 15"), bd=7, relief=SUNKEN, textvariable=meat_tax).grid(row=0, column=3)

new_meat_tax_lbl = Label(f5, text="New Meat Tax", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold")).grid(row=1, column=2, padx=20, pady=10)
new_meat_tax_enter = Entry(f5, width=10, bg="#999", fg=fg_color, font=("arial 15"), bd=7, relief=SUNKEN, textvariable=new_meat_tax).grid(row=1, column=3)

# =====> Btn Frame
btn_frame= Frame(f5, pady=5, bd=12, relief=GROOVE)
btn_frame.place(x= 700)  # Write y = 120 is Hide element

total_btn = Button(btn_frame, text="Total", bg="#0f0", fg=fg_color, font=("arial 18 bold"), bd=7, activebackground="#00f", activeforeground=fg_color, command=total).grid(row=0, column=0, padx=5, pady=5)
genrate_bill_btn = Button(btn_frame, text="Genrate Bill", bg="yellow", fg=fg_color, font=("arial 18 bold"), bd=7, activebackground="#00f", activeforeground=fg_color, command=bill_area).grid(row=0, column=1, padx=5, pady=5)
clear_btn = Button(btn_frame, text="Clear", bg="#f00", fg=fg_color, font=("arial 18 bold"), bd=7, activebackground="#00f", activeforeground=fg_color, command=clear_data).grid(row=0, column=2, padx=5, pady=5)
exit_btn = Button(btn_frame, text="Exit", bg="lightgreen", fg=fg_color, font=("arial 18 bold"), bd=7, activebackground="#00f", activeforeground=fg_color, command=window.quit).grid(row=0, column=3, padx=5, pady=5)
welcome_bill()

# Execute the above code
window.mainloop()

#
# print("*" * 50)
# print(" Code ".center(40, "=").center(50, '*'))
# print("*" * 50)