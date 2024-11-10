import tkinter as tk
from wordFreq import *

file_path = "C:\\Users\\angel\\PycharmProjects\\FirstSemesterRVCE\\"

color1 = "#f3f2ce"
color2 = "#6e806e"
color3 = "#110930"  # for employee-outerspace
color4 = "#edd06c"  # for text box
color5 = "#4c7c88"

root = tk.Tk()
root.title("Experiential Learning - Python GUI")
root.configure(bg=color1)

# fit to screen
screen = f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}"
root.geometry(screen)

# Load the image
img1 = tk.PhotoImage(file=file_path + "itchio.png")
img3 = tk.PhotoImage(file=file_path + "itchio_forest.png")
img1_label = tk.Label(root, image=img1)
img1_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="n")

# Header Label
header_label1 = tk.Label(root, text="Experiential Learning - Python GUI", font=("Arial 25 bold"), bg=color2,
                         fg="WHITE")
header_label1.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="n")

# Footer label
footer_label1 = tk.Label(root, text="Angela Varghese\n1RV23IS014", font=("Arial", 16), bg=color2,
                         fg="WHITE")
footer_label1.grid(row=2, column=1, padx=10, pady=10, sticky="se")

# defining the grid
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)


def employeedatabase():
    employee = dict()
    root_employee = tk.Toplevel(root)
    root_employee.title("Employee Database Menu")
    root_employee.configure(bg=color3)

    # Set the window size to fit the screen
    root_employee.geometry(screen)


    # Header Label
    header_label2 = tk.Label(root_employee, text="Employee Database", font="Arial 25 bold", bg=color4, fg="BLACK")
    header_label2.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="n")

    footer_label2 = tk.Label(root_employee, text="Angela Varghese\n1RV23IS014", font=("Arial", 16),
                             bg=color4,
                             fg="BLACK")
    footer_label2.grid(row=2, column=1, padx=10, pady=10, sticky="se")

    # defining the grid
    root_employee.grid_rowconfigure(0, weight=1)
    root_employee.grid_columnconfigure(0, weight=1)
    root_employee.grid_columnconfigure(1, weight=1)

    root_employee.grid_rowconfigure(1, weight=1)
    root_employee.grid_columnconfigure(0, weight=1)
    root_employee.grid_columnconfigure(1, weight=1)

    root_employee.grid_rowconfigure(2, weight=1)
    root_employee.grid_columnconfigure(0, weight=1)
    root_employee.grid_columnconfigure(1, weight=1)

    def addemployee():
        new_window = tk.Toplevel()
        new_window.geometry("1000x500")
        new_window.title("Add Employee")
        new_window.configure(bg="#ffdae7")

        # defining the grid
        new_window.grid_rowconfigure(0, weight=1)
        new_window.grid_columnconfigure(0, weight=1)
        new_window.grid_columnconfigure(1, weight=1)

        new_window.grid_rowconfigure(1, weight=1)
        new_window.grid_columnconfigure(0, weight=1)
        new_window.grid_columnconfigure(1, weight=1)

        # Header Label
        header_label3 = tk.Label(new_window, text="Add Employee", font=("Arial 20 bold"), bg="#7a3e8d",
                                 fg="WHITE")
        header_label3.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="n")

        # Define a function to get the values and store them in variables
        def get_values():  # loop karo
            empID = empID_entry.get()
            empName = empName_entry.get()
            empDOB = empDOB_entry.get()
            empDes = empDes_entry.get()
            if empID and empName and empDOB and empDes:
                employee.update({empID: [empName, empDOB, empDes]})
                empID_entry.delete(0, tk.END)
                empName_entry.delete(0, tk.END)
                empDOB_entry.delete(0, tk.END)
                empDes_entry.delete(0, tk.END)

        empID_entry_label = tk.Label(new_window, text="Employee ID: ", font=("Arial 12"), bg="#ffdae7")
        empName_entry_label = tk.Label(new_window, text="Employee Name: ", font="Arial 12", bg="#ffdae7")
        empDOB_entry_label = tk.Label(new_window, text="Employee DOB: ", font=("Arial 12"), bg="#ffdae7")
        empDes_entry_label = tk.Label(new_window, text="Employee Designation: ", font=("Arial 12"), bg="#ffdae7")

        empID_entry = tk.Entry(new_window, font="Arial 12")
        empName_entry = tk.Entry(new_window, font="Arial 12")
        empDOB_entry = tk.Entry(new_window, font="Arial 12")
        empDes_entry = tk.Entry(new_window, font="Arial 12")

        empID_entry_label.grid(row=0, column=0, padx=10, pady=10, sticky="ws")
        empID_entry.grid(row=0, column=0, pady=10, sticky="es")

        empName_entry_label.grid(row=0, column=1, padx=10, pady=10, sticky="ws")
        empName_entry.grid(row=0, column=1, padx=10, pady=10, sticky="es")

        empDOB_entry_label.grid(row=1, column=0, padx=5, pady=10, sticky="wn")
        empDOB_entry.grid(row=1, column=0, padx=10, pady=10, sticky="en")

        empDes_entry_label.grid(row=1, column=1, padx=10, pady=10, sticky="wn")
        empDes_entry.grid(row=1, column=1, padx=10, pady=10, sticky="en")

        def close_window():
            new_window.destroy()

        # Create a button to trigger the value retrieval
        confirm_button = tk.Button(new_window,
                                   text="Confirm",
                                   command=get_values,
                                   background="#7a3e8d",
                                   foreground='WHITE',
                                   activebackground="#eba2ab",
                                   activeforeground="#e7dada",
                                   highlightthickness=2,
                                   highlightbackground="#d4d4aa",
                                   highlightcolor='WHITE',
                                   width=7, height=1, border=3,
                                   cursor='hand2',
                                   font=('Arial', 12)
                                   )
        confirm_button.grid(row=1, column=0, columnspan=2, pady=10)

        close_button = tk.Button(new_window,
                                 text="Close",
                                 command=close_window,
                                 background="#7a3e8d",
                                 foreground='WHITE',
                                 activebackground="#eba2ab",
                                 activeforeground="#e7dada",
                                 highlightthickness=2,
                                 highlightbackground="#d4d4aa",
                                 highlightcolor='WHITE',
                                 width=7, height=1, border=3,
                                 cursor='hand2',
                                 font=('Arial', 12)
                                 )
        close_button.grid(row=1, column=0, columnspan=2, pady=20, sticky="s")

        new_window.mainloop()

    def findemployee():
        new_window_fe = tk.Toplevel()
        new_window_fe.geometry("1000x500")
        new_window_fe.title("Find Employee")
        new_window_fe.configure(bg="#ffdae7")

        # defining the grid
        new_window_fe.grid_rowconfigure(0, weight=1)
        new_window_fe.grid_columnconfigure(0, weight=1)
        new_window_fe.grid_columnconfigure(1, weight=1)

        new_window_fe.grid_rowconfigure(1, weight=1)
        new_window_fe.grid_columnconfigure(0, weight=1)
        new_window_fe.grid_columnconfigure(1, weight=1)

        # Header Label
        header_label3 = tk.Label(new_window_fe, text="Find Employee", font=("Arial 20 bold"), bg="#7a3e8d",
                                 fg="WHITE")
        header_label3.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="n")

        empID_entry_label = tk.Label(new_window_fe, text="Employee ID: ", font=("Arial 12"), bg="#ffdae7")
        empID_entry = tk.Entry(new_window_fe, font="Arial 12")
        empID_entry_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        empID_entry.grid(row=0, column=1, pady=10, sticky="w")

        def get_values():
            empID = empID_entry.get()
            if empID:
                output = ""
                output_text = tk.Text(new_window_fe, width=50, height=5, font="Arial 12")
                output_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="s")
                empID_entry.delete(0, tk.END)
                output += f"For employee ID: {empID}\n"
                j = 0
                if empID in employee:
                    for i in ["Name", "DOB", "Designation"]:
                        output += f"{i}: {employee[empID][j]}\n"
                        j += 1
                else:
                    output += "Employee Not Found"

                output_text.insert(tk.END, output)

        def close_window():
            new_window_fe.destroy()

        confirm_button = tk.Button(new_window_fe,
                                   text="Confirm",
                                   command=get_values,
                                   background="WHITE",
                                   foreground="#7a3e8d",
                                   activebackground="#eba2ab",
                                   activeforeground="#e7dada",
                                   highlightthickness=2,
                                   highlightbackground="#d4d4aa",
                                   highlightcolor='WHITE',
                                   width=7, height=1, border=3,
                                   cursor='hand2',
                                   font=('Arial', 12)
                                   )
        confirm_button.grid(row=1, column=0, columnspan=2, pady=10)

        close_button = tk.Button(new_window_fe,
                                 text="Close",
                                 command=close_window,
                                 background='WHITE',
                                 foreground="#7a3e8d",
                                 activebackground="#eba2ab",
                                 activeforeground="#e7dada",
                                 highlightthickness=2,
                                 highlightbackground="#d4d4aa",
                                 highlightcolor='WHITE',
                                 width=7, height=1, border=3,
                                 cursor='hand2',
                                 font=('Arial', 12)
                                 )
        close_button.grid(row=1, column=0, columnspan=2, pady=10, sticky="s")

        new_window_fe.mainloop()

    def delemployee():
        new_window_de = tk.Toplevel()
        new_window_de.geometry("1000x500")
        new_window_de.title("Delete Employee")
        new_window_de.configure(bg="#ffdae7")

        # defining the grid
        new_window_de.grid_rowconfigure(0, weight=1)
        new_window_de.grid_columnconfigure(0, weight=1)
        new_window_de.grid_columnconfigure(1, weight=1)

        new_window_de.grid_rowconfigure(1, weight=1)
        new_window_de.grid_columnconfigure(0, weight=1)
        new_window_de.grid_columnconfigure(1, weight=1)

        # Header Label
        header_label4 = tk.Label(new_window_de, text="Delete Employee", font=("Arial 20 bold"), bg="#7a3e8d",
                                 fg="WHITE")
        header_label4.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="n")

        empID_entry_label = tk.Label(new_window_de, text="Employee ID: ", font=("Arial 12"), bg="#ffdae7")
        empID_entry = tk.Entry(new_window_de, font="Arial 12")
        empID_entry_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        empID_entry.grid(row=0, column=1, pady=10, sticky="w")

        def get_values():
            empID = empID_entry.get()
            if empID:
                output = ""
                output_text = tk.Text(new_window_de, width=50, height=5, font="Arial 12")
                output_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="s")
                empID_entry.delete(0, tk.END)
                if empID in employee:
                    output = f"Deleted employee with ID: {empID}"
                    del employee[empID]
                else:
                    output = "Employee Not Found"
                output_text.insert(tk.END, output)

        def close_window():
            new_window_de.destroy()

        confirm_button = tk.Button(new_window_de,
                                   text="Confirm",
                                   command=get_values,
                                   background="#7a3e8d",
                                   foreground="WHITE",
                                   activebackground="#eba2ab",
                                   activeforeground="#e7dada",
                                   highlightthickness=2,
                                   highlightbackground="#d4d4aa",
                                   highlightcolor='WHITE',
                                   width=7, height=1, border=3,
                                   cursor='hand2',
                                   font=('Arial', 12)
                                   )
        confirm_button.grid(row=1, column=0, columnspan=2, pady=10)

        close_button = tk.Button(new_window_de,
                                 text="Close",
                                 command=close_window,
                                 background='WHITE',
                                 foreground="#7a3e8d",
                                 activebackground="#eba2ab",
                                 activeforeground="#e7dada",
                                 highlightthickness=2,
                                 highlightbackground="#d4d4aa",
                                 highlightcolor='WHITE',
                                 width=7, height=1, border=3,
                                 cursor='hand2',
                                 font=('Arial', 12)
                                 )
        close_button.grid(row=1, column=0, columnspan=2, pady=10, sticky="s")
        new_window_de.mainloop()

    def display():
        disp = tk.Toplevel()
        disp.geometry("800x500")
        disp.title("Display Database")
        disp.configure(bg="#ffdae7")

        disp.grid_rowconfigure(0, weight=1)
        disp.grid_columnconfigure(0, weight=1)
        disp.grid_columnconfigure(1, weight=1)

        # Header Label
        header_label5 = tk.Label(disp, text="Display Database", font=("Arial 20 bold"), bg="#7a3e8d",
                                 fg="WHITE")
        header_label5.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="n")

        output = ""
        output_text = tk.Text(disp, width=50, height=10, font="Arial 12")
        output_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="s")
        if bool(employee):
            for key, value in employee.items():
                output += f"Employee ID {key}:\n"
                j = 0
                for i in ["Name", "DOB", "Designation"]:
                    output += f"{i}: {value[j]}\n"
                    j += 1
                output += "\n"
        else:
            output += "No Employee Details found."
        output_text.insert(tk.END, output)

        disp.mainloop()

    open_window_button1 = tk.Button(root_employee,
                                    background=color5,
                                    foreground='WHITE',
                                    activebackground="#edd06c",
                                    activeforeground="#736269",
                                    highlightthickness=2,
                                    highlightbackground="#d4d4aa",
                                    highlightcolor='WHITE',
                                    width=30, height=2, border=5,
                                    cursor='hand2', text='Add Employee',
                                    font=('Arial', 14),
                                    command=addemployee
                                    )
    open_window_button1.grid(row=1, column=0, padx=10, pady=10, sticky="ne")
    open_window_button2 = tk.Button(root_employee,
                                    background=color5,
                                    foreground='WHITE',
                                    activebackground="#edd06c",
                                    activeforeground="#736269",
                                    highlightthickness=2,
                                    highlightbackground="#d4d4aa",
                                    highlightcolor='WHITE',
                                    width=30, height=2, border=5,
                                    cursor='hand2', text='Find Employee',
                                    font=('Arial', 14),
                                    command=findemployee
                                    )
    open_window_button2.grid(row=1, column=1, padx=10, pady=10, sticky="nw")
    open_window_button3 = tk.Button(root_employee,
                                    background=color5,
                                    foreground='WHITE',
                                    activebackground="#edd06c",
                                    activeforeground="#736269",
                                    highlightthickness=2,
                                    highlightbackground="#d4d4aa",
                                    highlightcolor='WHITE',
                                    width=30, height=2, border=5,
                                    cursor='hand2', text='Delete Employee',
                                    font=('Arial', 14),
                                    command=delemployee
                                    )
    open_window_button3.grid(row=1, column=0, padx=10, pady=10, sticky="se")
    open_window_button4 = tk.Button(root_employee,
                                    background=color5,
                                    foreground='WHITE',
                                    activebackground="#edd06c",
                                    activeforeground="#736269",
                                    highlightthickness=2,
                                    highlightbackground="#d4d4aa",
                                    highlightcolor='WHITE',
                                    width=30, height=2, border=5,
                                    cursor='hand2', text='Display Database',
                                    font=('Arial', 14),
                                    command=display
                                    )
    open_window_button4.grid(row=1, column=1, padx=10, pady=10, sticky="sw")
    root_employee.mainloop()


def wordfreq():
    root_wq = tk.Toplevel(root)
    root_wq.title("Word Frequency in a Paragraph")
    root_wq.configure(bg="#3f7e54")

    # Set the window size to fit the screen
    root_wq.geometry(screen)

    # defining the grid
    root_wq.grid_rowconfigure(0, weight=1)
    root_wq.grid_columnconfigure(0, weight=1)
    root_wq.grid_columnconfigure(1, weight=1)

    root_wq.grid_rowconfigure(1, weight=1)
    root_wq.grid_columnconfigure(0, weight=1)
    root_wq.grid_columnconfigure(1, weight=1)

    root_wq.grid_rowconfigure(2, weight=1)
    root_wq.grid_columnconfigure(0, weight=1)
    root_wq.grid_columnconfigure(1, weight=1)
    # Load the image
    img3_label = tk.Label(root_wq, image=img3)
    img3_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="n")

    # Header Label
    header_label2 = tk.Label(root_wq, text="Word Frequency in a Paragraph", font="Arial 25 bold", bg="#2e2e2a",
                             fg="WHITE")
    header_label2.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="n")

    footer_label2 = tk.Label(root_wq, text="Aditya Nair, 1RV23ME013\nAchinthya Kadekar, 1RV23ME009", font=("Arial", 16),
                             bg="#2e2e2a",
                             fg="WHITE")
    footer_label2.grid(row=2, column=1, padx=10, pady=10, sticky="se")

    def on_enter_pressed():
        user_input = textbox.get("1.0", "end-1c")
        new_window = tk.Toplevel()
        new_window.geometry(screen)
        new_window.configure(bg="#3f7e54")
        new_window.title("Word Frequency: Output")

        new_window.rowconfigure(0, weight=1)
        new_window.columnconfigure(0, weight=1)
        new_window.columnconfigure(1, weight=1)

        tk.Label(new_window, text="Output", font="Arial 20 bold", bg="#2e2e2a", fg="WHITE").grid(
            row=0, column=0, columnspan=2, padx=10, pady=10, sticky="n")

        output_text = tk.Text(new_window, width=50, height=10)
        output_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        count = wordFreq(user_input)
        for key, value in count.items():
            output_text.insert(tk.END, f"{key}: {value}\n")

        new_window.mainloop()

    textbox = tk.Text(root_wq, width=80, height=10, font="Arial 14", background="#ebe8dd")
    textbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="n")

    enter_button = tk.Button(root_wq, command=on_enter_pressed,
                             text="Confirm",
                             background="#2e2e2a",
                             foreground='WHITE',
                             activebackground="#9a8a53",
                             activeforeground="WHITE",
                             highlightthickness=2,
                             highlightbackground="#d4d4aa",
                             highlightcolor='WHITE',
                             width=7, height=1, border=3,
                             cursor='hand2',
                             font=('Arial', 12)
                             )
    enter_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="s")

    result_label = tk.Label(root_wq, text="")
    result_label.grid(row=0, column=0, padx=10, pady=10)

    root_wq.mainloop()


wordfreqbutton = tk.Button(root,
                           background="#d4d4aa",
                           foreground='BLACK',
                           activebackground=color1,
                           activeforeground=color4,
                           highlightthickness=2,
                           highlightbackground="#d4d4aa",
                           highlightcolor='WHITE',
                           width=30, height=2, border=5,
                           cursor='hand2', text='Word Frequency in a Paragraph',
                           font=('Arial', 14),
                           command=wordfreq
                           )
wordfreqbutton.grid(row=1, column=0, padx=10, pady=10, sticky="ne")

empdatabutton = tk.Button(root,
                          background="#d4d4aa",
                          foreground='BLACK',
                          activebackground=color1,
                          activeforeground=color4,
                          highlightthickness=2,
                          highlightbackground="#d4d4aa",
                          highlightcolor='WHITE',
                          width=30, height=2, border=5,
                          cursor='hand2', text='Employee Database',
                          font=('Arial', 14),
                          command=employeedatabase
                          )
empdatabutton.grid(row=1, column=1, padx=10, pady=10, sticky="nw")
root.mainloop()
