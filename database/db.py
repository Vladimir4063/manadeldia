import sqlite3

try:
    # Conectar a la base de datos SQLite
    connection = sqlite3.connect("database/database.sqlite", check_same_thread=False)
    cursor = connection.cursor()

    # Verificar si la tabla existe
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='parasha'"
    )
    tabla_existe = cursor.fetchone()

    if tabla_existe:
        print("La tabla ya existe en la base de datos.")
    else:
        # Crear la tabla si no existe
        cursor.execute(
            """CREATE TABLE parasha(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	isPublic BOOLEAN,
    nroParasha INT,
    nameParasha VARCHAR(255),
    signParasha VARCHAR(255),
	section1 VARCHAR(255),
	section2 VARCHAR(255),
	section3 VARCHAR(255),
	section4 VARCHAR(255),
	section5 VARCHAR(255),
	section6 VARCHAR(255),
	section7 VARCHAR(255),
    aliya1 TEXT,
    aliya2 TEXT,
    aliya3 TEXT,
    aliya4 TEXT,
    aliya5 TEXT,
    aliya6 TEXT,
    aliya7 TEXT,
    titleReflection1 VARCHAR(255),
    titleReflection2 VARCHAR(255),
    titleReflection3 VARCHAR(255),
    titleReflection4 VARCHAR(255),
    titleReflection5 VARCHAR(255),
    titleReflection6 VARCHAR(255),
    titleReflection7 VARCHAR(255),
    reflection1 TEXT,
    reflection2 TEXT,
    reflection3 TEXT,
    reflection4 TEXT,
    reflection5 TEXT,
    reflection6 TEXT,
    reflection7 TEXT,
    sectionHaftara VARCHAR(255),
    haftara TEXT,
    verso1 TEXT,
    verso2 TEXT,
    verso3 TEXT,
    verso4 TEXT,
    verso5 TEXT,
    verso6 TEXT,
    verso7 TEXT
);"""
        )
        connection.commit()
        print("La tabla ha sido creada correctamente.")

    # Cerrar la conexión
    connection.close()

except Exception as error:
    print(error)
