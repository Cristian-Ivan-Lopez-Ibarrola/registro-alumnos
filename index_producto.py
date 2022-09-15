from tkinter import *
from tkinter import ttk
from conexion_producto import *


class Registro_producto(Frame):
    def __init__(self, ventana, *args, **kwargs):
        super().__init__(ventana, *args, **kwargs)
        self.frame1 = Frame(ventana)
        self.frame1.grid(columnspan=2, column=0, row=0)
        
        self.frame2 = Frame(ventana, bg="navy")
        self.frame2.grid(column=0, row=1, sticky="wens")
        
        self.frame3 = Frame(ventana)
        self.frame3.grid(rowspan = 2, column=1, row=1)
        
        self.frame4 = Frame(ventana, bg="black")
        self.frame4.grid(column=0, row=2, sticky="wens")
        
        # self.codigo = StringVar()
        # self.nombre = StringVar()
        # self.precio = StringVar()
        # self.cantidad = StringVar()
        
        self.base_datos = Base()
        self.create_wietgs()
    
    def create_wietgs(self):
        
        self.codigo = StringVar()
        self.nombre = StringVar()
        self.precio = StringVar()
        self.cantidad = StringVar()
        
        
        Label(self.frame1, text="registrador \t de \t productos", bg="gray22",fg="white", font=("Orbitron",15,"bold"), justify="center").grid(column=0, row=0)
        
        Label(self.frame2, text="Agregar Nuevo Alumno", fg="white", bg="navy", font=("Rockwell", 12, "bold")).grid(columnspan=2, column=0,row=0, pady=5)
        Label(self.frame2, text="Codigo", fg="white", bg="navy", font=("Rockwell", 13, "bold")).grid(column=0,row=1, pady=15)
        Label(self.frame2, text="Nombre", fg="white", bg="navy", font=("Rockwell", 13, "bold")).grid(column=0,row=2, pady=15)
        Label(self.frame2, text="Precio", fg="white", bg="navy", font=("Rockwell", 13, "bold")).grid(column=0,row=3, pady=15)
        Label(self.frame2, text="cantidad", fg="white", bg="navy", font=("Rockwell", 13, "bold")).grid(column=0,row=4, pady=15)
        
        Entry(self.frame2, textvariable= self.codigo, text="Codigo", font=("Arial", 12)).grid(column=1,row=1, padx=5)
        Entry(self.frame2, textvariable= self.nombre, text="Nombre", font=("Arial", 12)).grid(column=1,row=2)
        Entry(self.frame2, textvariable= self.precio, text="Precio", font=("Arial", 12)).grid(column=1,row=3)
        Entry(self.frame2, textvariable= self.cantidad, text="cantidad", font=("Arial", 12)).grid(column=1,row=4)
        
        
        Label(self.frame4, text="Control", fg="white", bg="black", font=("Rockwell", 13, "bold"), anchor="center").grid(columnspan=3, column=0, row=0, pady=1, padx=4)
        Button(self.frame4,command=self.agregar_datos, text="REISTRAR", font=("Arial", 10), bg="magenta", justify="center").grid(column=0, row=1, pady=10, padx=40)
        Button(self.frame4,command=self.limpiar_datos, text="Limpiar", font=("Arial", 10), bg="red").grid(column=1, row=1, padx=10, pady=10)
        Button(self.frame4,command=self.eliminar_registro, text="Eliminar", font=("Arial", 10), bg="black", fg="white").grid(column=2, row=1, padx=40)
        Button(self.frame4,command=self.mostrar_todo, text="Mostrar Todo", font=("Arial", 10), bg="yellow").grid(columnspan=3, column=0, row=2, padx=100)
        
        self.tabla = ttk.Treeview(self.frame3, height=21)
        self.tabla.grid(column=0, row=0)
        
        ladox = Scrollbar(self.frame3, orient=HORIZONTAL, command= self.tabla.xview)
        ladox.grid(column=0,row=1, sticky="ew")
        ladoy = Scrollbar(self.frame3, orient=VERTICAL, command= self.tabla.yview)
        ladoy.grid(column=1, row=0, sticky="ns")
        
        self.tabla.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)
        
        self.tabla["columns"] = ("Nombre", "Precio", "Cantidad")
        
        self.tabla.column("#0", minwidth=100, width=120, anchor="center")
        self.tabla.column("Nombre", minwidth=100, width=130, anchor="center")
        self.tabla.column("Precio", minwidth=100, width=120, anchor="center")
        self.tabla.column("Cantidad", minwidth=100, width=105, anchor="center")
        
        self.tabla.heading("#0", text= "Codigo", anchor="center")
        self.tabla.heading("Nombre", text= "Nombre", anchor="center")
        self.tabla.heading("Precio", text= "Precio", anchor="center")
        self.tabla.heading("Cantidad",text= "Cantidad", anchor="center")
        
        estilo = ttk.Style(self.frame3)
        estilo.theme_use("alt")
        estilo.configure(".", front=("Helvetica", 12, "bold"), foreground="red2")
        estilo.configure("Treeview", font=("Helvetica", 10, "bold") ,foreground="black", background="white")
        estilo.map("Treeview", background=[("selected", "green2")], foreground=[("selected","black")])
        
        self.tabla.bind("<<TreeviewSelect>>", self.obtener_registro)
        
    def agregar_datos(self):
        self.tabla.get_children()
        codigo = self.codigo.get()
        nombre = self.nombre.get()
        precio = self.precio.get()
        cantidad = self.cantidad.get()
        print(codigo, nombre, precio, cantidad)
        datos = (nombre, precio, cantidad)
        if codigo and nombre and precio and cantidad !="":
            self.tabla.insert("",0, text=codigo, values=datos)
            self.base_datos.insertar_producto(codigo,nombre,precio,cantidad)
    
    def limpiar_datos(self):
        self.tabla.delete(*self.tabla.get_children())
        self.codigo.set("")
        self.nombre.set("")
        self.precio.set("")
        self.cantidad.set("")
    
    def mostrar_todo(self):
        self.tabla.delete(*self.tabla.get_children())
        registro = self.base_datos.mostrar_producto()
        i = 0
        for dato in registro:
            self.tabla.insert("",i,text=registro[i][0:1], values=[i][1:4])
    
    def eliminar_registro(self):
        registro = self.tabla.selection()
        if len(registro) !=0:
            self.tabla.delete(registro)
            codigo =("'" + str(self.codigo_borrar) + "'")
            self.base_datos.elimionar_producto(codigo)
    
    def obtener_registro(self, evento):
        current_item = self.tabla.focus()
        if not current_item:
            return
        data = self.tabla.item(current_item)
        self.codigo_borrar = data["values"][0]

def main():
    ventana = Tk()
    ventana.wm_title("Registro")
    ventana.config(bg="gray22")
    ventana.geometry("900x500")
    ventana.resizable(False, False)
    app = Registro_producto(ventana)
    app.mainloop()
    
if __name__ =="__main__":
    main()