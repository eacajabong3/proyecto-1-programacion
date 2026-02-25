
class Vuelo:
    def __init__(self, codigo, origen, destino, duracion, aerolinea):
        self.codigo=codigo
        self.origen=origen
        self.destino=destino
        self.duracion=int(duracion)
        self.aerolinea=aerolinea

    def __str__(self):
        return (f"codigo: {self.codigo}, origen: {self.origen}, "
                f"destino: {self.destino}, duracion: {self.duracion}, "
                f"aerolinea: {self.aerolinea}")

import xml.etree.ElementTree as ET

def cargar_archivo(ruta_archivo):
    vuelos = {}
    tree = ET.parse(ruta_archivo)
    root = tree.getroot()

    for vuelo_elem in root.findall("vuelo"):
        codigo = vuelo_elem.find("codigo").text
        if codigo in vuelos:
            print("Error: vuelo con codigo {codigo} ya existe")
            continue
        vuelo = Vuelo(
                codigo,
                vuelo_elem.find("origen").text,
                vuelo_elem.find("destino").text,
                vuelo_elem.find("duracion").text,
                vuelo_elem.find("aerolinea").text
            )
        vuelos[codigo] = vuelo
    return vuelos

def detalle_vuelo(vuelos, codigo):
    vuelo= vuelos.get(codigo)
    if vuelo:
        print(vuelo)
    else:
        print("EL vuelo no existe")

def agrupar_por_aerolinea(vuelos):
    grupos={}
    for v in vuelos.values():
        grupos.setdefault(v.aerolinea, []).append(v.codigo)
    for aerolinea, codigos in grupos.items():
         print(f"{aerolinea}: {', '.join(codigos)}")

def ordenar_por_duracion(vuelos):
    ordenados= sorted(vuelos.values(), key=lambda v: v.duracion, reverse=True)
    for v in ordenados:
        print(v)



def menu():
    vuelos={}
    while True:
        print("-----------MENU-----------")
        print("1. Cargar archivo. \n2. Detalle de vuelo especifico. \n3. Agrupar vuelos por aerolinea. \n4. Ordenar mas duracion a menor duracion. \n5. Salir")
        opcion=input("Escribe una de las opciones: ")
        if opcion=="1":
            ruta= input("ingrese una ruta:")
            try:
                vuelos = cargar_archivo(ruta)
                print("El archivo se cargó correctamente")
            except Exception as e:
                print("Error al cargar el archivo:", e)
        elif opcion=="2":
            codigo=input("Ingrese el codigo del vuelo: ")
            detalle_vuelo(vuelos, codigo)
        elif opcion=="3":
            agrupar_por_aerolinea(vuelos)
        elif opcion=="4":
            ordenar_por_duracion(vuelos)
        elif opcion=="5":
            break
        else:
            print("La opcion no existe")

if __name__=="__main__":
    menu()