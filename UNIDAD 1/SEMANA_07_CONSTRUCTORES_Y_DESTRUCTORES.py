class DatabaseConnection:
    def __init__(self, host, database, user, password):
        """
        Constructor que inicializa los atributos de la conexión a la base de datos.
        """
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        print(f"[INFO] Inicializando conexión a {self.database} en {self.host}...\n")
        self.connect()

    def connect(self):
        """
        Simula la conexión a la base de datos.
        """
        # En una aplicación real, aquí usarías una biblioteca como psycopg2 o mysql.connector.
        self.connection = f"Conexión establecida a {self.database} como {self.user}"
        print(f"[INFO] {self.connection}")

    def close(self):
        """
        Simula el cierre de la conexión a la base de datos.
        """
        if self.connection:
            print(f"[INFO] Cerrando la conexión a {self.database}...\n")
            self.connection = None
        else:
            print("[INFO] No hay conexión activa para cerrar.")

    def __del__(self):
        """
        Destructor que asegura que los recursos se limpien correctamente.
        """
        print(f"[INFO] Llamando al destructor para {self.database}...")
        self.close()

# Uso de la clase
if __name__ == "__main__":
    print("[INFO] Creando objeto DatabaseConnection...\n")
    db_conn = DatabaseConnection(host="localhost", database="test_db", user="admin", password="admin123")

    print("\n[INFO] Realizando operaciones con la base de datos...\n")
    # Simula alguna operación aquí

    print("\n[INFO] Eliminando objeto DatabaseConnection...\n")
    del db_conn
