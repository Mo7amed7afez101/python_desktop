from tkinter import *
import datetime

window = Tk()
window.geometry("600x400+150+150")
window.title("My Tasks")

# ==================================================
# ====================== Code ======================
# ==================================================

# ======> time
my_date = datetime.datetime.now().date()
from_date = datetime.datetime.now().strftime("%H")
to_date = ":5 hours" 

print("Task created time:")
print(f"Date: {my_date} Hour: {from_date}")


# =====> Variables
txt = StringVar()


# ======> Functions
def get_task():
        result = txt.get()
        txtarea.insert(END, f"Task Name: {result}\n")
        # txtarea.insert(END, f"Task time: {from_date} hours\n")
        txtarea.insert(END, "-" * 50 + "\n")
        txt.set("")

# ==================================================
# ===================== Design =====================
# ==================================================
lf = Frame(window, bg="#999", padx=10, pady=10)
lf.place(x=0, y=0, width=200, relheight=1)

txt_entry = Entry(lf, width=15, font=("arial 15 bold"), bd=7, relief=SUNKEN, textvariable=txt).grid(row=0, column=0, pady=10)
btn_add = Button(lf, text="Add Task    +", width=15, bg="#0f0", fg="white", font=("times new roman", 15, "bold"), command=get_task).grid(row=1, column=0)


rf = Frame(window, padx=10, pady=10, bd=12, relief=GROOVE)
rf.place(x=200, y=0, width=400, relheight=1)

title_lbl = Label(rf, text="My Objectives On Day", font=("times new roman", 15, "bold")).pack()

txtarea = Text(rf, font=("arial 15"))
txtarea.pack()




window.mainloop()

