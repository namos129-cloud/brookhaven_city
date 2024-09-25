import tkinter as tk
from gui import CityManagementApp
import database

if __name__ == "__main__":
    # Creazione delle tabelle nel database se non esistono già
    database.create_tables()

    # Avvio dell'applicazione GUI
    root = tk.Tk()
    app = CityManagementApp(root)
    root.mainloop()
