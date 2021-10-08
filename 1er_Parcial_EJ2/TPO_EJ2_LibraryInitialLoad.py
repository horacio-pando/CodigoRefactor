import random #Importe de modulo random para generador de stock inicial.
import TPO_EJ2_LibraryGen as gen

def initializeMatrix(matrix,stockMin,stockMax): #Listo
    '''Función para realizar la carga inicial de la matriz
        Parametros: 
        [f] cantidad de filas'''
    opcion='-1'
    impFlag='i'
        
    while int(opcion)!=0:
        while opcion.isdigit() is False:
            opcion=input("Que tipo de carga desea hacer?: \n 1. Carga Automática (Código y stock randomizados) \n 2. Carga Semi-Automática (Stock randomizado) \n 3. Carga Manual \n 0. Salir \n")
        if int(opcion)==1:
            matrix=generateLoadAuto(matrix,stockMin,stockMax)
            opcion=0
        elif int(opcion) ==2:
            matrix=generateLoadSemiAuto(matrix)
            opcion=0
        elif int(opcion) ==3:
            matrix=generateLoadManual(matrix,stockMin,stockMax)
            opcion=0
        elif int(opcion)==0:
            opcion=0
            impFlag='Cancelled'
        else:
            print("La opción seleccionada no es válida.")
            opcion=10
    
    #Consulta para impresion de tabla
    if int(opcion)==0 and impFlag is 'Cancelled':
        print("Carga inicial cancelada.")
    else:
        while impFlag !='Y' or impFlag !='N' or impFlag !='y' or impFlag !='n':
            impFlag=input("Desea mostrar la tabla en pantalla? Y/N ")
            if impFlag=='Y' or impFlag=='y':
                gen.imprimirMatriz(matrix)
                return matrix
            elif impFlag=='N' or impFlag=='n':
                return matrix
            else:
                print("La opción ingresada no es válida.")
    
def generateLoadSemiAuto(matrix): #Generación de stock por ingreso de código de producto y generador de stock
    '''La función genera una carga automática dummy en la tabla. El código de producto se pide por carga manual y el stock se generan aleatoriamente.'''
    i=0
    codProd='-2'
    inicio='-1'
    fin='-1'
    while int(codProd)!=-1:
        while codProd.isdigit() is False and int(codProd)!=-1:
            codProd=input("Ingrese el código del nuevo producto (para salir ingrese -1): ")
        if int(codProd)!=-1:
            if len(str(int(codProd)))==4:
                if gen.buscarCodigoDuplicadoMatrix(matrix,int(codProd))==False:
                    matrix.append([int(codProd)])
                    while int(inicio) < 0:
                        while inicio.isdigit() is False:
                            inicio=input("Para generar el stock, ingrese el rango inicial: ")
                        if int(inicio)<0:
                            print("El valor ingresado no es valido, ingreselo nuevamente.")
                            inicio='-1'
                    while int(inicio) > int(fin):
                        while fin.isdigit() is False:
                            fin=input("Para generar el stock, ingrese el rango final: ")
                        if int(fin) < int(inicio):
                            print("El valor ingresado no es valido, ingreselo nuevamente.")
                            fin='-1'
                    matrix[i].append(random.randint(int(inicio),int(fin)))
                    print("Producto agregado exitosamente.")
                    inicio='-1'
                    fin='-1'
                    i+=1
                    codProd='-2'
                else:
                    print("El código ingresado ya existe, ingrese un nuevo código.")
                    codProd='-2'
            else:
                print("El largo del código es inválido. Ingrese un código de 4 dígitos.")
                codProd='-2'
    return matrix
    
def generateLoadAuto(matrix,stockMin,stockMax,codProdLen=4): #Generación de código de producto y stock automáticos
    '''La función genera una carga automática dummy en la tabla. Tanto el código de producto como el stock se generan aleatoriamente.'''
    i=0
    codProd='-2'
    cantProd='0'
    inicio='-1'
    fin='-1'
    while int(inicio) < 0:
        while inicio.isdigit() is False:
            inicio=input("Para generar la cantidad de productos, ingrese el rango inicial: ")
        if int(inicio)<0:
            print("El valor ingresado no es valido, ingreselo nuevamente.")
            inicio='-1'
    while int(inicio) > int(fin):
        while fin.isdigit() is False:
            fin=input("Para generar la cantidad de productos, ingrese el rango final: ")
        if int(fin) < int(inicio):
            print("El valor ingresado no es valido, ingreselo nuevamente.")
            fin='-1'
    cantProd=random.randint(int(inicio),int(fin))
    
    #Genera contenido en tabla
    for i in range(cantProd):
        inicio=10**(codProdLen-1)
        fin=(10**codProdLen)-1
        codProd=random.randint(int(inicio),int(fin))
        while gen.buscarCodigoDuplicadoMatrix(matrix,int(codProd))==True:
            codProd=random.randint(int(inicio),int(fin))
        matrix.append([int(codProd)])
        matrix[i].append(random.randint(stockMin,stockMax))
    print("Auto Carga completa.")
    
    return matrix

def generateLoadManual (matrix, stockMin, stockMax): #Generación de código de producto y stock manuales
    '''La función carga valores en tabla por input pedido al usuario.'''
    i=0
    codProd='-2'
    stockProd='-1'
        
    while int(codProd)!=-1:
        while codProd.isdigit() is False and int(codProd)!=-1:
            codProd=input("Ingrese el código del nuevo producto (para salir ingrese -1): ")
        if int(codProd)!=-1:
            if len(str(int(codProd)))==4:
                if gen.buscarCodigoDuplicadoMatrix(matrix,int(codProd))==False:
                    while stockProd.isdigit() is False:
                        stockProd=input("Ingrese el stock del nuevo producto: ")
                    if int(stockProd) >= stockMin and int(stockProd) <= stockMax:
                        matrix.append([int(codProd)])
                        matrix[i].append(int(stockProd))
                        print("Producto agregado exitosamente.")
                        i+=1
                        codProd='-2'
                        stockProd='-1'
                    else:
                        stockProd='-1'
                        print("El stock ingresado no es valido.")
                else:
                    print("El código ingresado ya existe, ingrese un nuevo código.")
                    codProd='-2'
            else:
                print("El largo del código es inválido. Ingrese un código de 4 dígitos.")
                codProd='-2'
    return matrix

def main():
    print()

if __name__=="__main__":
    main()