### Programacion de Computadoras IV
## Taller 2
# Braulio Rodriguez 8-899-1093

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String
from sqlalchemy.sql.sqltypes import Integer
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:123456789@localhost/slangs')
Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()

class Slangs(Base):
    __tablename__ = 'Slangs'
    id = Column(Integer(20), primary_key=True, AutoIncrement=True)
    Slang = Column(String(100))
    Significado = Column(String(100))


def add(var1, var2):
    add = Slangs(Slang=var1, Definicion=var2)
    session.add(add)
    session.commit()

def edit(var3, var4):
    edit = session.query(Slangs).get(var3)
    edit.Definicion = var4
    session.commit()

def delete(var5):
    session.query(Slangs).filter(Slangs.Slang == var5).delete()
    session.commit()

def view():
    ver = session.query(Slangs).all()
    for palabra in ver:
        print("El slang panameno es: " + palabra.Slang + " su significado es : " + palabra.Definicion)

def search(var6):
    significado = session.query(Slangs).filter_by(Slang = var6)
    for palabra in significado:
        print("El significado de: " + palabra.Slang + ", es: ", + palabra.Definicion)


# Menu de opciones
print("""
1. Insertar
2. Editar
3. Borrar
4. Visualizar
5. Buscar
6. Salir
""")

resp = 1
while(resp == 1):
    opcion = int(input("Ingrese una opcion"))

    if (opcion == 1):
        print("Ingresar nuevo registro")
        var1 = input("Ingrese un slang panameno: ")
        var2 = input("Ingrese su significado: ")
        add(var1, var2)

    elif (opcion == 2):
        print("Edite un registro: ")
        var3 = input("Ingrese un slang panameno ya existente: ")
        var4 = input("Ingrese su nuevo significado: ")
        edit(var3, var4)

    elif opcion == 3:
        print("Borre un registro")
        var5 = input("Ingrese el slang que desea eliminar")
        delete(var5)

    elif opcion == 4:
        print("Ver listado de palabras")
        view()

    elif opcion == 5:
        print("Buscar significado de palabra")
        var6 = input("Ingrese un slang panameno: ")
        search(var6)

    elif opcion == 6:
        break

    else:
        print("ERROR! OPCION INVALIDA")

    resp = input("Si desea continuar presione [1]")