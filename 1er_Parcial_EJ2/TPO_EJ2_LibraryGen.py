def imprimirMatriz(matriz):
    '''Función para imprimir la matriz proporcionada'''
    f=0
    c=0
    print("\n")
    print("|Cod. Prod.||   Stock  |")
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("|","%8d" %matriz[f][c], end=" |")
        print()
    print("\n")
    input()

#Lambdas para dibujado de UI
menuPrincipal = lambda : print("Que acción desea tomar? \n 1. Carga Inicial. \n 2. Actualizar Stock. \n 3. Consultas e Informes. \n 0. Exit.")
'''Imprime el menú principal en pantalla'''
subMenuCI = lambda : print("Que acción desea tomar? \n 1. Realizar carga inicial de Prueba. \n 2. Definir stock Mínimo. \n 3. Definir stock Máximo. \n 0. Volver al menu principal.")
'''Imprime el sub-menú de Carga Inicial en pantalla'''
subMenuAS = lambda : print("Que tipo de actualización desea hacer? \n 1. Agregar un nuevo Producto. \n 2. Actualizar stock existente por fabricación. \n 3. Actualizar stock existente por venta. \n 4. Eliminar producto de la tabla. \n 0. Volver al menu principal.")
'''Imprime el sub-menú de Actualizar Stock en pantalla'''
subMenuCoIn = lambda : print("Que tipo de informe necesita? \n 1. Ordenar por código y mostrar tabla. \n 2. Productos con stock debajo del mínimo. \n 3. Detalle de stock de un producto. \n 0. Volver al menu principal.")
'''Imprime el sub-menú de Consultas e Informes en pantalla'''

def buscarCodigoDuplicadoMatrix(matrix, newCode):
    '''Función busca un código dentro de la matriz provista:
        Encontrado = True
        No encontrado = False'''
    response=False
    filas = len(matrix)
    for f in range(filas):
        if matrix[f][0]==newCode:
            response=True
    
    return response
    
def buscarCodigoEnTabla(matrix, Code):
    '''La función busca un código de producto dentro de la matriz provista'''
    position=0
    filas = len(matrix)
    for f in range(filas):
        if matrix[f][0]==Code:
            position=f
    
    return position

def main():
    print()

if __name__ =="__main__":
    main()