# Proyectos
Un programa en python con interfaz grafico con tkinter y una base de datos con pymysql de inicio y registro de sesion con base de datos
el error que me da al dar click en el boton de registrarse una vez introducido los datos es:

line 86, in inserta_datos
    sql="INSERT INTO login (usuario,  contrasena) VALUES ('{0}', '{1}')".format(nombreusuario_entry.get(), contrasenausuario_entry.get());    
AttributeError: 'NoneType' object has no attribute 'get'
