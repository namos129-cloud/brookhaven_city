import tkinter as tk
from tkinter import messagebox
import database  # Importiamo il file database.py

# Creiamo la classe principale dell'interfaccia GUI
class CityManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("City Management App")

        # Creazione dei widget
        self.label_title = tk.Label(root, text="Gestione Città", font=('Helvetica', 16, 'bold'))
        self.label_title.pack()

        # Sezione per aggiungere nuovi edifici
        self.label_building = tk.Label(root, text="Aggiungi nuovo edificio")
        self.label_building.pack()

        self.entry_name = tk.Entry(root)
        self.entry_name.pack()
        self.entry_name.insert(0, "Nome Edificio")

        self.entry_address = tk.Entry(root)
        self.entry_address.pack()
        self.entry_address.insert(0, "Indirizzo")

        self.entry_owner = tk.Entry(root)
        self.entry_owner.pack()
        self.entry_owner.insert(0, "Proprietario")

        self.add_button = tk.Button(root, text="Aggiungi Edificio", command=self.add_building)
        self.add_button.pack()

        # Sezione per visualizzare gli edifici
        self.view_button = tk.Button(root, text="Mostra Edifici", command=self.show_buildings)
        self.view_button.pack()

        self.buildings_list = tk.Listbox(root)
        self.buildings_list.pack()

    def add_building(self):
        name = self.entry_name.get()
        address = self.entry_address.get()
        owner = self.entry_owner.get()
        database.add_building(name, address, owner)
        messagebox.showinfo("Successo", "Edificio aggiunto con successo!")

    def show_buildings(self):
        self.buildings_list.delete(0, tk.END)
        buildings = database.get_buildings()
        for building in buildings:
            self.buildings_list.insert(tk.END, f"ID: {building[0]} - {building[1]}, {building[2]}, {building[3]}")

