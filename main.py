import tkinter as tk
from tkinter import ttk
import mysql.connector

def get_connection():
    f = open("./account.txt", "r")
    lines = f.readlines()
    host = lines[0]
    user = lines[1]
    password = lines[2]
    database = lines[3]
    f.close()
    try:
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=3306)
    except Exception as e:
        print("Wystąpil problem przy łaczeniu się z baza")
        print("Nastąpiło awaryjne zakończenie pracy programu")
    return mydb

def fetch_data(mydb):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM students")
    result = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return result

def load_data():
    data = fetch_data(get_connection())
    treeview.delete(*treeview.get_children())
    for row in data:
        treeview.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

def open_details_window(event):
    selected_item = treeview.focus()
    if selected_item:
        item_data = treeview.item(selected_item)
        item_values = item_data["values"]
        details_window = tk.Toplevel(root)
        details_window.title("Oceny")
        id_label = ttk.Label(details_window, text="ID:")
        id_label.pack()
        id_entry = ttk.Entry(details_window)
        id_entry.insert(0, item_values[0])
        id_entry.config(state="disabled")
        name_label = ttk.Label(details_window, text="Imie:")
        name_label.pack()
        name_entry = ttk.Entry(details_window)
        name_entry.insert(0, item_values[1])
        name_entry.pack()
        surname_label = ttk.Label(details_window, text="Nazwisko:")
        surname_label.pack()
        surname_entry = ttk.Entry(details_window)
        surname_entry.insert(0, item_values[2])
        surname_entry.pack()
        email_label = ttk.Label(details_window, text="Email:")
        email_label.pack()
        email_entry = ttk.Entry(details_window)
        email_entry.insert(0, item_values[3])
        email_entry.pack()
        status_label = ttk.Label(details_window, text="Status:")
        status_label.pack()
        status_entry = ttk.Entry(details_window)
        status_entry.insert(0, item_values[4])
        status_entry.pack()
        project_label = ttk.Label(details_window, text="Ocena za Projekt:")
        project_label.pack()
        project_entry = ttk.Entry(details_window)
        project_entry.insert(0, item_values[5])
        project_entry.pack()
        list1_label = ttk.Label(details_window, text="Ocena za Liste 1:")
        list1_label.pack()
        list1_entry = ttk.Entry(details_window)
        list1_entry.insert(0, item_values[6])
        list1_entry.pack()
        list2_label = ttk.Label(details_window, text="Ocena za Liste 2:")
        list2_label.pack()
        list2_entry = ttk.Entry(details_window)
        list2_entry.insert(0, item_values[7])
        list2_entry.pack()
        list3_label = ttk.Label(details_window, text="Ocena za Liste 3:")
        list3_label.pack()
        list3_entry = ttk.Entry(details_window)
        list3_entry.insert(0, item_values[8])
        list3_entry.pack()

        def edit():
            id = id_entry.get()
            new_name = name_entry.get()
            new_surname = surname_entry.get()
            new_email = email_entry.get()
            new_status = status_entry.get()
            new_project = project_entry.get()
            new_list1 = list1_entry.get()
            new_list2 = list2_entry.get()
            new_list3 = list3_entry.get()
            mydb = get_connection()
            mycursor = mydb.cursor()
            sql = "Update students Set name=%s,surname=%s,email=%s,status=%s,project=%s,l_1=%s,l_2=%s,l_3=%s Where id " \
                  "= %s"
            params = (new_name, new_surname, new_email, new_status, new_project, new_list1, new_list2, new_list3, id)
            mycursor.execute(sql, params)
            mydb.commit()
            mycursor.close()
            mydb.close()
            load_data()
            details_window.destroy()

        def delete():
            mydb = get_connection()
            mycursor = mydb.cursor()
            sql = "Delete from students Where id = " + id_entry.get()
            mycursor.execute(sql)
            mydb.commit()
            mycursor.close()
            mydb.close()
            load_data()
            details_window.destroy()

        add_button1 = ttk.Button(details_window, text="Potrwierdz zmiany", command=edit)
        add_button1.pack()

        add_button1 = ttk.Button(details_window, text="Usun", command=delete)
        add_button1.pack()

def open_new_book_window():
    new_window = tk.Toplevel(root)
    new_window.title("Dodaj noewgo studenta")
    name_label = ttk.Label(new_window, text="Imie:")
    name_label.pack()
    name_entry = ttk.Entry(new_window)
    name_entry.pack()
    surname_label = ttk.Label(new_window, text="Nazwisko:")
    surname_label.pack()
    surname_entry = ttk.Entry(new_window)
    surname_entry.pack()
    email_label = ttk.Label(new_window, text="Email:")
    email_label.pack()
    email_entry = ttk.Entry(new_window)
    email_entry.pack()
    status_label = ttk.Label(new_window, text="Status:")
    status_label.pack()
    status_entry = ttk.Entry(new_window)
    status_entry.pack()
    def add_new():
        new_name = name_entry.get()
        new_surname = surname_entry.get()
        new_email = email_entry.get()
        new_status = status_entry.get()
        mydb = get_connection()
        mycursor = mydb.cursor()
        sql = "Insert into students (name,surname,email,status) VALUES (%s,%s,%s,%s)"
        params = (new_name, new_surname, new_email, new_status)
        mycursor.execute(sql, params)
        mydb.commit()
        mycursor.close()
        mydb.close()
        new_window.destroy()
    add_button = ttk.Button(new_window, text="Dodaj", command=add_new)
    add_button.pack()

root = tk.Tk()
root.title("Students")

treeview = ttk.Treeview(root)
treeview["columns"] = ("id", "imie", "nazwisko", "emial", "status") #
treeview.pack()
treeview.heading("id",text="id")
treeview.heading("imie",text="imie")
treeview.heading("nazwisko",text="nazwisko")
treeview.heading("emial",text="emial")
treeview.heading("status",text="status")
treeview.column("#0", width=0)
add_new_book_button = tk.Button(root, text="Dodaj studenta", command=open_new_book_window)
add_new_book_button.pack(side="left")
load_data()
treeview.bind("<Double-1>", open_details_window)

root.mainloop()