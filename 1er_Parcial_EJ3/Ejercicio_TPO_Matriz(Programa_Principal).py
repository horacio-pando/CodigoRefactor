#TP3_EJ4
import random
from Ingresar_Nro import teclado 


def cargarMatriz(fabricas,columnas=6,desde=0,hasta=150): # Se pueden enviar diferentes valores para cada parametro.
    matriz = []
    filas = fabricas
    for f in range(filas):
        matriz.append([])
        for c in range(columnas):
            matriz[f].append(random.randint(desde,hasta))
    return matriz

def imprimirMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("|","%4d" %matriz[f][c], end=" |")
        print()
        
def sumarFabrica(matriz):
    filas = len(matriz)
    for f in range(filas):
        suma = sum(matriz[f])
        print("La cantidad de bicicletas producidas en la fabrica " , f+1 , ": ", suma)
      
def mayorFab(matriz):
    mayor = 0
    auxid = 0
    auxif = 0
    diasSemana=["Lunes", "Martes","Miercoles","Jueves","Viernes","Sabado"]
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        prod = 0
        for c in range(columnas):
            prod = (matriz [f][c])
            if prod > mayor:
                mayor = prod
                auxid = c
                auxif = f
            
                
    print("La fabrica que mas produjo en un solo día es: Fabrica ", auxif + 1 , "en el día: ", diasSemana[auxid])
    
def sumarDia(matriz):
    mayor = 0
    auxi = 0
    diasSemana=["Lunes", "Martes","Miercoles","Jueves","Viernes","Sabado"]
    filas = len(matriz)
    columnas = len(matriz[0])
    for c in range(columnas):
        suma = 0
        for f in range(filas):
            suma = suma + (matriz [f][c])
            if suma > mayor:
                mayor = suma
                auxi = c
    print("El dia con mayor produccion de bicicletas es: ", diasSemana[auxi])
    
#lista comprensión
    
def menorFab(matriz):
    listaComp = [min(matriz[f]) for f in range(len(matriz))] #funcion min (11 lineas)
    for f in range (len(listaComp)):
        print("La menor cantidad fabricada por la fabrica ", f+1 , " es: ", listaComp[f])
    
    '''
    "Este codigo es reemplazado por la lista por comprension. Lo dejamos como muestra de la cantidad de codigo que se puede llegar a reducir"
    menor = 0
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        menor = matriz[f][0]
        prod = matriz [f][c]
        for c in range(columnas):
            prod = (matriz [f][c])
            if prod < menor:
              menor = prod
    print("La menor cantidad de bicicletas producidas en la fabrica " , f+1 , ": ", menor)
    '''
    

#FUNCION MAIN
def main():
    fabricas = teclado("Ingrese cantidad de fabricas: ")
    matrix = cargarMatriz(fabricas) # 4 parametros. 3 por omision: cantidad de columnas (6), desde (0), hasta (150). Datos por omision dados por el enunciado.
    imprimirMatriz(matrix) #funcion que imprime la matriz
    print()
    sumarFabrica(matrix)#punto b (muestra el total de bicicletas fabricadas por fabrica)
    print()
    mayorFab(matrix)#punto c (muestra la fabrica que mas produjo en un solo dia, y que en que dia)
    print()
    sumarDia(matrix)#punto d (muestra el dia mas productivo. dia con mas produccion total)
    print()
    menorFab(matrix)#punto e (lista por comprension que contenga la menor cantidad fabricada por cada fabrica)
    
    
    
main()