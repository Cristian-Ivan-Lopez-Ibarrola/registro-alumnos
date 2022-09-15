import mysql.connector

class Base():
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            database="carrito_compras",
            user= "admin",
            password=""
            )
    
    def insertar_producto(self, codigo, nombre, precio, cantidad):
        cursor = self.conexion.cursor()
        sql = f"INSERT INTO producto (CODIGO, NOMBRE, PRECIO, CANTIDAD) VALUES({codigo}, '{nombre}', {precio}, {cantidad})"
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
    
    def mostrar_producto(self, codigo):
        cursor = self.conexion.cursor()
        sql = f"SELECT * INTO producto WHERE CODIGO = {codigo}"
        cursor.execute(sql)
        registro = cursor.fetchall()
        cursor.close()
        return registro
    
    def elimionar_producto(self, codigo):
        cursor = self.conexion.cursor()
        sql = f"DELETE FROM producto WHERE CODIGO = {codigo}"
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()