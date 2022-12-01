import csv
import os

ruta_base = 'C:/Users/Tarde/Downloads/DelaOsa_deGuzman_Daniel_Boletin1/consultas-csv/'
archivo = ruta_base + 'cust_orders_prods.csv'

def menu(ruta_archivo):
    os.system("cls")
    print("""-----------Consultas CSV-----------
    1.- Mostrar porcentaje de ventas de cada vendedor
    2.- Mostrar porcentaje de ventas de cada cliente
    3.- Mostrar TOP 5 productos más vendidos
    4.- Ingresos mensuales
    5.- Salir
    """)
    opc1 = input("Escriba con un numero lo que quiera realizar: ")
    if opc1 == "1":
        ventas_vendedor(ruta_archivo,dicc)
    
    elif opc1 == "2":
        ventas_clientes(ruta_archivo,dicc)
    
    elif opc1 == "3":
        top_productos(ruta_archivo)
    
    elif opc1 == "4":
        ingresos_mes(ruta_archivo)
    
    elif opc1 == "5":
        salir(ruta_archivo)




def ventas_vendedor(ruta_archivo,diccionario):
    
    diccVendedores = {}
    total_ventas = 0
    for i in range(len(diccionario)):
        total_ventas+=int(diccionario[i]['quantity'])*int(diccionario[i]['unit_price'])

    for fila in diccionario:
        vendedor = fila["employee_name"]
        cantidad = int(fila["quantity"])
        precio_ud = int(fila["unit_price"])
        precio_total = cantidad * precio_ud
        if vendedor not in diccVendedores:
            diccVendedores[vendedor] = precio_total
        else:
            diccVendedores[vendedor] = diccVendedores[vendedor] + precio_total
    for j in diccVendedores:
        diccVendedores[j] = f"{round(((diccVendedores[j] / total_ventas)*100),2)}%"

        
    print(diccVendedores)

    volver=input("Pulse enter para volver: ")
    if volver == "":
        menu(ruta_archivo)
    else:
        menu(ruta_archivo)

def ventas_clientes(ruta_archivo, dictcsv):
    os.system("cls")
    total_ventas = 0
    for i in range(len(dictcsv)):
        total_ventas+=int(dictcsv[i]['quantity'])*int(dictcsv[i]['unit_price'])
    print(total_ventas)
    listanombres = []
    
    for n in range(len(dictcsv)):
        listanombres.append(dictcsv[n]['customer_name'])
    listanombres = dict.fromkeys(listanombres,0)

    for j in listanombres:
        while j in dictcsv:
            listanombres[j]+= int(dictcsv[j]['quantity'])*int(dictcsv[j]['unit_price'])
    print(listanombres) 



    volver=input("Pulse enter para volver: ")
    if volver == "":
        menu(ruta_archivo)
    else:
        menu(ruta_archivo)

def top_productos(ruta_archivo):
    os.system("cls")
    print("Esto es top productos")
    volver=input("Pulse enter para volver: ")
    if volver == "":
        menu(ruta_archivo)
    else:
        menu(ruta_archivo)

def ingresos_mes(ruta_archivo):
    os.system("cls")
    print("Esto es ingresos_mes")
    volver=input("Pulse enter para volver: ")
    if volver == "":
        menu(ruta_archivo)
    else:
        menu(ruta_archivo)

def salir(ruta_archivo):
    exit()

def abrir_csv(ruta_archivo):
    f = open(ruta_archivo,"r")
    lector_dict = csv.DictReader(f)
    lista_dict = list(lector_dict)
    f.close()
    return lista_dict

dicc = abrir_csv(archivo)



print(menu(archivo))
#142