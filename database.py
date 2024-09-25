import sqlite3

# Connessione al database (crea se non esiste)
def create_connection():
    conn = sqlite3.connect('city_management.db')
    return conn

# Creazione delle tabelle principali
def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    # Creazione di una tabella per edifici
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS buildings (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL,
        owner TEXT NOT NULL
    )
    ''')

    # Creazione di una tabella per i residenti
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS residents (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        building_id INTEGER,
        FOREIGN KEY(building_id) REFERENCES buildings(id)
    )
    ''')

    conn.commit()
    conn.close()

# Funzione per aggiungere un nuovo edificio
def add_building(name, address, owner):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO buildings (name, address, owner) VALUES (?, ?, ?)", (name, address, owner))
    conn.commit()
    conn.close()

# Funzione per ottenere la lista degli edifici
def get_buildings():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM buildings")
    buildings = cursor.fetchall()
    conn.close()
    return buildings
