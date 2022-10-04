from tkinter import *
from tkinter import messagebox
import pymysql;

def menu_pantalla():
    global pantalla
    pantalla=Tk()
    pantalla.geometry("400x480")
    pantalla.title("bienvenidos")
    pantalla.iconbitmap("UNDAV.ico")

    image = PhotoImage(file="UNDAV.gif")
    image = image.subsample(1, 1)
    label = Label(image=image)
    label.pack()

    Label(text="Acceso al sistema",bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
    Label(text="").pack()

    Button(text="Iniciar Sesión", command=incio_sesion, height="3", width="30").pack()
    Label(text="").pack()

    Button(text="registrar", command=registrar, height="3", width="30").pack()

    pantalla.mainloop()

def incio_sesion():
    global pantalla1
    pantalla1 = Toplevel(pantalla)
    pantalla1.geometry("400x480")
    pantalla1.title("Inicio de sesion")
    pantalla1.iconbitmap("UNDAV.ico")

    Label(pantalla1, text="Ingrese Usuario y Contraseña", bg="navy", fg="white", width="300", height="3", font=("Calibri", 10)).pack()
    Label(pantalla1, text="").pack()

    global nombreusuario_verify
    global contrasenausuario_verify

    nombreusuario_verify = StringVar()
    contrasenausuario_verify = StringVar()

    global nombre_usuario_entry
    global contrasena_usuario_entry

    Label(pantalla1, text="Usuario").pack()
    nombre_usuario_entry = Entry(pantalla1, textvariable=nombreusuario_verify)
    nombre_usuario_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text="Contraseña").pack()
    contrasena_usuario_entry = Entry(pantalla1, textvariable=contrasenausuario_verify, show="*")
    contrasena_usuario_entry.pack()
    Label(pantalla1).pack()

    Button(pantalla1, text="Iniciar sesion", command=validar_datos).pack()

def registrar():
    global pantalla2;
    pantalla2 = Toplevel (pantalla);
    pantalla2.geometry("400x480");
    pantalla2.title("Registrarse");
    pantalla2.iconbitmap("UNDAV.ico");
    
    global nombreusuario_entry;
    global contrasena_entry;

    nombreusuario_entry=StringVar();
    contrasena_entry=StringVar();

    Label(pantalla2, text="Ingrese un Usuario y contraseña para el registro al sistema",bg="navy", fg="white", width="300", height="3", font=("Calibri", 10)).pack()
    Label(pantalla2, text="").pack();

    Label(pantalla2, text="Usuario").pack()
    nombreusuario_entry = Entry(pantalla2)
    nombreusuario_entry.pack()
    Label(pantalla2).pack();

    Label(pantalla2, text="Contraseña").pack()
    contrasena_entry = Entry(pantalla2, show="*")
    contrasena_entry.pack()
    Label(pantalla2).pack()
    Button(pantalla2, text="Registrarse", command=insertar_datos).pack()
    
def insertar_datos():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="bd2"
    )
    fcursor=bd.cursor();
    sql="INSERT INTO login (usuario, contrasena) VALUES ('{0}','{1}')".format(nombreusuario_entry.get(), contrasena_entry.get());
    
    try:
        fcursor.execute(sql);
        bd.commit();
        messagebox.showinfo(message="Registro exitoso", title="Aviso")
    except:
        bd.rollback();
        messagebox.showinfo(message="NO Registrado", title="Aviso");
        bd.close();
def validar_datos():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="bd2"
    )
    fcursor=bd.cursor();
    fcursor.execute("SELECT contrasena FROM login WHERE usuario='"+nombreusuario_verify.get()+"' and contrasena='"+contrasenausuario_verify.get()+"'")

    if fcursor.fetchall():
        messagebox.showinfo(title="Inicio de sesion exitoso", message="Usuario y contraseña correcta");
    else:
        messagebox.showinfo(title="Inicio de sesion incorrecto", message="Usuario y contraseña incorrecta");
    bd.close();
menu_pantalla()