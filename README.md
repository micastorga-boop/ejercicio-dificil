
peliculas = {
'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español',
False],
'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles',
False],
}

cartelera = {
'P101': [5990, 40],
'P102': [7990, 0],
'P103': [4990, 25],
'P104': [6990, 12],
'P105': [8990, 8],
'P106': [7490, 3],
}

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por género")
    print("2. Búsqueda de películas por rango de precio")
    print("3. Actualizar precio de película")
    print("4. Agregar película")
    print("5. Eliminar película")
    print("6. Salir")
    print("=====================================")
def leer_opcion():
 while True:
        try:
            opc = int(input("Ingrese una opción (1-6): "))
            if 1<=opc<=6:
                return opc
            print("ERROR ingrese una opción del 1 hasta el 6")
        except:
            print("ERROR tiene que ingresar un numero entero")

def validar_codigo(valor):
    if len(valor.strip())==0:
        return False
    return True

def validar_titulo(valor):
    if len(valor.strip())==0:
        return False
    return True

def validar_genero(valor):
    if len(valor.strip())==0:
        return False
    return True

def validar_duracion_min(valor):
    try:
        n = int(valor)
        if n>0:
            return True
        return False
    except:
        return False
    
def validar_clasificacion(valor):
    if len(valor.strip())==0:
        return False
    return True

def validar_idioma(valor):
    if len(valor.strip())==0:
        return False
    return True

def validar_3d(valor):
    if len(valor.strip().lower())=="si":
        return True
    elif len(valor.strip().lower())=="no":
        return False
    
def validar_precio(valor):
    try:
        n = int(valor)
        if n>0:
            return True
        return False
    except:
        return False
    
def validar_cupos(valor):
    try:
        n = int(valor)
        if n>0:
            return True
        return False
    except:
        return False
    

def agregar_pelicula(codigo,titulo,genero,duracion,clasificacion,idioma,es_3d,peliculas,cartelera,precio,cupos):
    if buscar_pelicula(codigo,peliculas,cartelera):
        print("esta pelicula ya existe")
    else:
        peliculas[codigo] = [titulo,genero,duracion,clasificacion,idioma,es_3d,]
        cartelera[codigo] = [precio,cupos]

def eliminar_pelicula(codigo,peliculas,cartelera):
    if buscar_pelicula(codigo,peliculas,cartelera):
        print("esta pelicula no existe")
    peliculas.pop(codigo)
    cartelera.pop(codigo)
    print("pelicula eliminada exitosamente")

def buscar_pelicula(codigo,peliculas,cartelera):
    for k in peliculas and cartelera:
        if k==codigo:
            return True
        return False
def busqueda_de_precio(p_min,p_max,peliculas,cartelera,precio):
    for p_min,p_max in cartelera:
        if p_min==cartelera(precio) and p_max==cartelera(precio):
            print()

def cupos_genero(codigo,peliculas,cartelera):
    for v in peliculas.item:
        if v==genero:
            for k in cartelera.keys:
                if k==codigo:
                    return True
                return False 

while True:
    mostrar_menu()
    opc=leer_opcion()
    if opc==1:
        while True:
            genero=input("Ingrese genero a consultar: ".strip().lower())
            if validar_genero(genero):
                if cupos_genero(genero):
                    print("")
    elif opc==2:
        while True:
            p_min=int(input("Ingrese precio minimo"))
            if p_min:
                pass
            p_max=int(input("Ingrese precio maximo"))
            if p_max:
                pass
            break
    elif opc==3:
        while True:
            codigo=input("Ingrese código de la pelicula: ")
            nuevo_precio=input("Ingrese nuevo precio")

            break
    elif opc==4:
        while True:
            pelicula=input("Que pelicula desea agregar")
            break
    elif opc==5:        
        while True:
            pelicula_eliminar=input("Ingrese la pelicula a eliminar: ")
            if eliminar_pelicula():
             pass
            break
    elif opc==6:
            while True:
                print("Programa finalizado")
                break
