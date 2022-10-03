from cProfile import label;
import tkinter ; #LIBRERIA PARA LA INTERFAZ GRAFICA
from tkinter import*;
from tkinter import messagebox;
from tkinter import font;
import pymysql; #LIBRERIA PARA MANEJAR BASE DE DATOS
#DEFINIMOS LA PANTALLA PRINCIPAL DEL PROGRAMA
def menu_pantalla():
    global pantalla;
    pantalla=Tk();
    pantalla.geometry("400x480");
    pantalla.title("Inicio");
    pantalla.iconbitmap("UNDAV.ico");
    image=PhotoImage(file="UNDAV.gif");
    image=image.subsample(1,1);
    label=Label(image=image);
    label.pack();
    Label(text="Acceso al sistema", bg="navy", fg="white", width="300", height="3", font=("calibrí", 15)).pack();
    Label(text="").pack();
    Button(text="Inicio de Sesion", height="3", width="30", command=inicio_sesion).pack();
    Label(text="").pack();
    Button(text="Registrarse", height="3", width="30", command=registrar).pack();
    pantalla.mainloop();

#DEFINIMOS LA PANTALLA DE INICIO
def inicio_sesion():
    global pantalla1;
    pantalla1 = Toplevel(pantalla);
    pantalla1.geometry("400x480");
    pantalla1.title("Iniciar Sesión");
    pantalla1.iconbitmap("UNDAV.ico");
    Label(pantalla1, text="Ingrese su Usuario y Contraseña a continuación", bg="navy", fg="white", width="150", height="2", font=("calibrí", 10)).pack();
    Label(pantalla1, text=" ").pack;
    global nombre_usuario_verify;
    global contrasenausuario_verify;

    nombre_usuario_verify = StringVar();
    contrasenausuario_verify = StringVar();

    global nombre_usuario_entry;
    global contrasena_usuario_entry;

    Label(pantalla1, text="Usuario").pack();
    nombre_usuario_entry = Entry(pantalla1, textvariable=nombre_usuario_verify);
    nombre_usuario_entry.pack();
    Label(pantalla1).pack();

    Label(pantalla1, text="Contraseña").pack();
    contrasena_usuario_entry = Entry(pantalla1, textvariable=contrasenausuario_verify);
    contrasena_usuario_entry.pack();
    Label(pantalla1).pack();

    Button(pantalla1, text="Iniciar sesion").pack();
#DEFINIMOS LA PANTALLA DE REGISTRO
def registrar():
    global pantalla2;
    pantalla2 = Toplevel (pantalla);
    pantalla2.geometry("400x480");
    pantalla2.title("Registrarse");
    pantalla2.iconbitmap("UNDAV.ico");
    
    global nombreusuario_entry;
    global contrasenausuario_entry;

    nombreusuario_entry = StringVar;
    contrasenausuario_entry = StringVar;

    Label(pantalla2, text="Ingrese un Usuario y Contraseña", bg="navy", fg="white", width="150", height="2", font=("calibrí", 10)).pack();
    Label(pantalla2, text="");
    Label(pantalla2, text="Usuario").pack();
    nombreusuario_entry = Entry(pantalla2).pack();
    Label(pantalla2, text="Contraseña").pack()
    contrasenausuario_entry = Entry(pantalla2).pack();
    Button(pantalla2, text="Registrarse", command=inserta_datos).pack();
#DEFINIMOS LA FUNCION PARA QUE AL MOMENTO DE DAR CLICK EN EL BOTON DE REGISTRARSE SUBA LOS DATOS DEL USUARIO Y CONTRASEÑA
def inserta_datos():


		bd = pymysql.connect(
			host ="localhost",
			user ="root",
			password ="",
			db ="bd2")

		fcursor = bd.cursor()
		
		sql="INSERT INTO login (usuario,  contrasena) VALUES ('{0}', '{1}')".format(nombreusuario_entry.get(), contrasenausuario_entry.get());

		try:
			fcursor.execute(sql)
			bd.commit()
			messagebox.showinfo(message="Registro Exitoso", title="Aviso")

		except: 
			bd.rollback()
			messagebox.showinfo(message="No pudo registrase", title="Aviso")

		bd.close()



menu_pantalla();
