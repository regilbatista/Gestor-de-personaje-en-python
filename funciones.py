import os
from re import A
from time import sleep
import webbrowser
from peewee import *
from soupsieve import escape
from prettytable import PrettyTable
from prettytable import from_db_cursor
from datetime import datetime
import time
import folium
from geopy.geocoders import Nominatim
import sqlite3

db = SqliteDatabase('pfinal.db')



class Serie(Model):
    serie = CharField(50)
    class Meta:
      database = db

class Sexo(Model):
    sexo = CharField(50)
    class Meta:
      database = db
class Estado(Model):
    estado = CharField(50)  
    class Meta:
      database = db

class Personaje(Model):
    nombre = CharField(50)
    apellido = CharField(50)
    foto= CharField(2083)
    idser = ForeignKeyField(Serie, backref='serieref')
    pronuciacion= CharField(50)
    fechan = DateTimeField()
    poder = CharField(50)
    frase = CharField(50)
    descripcion = CharField(50)
    edad = IntegerField()
    altura = CharField(8)
    idsex = ForeignKeyField(Sexo, backref='sexoref')
    idest = ForeignKeyField(Estado, backref='estadoref')
    Dirección  = CharField(50)
    Lat = FloatField()
    Lng = FloatField()


    class Meta:
      database = db




db.connect()
db.create_tables([Serie,Sexo,Personaje,Estado])

class makeser:
    def __init__(self) :
       self.ser = Serie()


    def  insert_to_seri(self):
        print(showser())
        lim()
        print('Agregaremos una serie')
        self.ser.serie = input('Ingrese el nombre de la serie: ')
        self.ser.save()
        input('La serie se guardo exitosamente (^-^). Presiona Enter para continuar')

    def  update_ser(self):

        lim()
        print('Lista de las serie registrados')
        print(showser())
        idm= input('Ingrese el id de la serie que quiere modificar. De lo contrario inserte X: ')
        if idm=='x' or idm=='X':
            return False
        seri = Serie.select().where(Serie.id == idm).get()
        seri.serie = confirmdat('Serie', seri.serie)
        seri.save()
        input('La serie se Modifico exitosamente \^o^/. Presiona Enter para continuar')

    def  remove_ser(self):
        lim()
        print('Lista de las series registrados')
        print(showser())
        idm= input('Ingrese el id de la serie que quiere eliminar. De lo contrario inserte X: ')
        if idm=='x' or idm=='X':
         return False
        seri = Serie.select().where(Serie.id == idm).get()
        input(f'La serie {seri.id}->{seri.serie}, se ha borrado satisfactoriamente (*^▽^*). Presione enter para continuar')
        seri.delete_instance()

class makeest:
    def __init__(self) :
       self.est = Estado()


    def  insert_to_est(self):
        print(showest())
        lim()
        print('Agregaremos un estado')
        self.est.estado = input('Ingrese el estado: ')
        self.est.save()
        input('El estdado se guardo exitosamente (^-^). Presiona Enter para continuar')

    def  update_est(self):

        lim()
        print('Lista de los estados registrados')
        print(showest())
        idm= input('Ingrese el id del estado que quiere modificar. De lo contrario inserte X: ')
        if idm=='x' or idm=='X':
            return False
        Est = Estado.select().where(Estado.id == idm).get()
        Est.estado = confirmdat('Estado', Est.estado)
        Est.save()
        input('El estado se Modifico exitosamente \^o^/. Presiona Enter para continuar')

    def  remove_est(self):
        lim()
        print('Lista de los estados registrados')
        print(showest())
        idm= input('Ingrese el id del estado que quiere eliminar. De lo contrario inserte X: ')
        if idm=='x' or idm=='X':
         return False
        est = Estado.select().where(Estado.id == idm).get()
        input(f'El estado {est.id}->{est.estado}, se ha borrado satisfactoriamente (*^▽^*). Presione enter para continuar')
        est.delete_instance()


class makesex:
    def __init__(self) :
       self.sex = Sexo()


    def  insert_to_sex(self):
        print(showsex())
        lim()
        print('Agregaremos un sexo')
        self.sex.sexo = input('Ingrese el sexo: ')
        self.sex.save()
        input('El sexo se guardo exitosamente (^-^). Presiona Enter para continuar')

    def  update_sex(self):

        lim()
        print('Lista de los sexo registrados')
        print(showsex())
        idm= input('Ingrese el id del sexo que quiere modificar. De lo contrario inserte X: ')
        if idm=='x' or idm=='X':
            return False
        sexi = Sexo.select().where(Sexo.id == idm).get()
        sexi.sexo = confirmdat('Sexo', sexi.sexo)
        sexi.save()
        input('El sexo se Modifico exitosamente \^o^/. Presiona Enter para continuar')

    def  remove_sex(self):
        lim()
        print('Lista de los sexos registrados')
        print(showsex())
        idm= input('Ingrese el id del sexo que quiere modificar. De lo contrario inserte X: ')
        if idm=='x' or idm=='X':
         return False
        sexi = Sexo.select().where(Sexo.id == idm).get()
        input(f'El sexo {sexi.id}->{sexi.sexo}, se ha borrado satisfactoriamente (*^▽^*). Presione enter para continuar')
        sexi.delete_instance()


class makeper:
    def __init__(self) :
       self.per = Personaje()


    def  insert_to_per(self):
        lim()
        print('Agregaremos al personaje')
        self.per.nombre = input('Ingrese el nombre del personaje: ')
        self.per.apellido = input('Ingrese el apellido del peronaje: ')
        self.per.foto = input('Ingrese el Url de la foto del personaje: ')
        print(showser())
        self.per.idser = input('Ingrese el id de la serie de donde pertenece el personaje: ')
        self.per.pronuciacion = input('Ingrese la pronuciacion nombre del personaje: ')
        self.per.fechan = input('Ingrese la fecha de naciento del personaje: ')
        self.per.poder = input('Ingrese el poder del personaje: ')
        self.per.frase = input('Ingrese la frase caracteristica del personaje: ')
        self.per.edad = input('Ingrese ingrese la edad del personaje: ')
        self.per.descripcion = input('Ingrese la descripcion de la ropa del personaje: ')
        self.per.altura = input('Ingrese la altura del peronaje: ')
        print(showsex())
        self.per.idsex = input('Ingrese el id del sexo del peronaje: ')
        print(showest())
        self.per.idest = input('Ingrese el id del estado del peronaje: ')
        self.per.Dirección = input('Ingrese la direcciòn del personaje: ')
        resultado=in_earth()
        self.per.Lat=resultado[0]
        self.per.Lng=resultado[1]
        self.per.save()
        input('Los datos se guardo exitosamente (^-^). Presiona Enter para continuar')

    def  update_per(self):

        lim()
        print('Lista de los personajes registrados')
        print(showlistper())
        idm=""
        while idm=="":
            idm= input('Ingrese el id del registro que quiere modificar. De lo contrario inserte X: ')
            if idm=='x' or idm=='X':
                return False
            
        prove = Personaje.select().where(Personaje.id == idm).get()
        prove.nombre = confirmdat('Nombre', prove.nombre)
        prove.apellido = confirmdat('Apellido', prove.apellido)
        prove.foto = confirmdat('Foto', prove.foto)
        print(showser())
        prove.idser = confirmdat('Serie', str(prove.idser))
        prove.pronuciacion = confirmdat('Pronuciacion', prove.pronuciacion)
        prove.fechan = confirmdat('Fecha', prove.fechan)
        prove.poder = confirmdat('Poder', prove.poder)
        prove.frase = confirmdat('Frase', prove.frase)
        prove.edad = confirmdat('Edad', str(prove.edad))
        prove.descripcion = confirmdat('Descripcion', prove.descripcion)
        print(showsex())
        prove.idsex = confirmdat('Sexo', str(prove.idsex))
        print(showest())
        prove.idest = confirmdat('Estado', str(prove.idest))
        prove.Dirección = confirmdat('Direccion', prove.Dirección)
        prove.Lat = confirmdat('Latitud', str(prove.Lat))
        prove.Lng = confirmdat('Longitud', str(prove.Lng))
        prove.save()
        input('Los registros se Modificaron exitosamente \^o^/. Presiona Enter para continuar')
    
    def  remove_per(self):
        lim()
        print('Lista de los sexos registrados')
        print(showlistper())
        idm= input('Ingrese el id del sexo que quiere modificar. De lo contrario inserte X: ')
        if idm=='x' or idm=='X':
         return False
        per = Personaje.select().where(Personaje.id == idm).get()
        input(f'El personaje {per.id}->{per.nombre}, se ha borrado satisfactoriamente (*^▽^*). Presione enter para continuar')
        per.delete_instance()


def in_earth():
    coco = True
    while coco:
        coca = input('Ingrese ubicacion en latidud del dueño: ')
        cola = input('Ingrese ubicacion en longitud del dueño: ')

        

        if str(cola)=="" and str(coca)=="":
                    str(coca)
                    str(cola)
                    coca="18.707034952626643"
                    cola="-70.60262607863835"
                    return coca, cola

        elif int(coca) >=-90 or int(coca)<=90:
            if int(cola) >=-180 or int(cola)<=180: 
                    coco = False
                    return coca, cola   
                    
            else:
                str(coca)
                str(cola)
                coca="18.707034952626643"
                cola="-70.60262607863835"
                return coca, cola
        else:
           str(coca)
           str(cola)
           coca="18.707034952626643"
           cola="-70.60262607863835"
           return coca, cola


def showser():
  tabla=PrettyTable()
  tabla.field_names=['Id','Serie']
  for Ser in Serie.select():
     tabla.add_row([Ser.id,Ser.serie])
  return tabla

def showsex():
 tabla=PrettyTable()
 tabla.field_names=['Id','Sexo']
 for sex in Sexo.select():
     tabla.add_row([sex.id,sex.sexo])
 return tabla
 
def showest():
 tabla=PrettyTable()
 tabla.field_names=['Id','Estado']
 for est in Estado.select():
     tabla.add_row([est.id,est.estado])
 return tabla

def showlistper():
  tabla=PrettyTable()
  tabla.field_names=['Id','Nombre','Apellido','Serie','Genero','Edad']
  conn = sqlite3.connect('pfinal.db')
  cursor = conn.cursor()
  sql = '''SELECT personaje.id,nombre,apellido,serie,sexo,edad
  FROM personaje
  INNER JOIN serie
  ON personaje.idser_id = serie.id
  INNER JOIN Sexo
  ON personaje.idsex_id = sexo.id;'''
  cursor.execute(sql)
  mytable = from_db_cursor(cursor)
  print(mytable)
  input('Presiona Enter para continuar')


def showlistsigno():  
    cap=0
    ac=0
    pi=0
    ar=0
    ta=0
    ge=0
    ca=0
    le=0
    vi=0
    li=0
    es=0
    sa=0

    for Ser in Personaje.select():
      x= str(Ser.fechan).split("/")
      if int(x[1]) ==1:
         if int(x[0]) <=21:
                signo="Capricornio"
                cap=cap+1
         else:
                signo="Acuario"
                ac=ac+1
      if int(x[1]) ==2:
          if int(x[0]) <=19:
                signo="Acuario"
                ac=ac+1
          else:
                signo="Picis"
                pi=pi+1
      if int(x[1]) ==3:
        if int(x[0]) <=21:
                signo="Picis"
                pi=pi+1
        else:
                signo="Aries"
                ar=ar+1
      if int(x[1]) ==4:
         if int(x[0]) <=21:
                signo="Aries"
                ar=ar+1
         else:
                signo="Tauro"
                ta=ta+1
      if int(x[1]) ==5:
          if int(x[0]) <=22:
                signo="Tauro"
                ta=ta+1
          else:
                signo="Geminis"
                ge=ge+1
      if int(x[1]) ==6:
           if int(x[0]) <=22:
                signo="Geminis"
                ge=ge+1
           else:
                signo="Cancer"
                ca=ca+1
      if int(x[1]) ==7:
          if int(x[0]) <=23:
                signo="Cancer"
                ca=ca+1
          else:
                signo="Leo"
                le=le+1
      if int(x[1]) ==8:
          if int(x[0]) <=23:
                signo="Leo"
                le=le+1
          else:
                signo="Virgo"
                vi=vi+1
      if int(x[1]) ==9:
          if int(x[0]) <=23:
                signo="Virgo"
                vi=vi+1
          else:
                signo="Libra"
                li=li+1
      if int(x[1]) ==10:
          if int(x[0]) <=23:
                signo="Libra"
                li=li+1
          else:
                signo="Ecorpio"
                es=es+1
      if int(x[1]) ==11:
          if int(x[0]) <=23:
                signo="Ecorpio"
                es=es+1
          else:
                signo="Sagitario"
                sa=sa+1
      if int(x[1]) ==12:
          if int(x[0]) <=22:
                signo="Sagitario"
                sa=sa+1
          else:
                signo="Capricornio"
                cap=cap+1
    x = PrettyTable()
    x.field_names = ["Signo Sodiacal", "Cantidad"]
    x.add_row(["Capricornio",cap ])
    x.add_row(["Acuario", ac])
    x.add_row(["Picis", pi])
    x.add_row(["Aries", ar])
    x.add_row(["Tauro", ta])
    x.add_row(["Geminis", ge])
    x.add_row(["Cancer", ca])
    x.add_row(["Leo", le])
    x.add_row(["Virgo", vi])
    x.add_row(["Libra", li])
    x.add_row(["Ecorpio", es])
    x.add_row(["Sagitario", sa])
    print(x)
    input('Presione para continuar')

def showlistedad():
  tabla=PrettyTable()
  tabla.field_names=['Id','Nombre','Apellido','Serie','Genero','Edad']
  conn = sqlite3.connect('pfinal.db')
  cursor = conn.cursor()
  a=input("Ingrese una edad ")
  sql = f'''SELECT personaje.id,nombre,apellido,serie,sexo,edad
    FROM personaje
    INNER JOIN serie
    ON personaje.idser_id = serie.id
    INNER JOIN Sexo
    ON personaje.idsex_id = sexo.id
    where personaje.edad={a};'''
  cursor.execute(sql)
  mytable = from_db_cursor(cursor)
  print(mytable)
  input('Presiona Enter para continuar')

def showlistserie():
  tabla=PrettyTable()
  tabla.field_names=['Id','Serie','Personajes']
  conn = sqlite3.connect('pfinal.db')
  cursor = conn.cursor()
  sql = '''SELECT serie.id, serie,count(personaje.id) as personajes
FROM serie
INNER JOIN personaje
ON  serie.id = personaje.idser_id;'''
  cursor.execute(sql)
  mytable = from_db_cursor(cursor)
  print(mytable)
  input('Presiona Enter para continuar')

def showlistest():
  tabla=PrettyTable()
  tabla.field_names=['Id','estado','Personajes']
  conn = sqlite3.connect('pfinal.db')
  cursor = conn.cursor()
  sql = '''SELECT estado.id, estado,count(personaje.id) as personajes
FROM estado
INNER JOIN personaje
ON  estado.id = personaje.idest_id;'''
  cursor.execute(sql)
  mytable = from_db_cursor(cursor)
  print(mytable)
  input('Presiona Enter para continuar')

def export():
    print ("Exportando a mapa")
    m = folium.Map(location=[18.992362, -70.7290879], zoom_start=8)
    for registro in Personaje.select():
        tool = registro.nombre
        pop= f"""
            <h3>Datos: </h3>
            <table>
                <tr>
                    <th>Nombre: </th>
                    <td>{registro.nombre}</td>
                </tr>
                <tr>
                    <th>Apellido: </th>
                    <td>{registro.apellido}</td>
                </tr>
                <tr>
                    <th>Edad: </th>
                    <td>{registro.edad}</td>
                </tr>
                <tr>
                    <th>Descripcion: </th>
                    <td>{registro.descripcion}</td>
                </tr>

            </table>"""
        folium. Marker ([float (registro.Lat), float(registro.Lng)], popup=pop, tooltip=tool).add_to(m)
    m.save("prueba.html")
    webbrowser.open("prueba.html")
    input ("Registro importado. Presione enter para continuar")


def  lim():
    os.system('cls')
se= makeser()
e= makeest()
s= makesex()
p= makeper()

def agser():
    se.insert_to_seri()

def modser():
    se.update_ser()

def elimser():
    se.remove_ser()

def agest():
    e.insert_to_est()

def modest():
    e.update_est()

def elimest():
    e.remove_est()

def agsex():
    s.insert_to_sex()

def modsex():
    s.update_sex()

def elimsex():
    s.remove_sex()

def agper():
    p.insert_to_per()

def modper():
    p.update_per()

def elimper():
    p.remove_per()

def confirmdat(c,v):
    print("El campo "+c+" tiene el valor "+v)
    tmp=input('Ingrese el nuevo valor o dejelo en blanco para no afectar el valor: ')
    if tmp == "":
        return v
    else:
        return tmp
  
def Export():
    
  showlistper()
  idm=""
  while idm=="":
            idm= input('Ingrese el id del registro que quiere seleccionar. De lo contrario inserte X: ')
            if idm=='x' or idm=='X':
                return False
  rgt = Personaje.select().where(Personaje.id == idm).get()
 
  html= f"""
    <html>
  <head>
    <link rel="stylesheet" type="text/css" href="style.css" >
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  </head>
  <body>
   <div>
    <br><br><br><br><br><br>
    <div id= "principal">               
        
            <div  id="secundario" ><ul>
            <table>
                <tr>
                   <td>
<img src= {rgt.foto} align="left" width="120"
     height="200" > </td> <td>    &nbsp; </td><td>    &nbsp; </td> <td>    &nbsp; </td><td>    &nbsp; </td>
                    <td>
                    <li><b>Nombre: </b> {rgt.nombre} </li>
                     <li><b>Apellido: </b> {rgt.apellido} </li>    
                    <li><b>Fecha de nacimiento: </b>  {rgt.fechan} </li>
                    <li><b>Edad: </b>{rgt.edad}</li> 
                     <li><b>frase: </b>  {rgt.frase} </li>
                     <li><b>altura: </b>{rgt.altura}</li>
                     <li><b>direccion: </b>{rgt.Dirección}</li> 
             <br> <br> 
            </ul>
            </td><td>    &nbsp; </td>  
            
             </div>
                </div>
            </div>
            </body>
            </html> """

  o= open("easy.html", "w", encoding="utf-8")
  o.write(html)
  o.close()
  webbrowser.open("easy.html")

def  aboutme():
    ab= """
         Creador:
           -Matricula: 2021-2251
           -Nombre: Regil Isaac 
           -Apellido: Batista Calderon
            
    """
    print(ab)
    webbrowser.open_new_tab("https://youtu.be/ck-245w3BXE")