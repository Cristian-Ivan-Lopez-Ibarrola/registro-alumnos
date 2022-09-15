from tkinter import *
from tkinter import messagebox
import pymysql


def menu_pantalla():
    global pantalla
    
    pantalla =  Tk()
    pantalla.geometry("300x250")
    pantalla.title("bienvenido")
    pantalla.iconbitmap("unnamed.ico")
    pantalla.resizable(0,0)

    Label(text="Acceso al Sistema", bg="navy", fg="white", width="300", height="3", font=("calibri", 15)).pack()
    Label(text="").pack()

    Button(text="Iniciar Sesion", height="3", width="30", command=inicio_sesion).pack()
    Label(text="").pack()

    Button(text="Registrar", height="3", width="30", command=registrar).pack()
    pantalla.mainloop()

def alumnos_pantalla():
    global pantalla_alumno
    pantalla_alumno = Toplevel(pantalla)
    pantalla_alumno.geometry("270x300")
    pantalla_alumno.title("Alumnos")
    pantalla_alumno.config(bg="gray22")
    pantalla_alumno.iconbitmap("unnamed.ico")
    pantalla_alumno.resizable(0,0)
    pantalla_alumno.focus_set()
    pantalla_alumno.grab_set()
    
    
    global idA
    global nombre
    global  apellido
    
    
    e = Label(pantalla_alumno, text="ID", bg="green", fg="white")
    e.pack(padx=5, pady=5, ipady=5, fill=X)

    idA = Entry(pantalla_alumno)
    idA.pack(padx=5, pady=5, ipady=5, fill=X)
    
    e1 = Label(pantalla_alumno, text="Nombre", bg="green", fg="white")
    e1.pack(padx=5, pady=5, ipady=5, fill=X)

    nombre = Entry(pantalla_alumno)
    nombre.pack(padx=5, pady=5, ipady=5, fill=X)
    
    e2 = Label(pantalla_alumno, text="Apellido", bg="green", fg="white")
    e2.pack(padx=5, pady=5, ipady=5, fill=X)
    
    apellido = Entry(pantalla_alumno)
    apellido.pack(padx=5, pady=5, ipady=5, fill=X)


    #botones
    boton = Button(pantalla_alumno, command=registrar_alumno, text="Registrar", fg="black")
    boton.pack(side=LEFT)
    
    boton1 = Button(pantalla_alumno, command=listar_alumno, text="listar", fg="black")
    boton1.pack(side=LEFT)
    
    boton2 = Button(pantalla_alumno, command=actualizar_alumno, text="Actualizar", fg="black")
    boton2.pack(side=LEFT)
    
    boton3 = Button(pantalla_alumno, command=eliminar_alumno, text="Eliminar", fg="black")
    boton3.pack(side=LEFT)
    
    boton4 = Button(pantalla_alumno,command= pantalla_alumno.destroy, text="salir", fg="black")
    boton4.pack(side=LEFT)
    
    
    
    pantalla_alumno.mainloop()

def inicio_sesion():
    global pantalla1
    pantalla1=Toplevel(pantalla)
    pantalla1.geometry("400x250")
    pantalla1.title("inicio de sesion")
    pantalla1.iconbitmap("unnamed.ico")
    pantalla1.resizable(0,0)
    pantalla1.focus_set()
    pantalla1.grab_set()
    
    Label(pantalla1, text="Por favor ingrese su Usuario y contraseña", bg="navy", fg="white", width="300", height="2", font=("calibri", 15)).pack()
    Label(pantalla1, text="").pack()
    
    global nombreUsuario_verify
    global contrasenaUsuario_verify
    
    nombreUsuario_verify= StringVar()
    contrasenaUsuario_verify= StringVar()
    
    global nombre_usuario_entry
    global contrasena_usuario_entry
    
    Label(pantalla1, text="Usuario").pack()
    nombre_usuario_entry= Entry(pantalla1, textvariable=nombreUsuario_verify)
    nombre_usuario_entry.pack()
    Label(pantalla1).pack()
    
    Label(pantalla1, text="Contraseña").pack()
    contrasena_usuario_entry= Entry(pantalla1, textvariable=contrasenaUsuario_verify, show="\u2022")
    contrasena_usuario_entry.pack()
    Label(pantalla1).pack()
    
    Button(pantalla1, text="Iniciar Sesion", command=login).pack()

 
def registrar():
    global pantalla2
    pantalla2=Toplevel(pantalla)
    pantalla2.geometry("400x250")
    pantalla2.title("registro")
    pantalla2.iconbitmap("unnamed.ico")
    pantalla2.resizable(0,0)
    pantalla2.grab_set()
    pantalla2.focus_set()
    
    global nombre_entry
    global contrasena_entry
    
    nombreUsuario_entry= StringVar()
    contrasenaUsuario_entry= StringVar()
    
    Label(pantalla2, text="Ingrese un nombre de usuario y contraseña\npara el registro", bg="navy", fg="white", width="300", height="2", font=("calibri", 15)).pack()
    Label(pantalla2).pack()
    
    Label(pantalla2, text="Usuario").pack()
    nombre_entry= Entry(pantalla2, textvariable=nombreUsuario_entry)
    nombre_entry.pack()
    Label(pantalla2).pack()
    
    Label(pantalla2, text="contraseña").pack()
    contrasena_entry= Entry(pantalla2, textvariable=contrasenaUsuario_entry, show="\u2022")
    contrasena_entry.pack()
    Label(pantalla2).pack()

    Button(pantalla2, text="Registrar", command=registro).pack()

def registro():
    db=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="asistencia"
        )
    
    db_cursor=db.cursor()
    
    sql="INSERT INTO register_user VALUES('{0}', '{1}')".format(nombre_entry.get(), contrasena_entry.get())

    try:
        db_cursor.execute(sql)
        db.commit()
        messagebox.showinfo(message="Registro Exitoso", title="Aviso")
        pantalla2.destroy()
        
    except:
        db.rollback()
        messagebox.showinfo(message="No Registrado", title="Aviso")
        nombreUsuario_verify.set("")
        contrasenaUsuario_verify.set("")
        
    db.close()

def login():
    db=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="asistencia"
        )
    db_cursor=db.cursor()
    
    db_cursor.execute("SELECT * FROM register_user WHERE username='"+nombreUsuario_verify.get()+"' and pass='"+contrasenaUsuario_verify.get()+"'")
    if db_cursor.fetchall():
        global user_verificado
        
        user_verificado = nombreUsuario_verify.get()
        pantalla1.destroy()
        alumnos_pantalla()
    else:
        messagebox.showinfo(title="inicio de sesion incorrecta", message="Usuario y contraseña incorrecta")
        nombreUsuario_verify.set("")
        contrasenaUsuario_verify.set("")
        
    db.close()

def registrar_alumno():
    db=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="asistencia"
        )
    db_cursor=db.cursor()
    
    sql = "INSERT INTO alumno VALUES('{0}', '{1}', '{2}', '{3}')".format(idA.get(), nombre.get(), apellido.get(), user_verificado)
    
    try:
        db_cursor.execute(sql)
        db.commit()
        messagebox.showinfo(message="Registrado", title="Aviso")

    except:
        db.rollback()
        messagebox.showinfo(message="No Registrado", title="Aviso")

def eliminar_alumno():
    db=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="asistencia"
        )
    db_cursor=db.cursor()
    
    sql = "DELETE FROM alumno WHERE id='{0}'".format(idA.get())
    
    try:
        db_cursor.execute(sql)
        db.commit()
        messagebox.showinfo(message="eliminado", title="Aviso")

    except:
        db.rollback()
        messagebox.showinfo(message="No eliminado", title="Aviso")

def actualizar_alumno():
    db=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="asistencia"
        )
    db_cursor=db.cursor()
    
    sql = "UPDATE alumno SET nombre= '{0}',  apellido= '{1}' WHERE id= '{2}' and username_user= '{3}'".format(nombre.get(), apellido.get(), idA.get(),  user_verificado)
    
    try:
        db_cursor.execute(sql)
        db.commit()
        messagebox.showinfo(message="actualizado", title="Aviso")

    except:
        db.rollback()
        messagebox.showinfo(message="No actualizado", title="Aviso")

def listar_alumno():
    db=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="asistencia"
        )
    db_cursor=db.cursor()
    
    sql = "SELECT * FROM alumnos WHERE username_user= {0}".format(user_verificado)
    
    try:
        db_cursor.execute(sql)
        
        contador=0
        for alu in db_cursor.fetchall():
            datos = "{0}. DNi: {1} NOMBRE: {2} APELLIDO: {3} DIRECCION: {4} LEGAJO: {5}"
            print(datos.format(contador, alu[0], alu[1], alu[2], alu[3], alu[4]))
            contador+1
            
        messagebox.showinfo(message="listado", title="Aviso")

    except:
        db.rollback()
        messagebox.showinfo(message="No actualizado", title="Aviso")
        
        
        
menu_pantalla()
