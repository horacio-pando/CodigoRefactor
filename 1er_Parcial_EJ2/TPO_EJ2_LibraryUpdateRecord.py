import TPO_EJ2_LibraryGen as gen

def agregarNuevoProd(matrix, stockMin, stockMax):
    i=len(matrix)
    codProd='-2'
    stockProd='-1'
    impFlag='i'
        
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

    #Consulta para impresion de tabla
    while impFlag !='Y' or impFlag !='N' or impFlag !='y' or impFlag !='n':
        impFlag=input("Desea mostrar la tabla en pantalla? Y/N ")
        if impFlag=='Y' or impFlag=='y':
            gen.imprimirMatriz(matrix)
            return matrix
        elif impFlag=='N' or impFlag=='n':
            return matrix
        else:
            print("La opción ingresada no es válida.")

    return matrix

def actualizarStockFab(matrix,stockMax):
    i=0
    codProd='-2'
    stockProd='-1'
    impFlag='i'
    #temp=0
    
    while int(codProd)!=-1:
        while codProd.isdigit() is False and int(codProd)!=-1:
            codProd=input("Ingrese el código del producto (Ingrese -1 para cancelar): ")
        if int(codProd)!=-1:
            if len(str(codProd))==4:
                if gen.buscarCodigoDuplicadoMatrix(matrix,int(codProd))==True:
                    while stockProd.isdigit() is False:
                        stockProd=input("Ingrese la cantidad de unidades fabricadas: ")
                    i=gen.buscarCodigoEnTabla(matrix,int(codProd))
                    if matrix[i][1]+int(stockProd) <= stockMax:
                        matrix[i][1]+=int(stockProd)
                        print("Stock actualizado existosamente.")
                        codProd='-2'
                        stockProd='-1'
                    else:
                        matrix[i][1]+=int(stockProd)
                        print("Stock actualizado existosamente.")
                        print("ATENCION: El stock actual del producto ",codProd," supera el máximo de stock permitido.")
                        codProd='-2'
                        stockProd='-1'
                else:
                    print("El código ingresado no existe, re-ingrese el código.")
                    codProd='-2'
            else:
                print("El largo del código es inválido. Ingrese un código de 4 dígitos.")
                codProd='-2'
    
    #Consulta para impresion de tabla
    while impFlag !='Y' or impFlag !='N' or impFlag !='y' or impFlag !='n':
        impFlag=input("Desea mostrar la tabla en pantalla? Y/N ")
        if impFlag=='Y' or impFlag=='y':
            gen.imprimirMatriz(matrix)
            return matrix
        elif impFlag=='N' or impFlag=='n':
            return matrix
        else:
            print("La opción ingresada no es válida.")
    
    return matrix

def actualizarStockVenta(matrix,stockMin):
    i=0
    codProd='-2'
    stockProd='-1'
    impFlag='i'
    
    while int(codProd)!=-1:
        while codProd.isdigit() is False and int(codProd)!=-1:
            codProd=input("Ingrese el código del producto (Ingrese -1 para cancelar): ")
        if int(codProd)!=-1:
            if len(str(int(codProd)))==4:
                if gen.buscarCodigoDuplicadoMatrix(matrix,int(codProd))==True:
                    while stockProd.isdigit() is False:
                        stockProd=input("Ingrese la cantidad de unidades vendidas: ")
                    i=gen.buscarCodigoEnTabla(matrix,int(codProd))
                    if matrix[i][1]>=int(stockProd):
                        matrix[i][1]-=int(stockProd)
                        print("Stock actualizado existosamente.")
                        if matrix[i][1]<stockMin:
                            print("ATENCION: El stock actual del producto ",codProd," está por debajo del stock permitido.")
                        codProd='-2'
                        stockProd='-1'
                    else:
                        print("Las unidedaes ingresadas exceden el stock actual.")
                        codProd='-2'
                        stockProd='-1'
                else:
                    print("El código ingresado no existe, re-ingrese el código.")
                    codProd='-2'
            else:
                print("El largo del código es inválido. Ingrese un código de 4 dígitos.")
                codProd='-2'
    
    #Consulta para impresion de tabla
    while impFlag !='Y' or impFlag !='N' or impFlag !='y' or impFlag !='n':
        impFlag=input("Desea mostrar la tabla en pantalla? Y/N")
        if impFlag=='Y' or impFlag=='y':
            gen.imprimirMatriz(matrix)
            return matrix
        elif impFlag=='N' or impFlag=='n':
            return matrix
        else:
            print("La opción ingresada no es válida.")
    
    return matrix

def eliminarProducto(matrix):
    i=0
    codProd='-2'
    stockProd='-1'
    impFlag='i'
    #temp=0
    
    while int(codProd)!=-1:
        while codProd.isdigit() is False and int(codProd)!=-1:
            codProd=input("Ingrese el código del producto que desea borrar (Ingrese -1 para cancelar): ")
        if int(codProd)!=-1:
            if len(str(codProd))==4:
                if gen.buscarCodigoDuplicadoMatrix(matrix,int(codProd))==True:
                    i=gen.buscarCodigoEnTabla(matrix,int(codProd))
                    matrix.pop(i)
                    print("Producto eliminado.")
                    codProd='-2'
                else:
                    print("El código ingresado no existe, re-ingrese el código.")
                    codProd='-2'
            else:
                print("El largo del código es inválido. Ingrese un código de 4 dígitos.")
                codProd='-2'

    #Consulta para impresion de tabla
    while impFlag !='Y' or impFlag !='N' or impFlag !='y' or impFlag !='n':
        impFlag=input("Desea mostrar la tabla en pantalla? Y/N ")
        if impFlag=='Y' or impFlag=='y':
            gen.imprimirMatriz(matrix)
            return matrix
        elif impFlag=='N' or impFlag=='n':
            return matrix
        else:
            print("La opción ingresada no es válida.")
    
    return matrix
    
def main():
    print()

if __name__=="__main__":
    main()