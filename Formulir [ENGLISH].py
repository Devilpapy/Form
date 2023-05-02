import os
import tkinter as tk
from datetime import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


window = tk.Tk()
window.title("Form")

window.geometry("400x350")

nama_label = tk.Label(window, text="Fullname:")
nama_label.grid(row=0, column=0, padx=10, pady=15)
nama_entry = tk.Entry(window)
nama_entry.grid(row=0, column=1, padx=10, pady=15)

gender_label = tk.Label(window, text="Gender:")
gender_label.grid(row=1, column=0, padx=10, pady=10)
gender_var = tk.StringVar()
gender_var.set("Man")
gender_radio1 = tk.Radiobutton(window, text="Man", variable=gender_var, value="Man")
gender_radio2 = tk.Radiobutton(window, text="Woman", variable=gender_var, value="Woman")
gender_radio1.grid(row=1, column=1, padx=10, pady=10)
gender_radio2.grid(row=1, column=2, padx=10, pady=10)

umur_label = tk.Label(window, text="Age:")
umur_label.grid(row=2, column=0, padx=10, pady=10)
umur_entry = tk.Entry(window)
umur_entry.grid(row=2, column=1, padx=10, pady=10)

email_label = tk.Label(window, text="Email:")
email_label.grid(row=3, column=0, padx=10, pady=10)
email_entry = tk.Entry(window)
email_entry.grid(row=3, column=1, padx=10, pady=10)

password_label = tk.Label(window, text="Password:")
password_label.grid(row=4, column=0, padx=10, pady=10)
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=4, column=1, padx=10, pady=10)

alamat_label = tk.Label(window, text="Addresss:")
alamat_label.grid(row=5, column=0, padx=10, pady=10)
alamat_entry = tk.Entry(window)
alamat_entry.grid(row=5, column=1, padx=10, pady=10)

def submit():
    print("Full Name:", nama_entry.get())
    print("Gender:", gender_var.get())
    print("Age:", umur_entry.get())
    print("Email:", email_entry.get())
    print("Password:", password_entry.get())
    print("Address:", alamat_entry.get())


def save_data():
    nama= nama_entry.get()
    gender = gender_var.get()
    umur = umur_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    alamat = alamat_entry.get() 

    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    filename = "Form Data " + str(timestamp) + ".txt"
    filepath = os.path.join(os.path.expanduser("~"), "Documents", filename)

    with open(filepath, 'w') as f:
        f.write(f"Fullname: {nama}\n")
        f.write(f"Gender: {gender}\n")
        f.write(f"Umur: {umur}\n")
        f.write(f"Email: {email}\n")
        f.write(f"Password: {password}\n")
        f.write(f"Address: {alamat}\n")

        messagebox.showinfo("Save Data", "Data saved successfully!!")


submit_button = tk.Button(window, text="Submit", bg = "red", fg = "white", command=submit)
submit_button.grid(row=6, column=1, padx=10, pady=10)

tk.Button(window, text="Save Data", command=save_data)

save_button = tk.Button(window, text="Save Data", command=save_data)
save_button.grid(row=7, column=1, padx=10, pady=10)

window.mainloop()
