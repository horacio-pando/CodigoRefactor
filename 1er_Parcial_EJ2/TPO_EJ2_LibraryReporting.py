import TPO_EJ2_LibraryGen as gen

#ordenarProductos=lambda matrix,a=False: gen.imprimirMatriz(matrix.sort(reverse=a))

def ordenarProductos(matrix,a=False):
    '''Ordena la tabla ingresada por código de producto de manera ascendente por defecto.
        Para ordenar de manera descendente ingresar como 2do parametro True'''
    matrix.sort(reverse=a)
    gen.imprimirMatriz(matrix)

def productosStockMenorMin(matrix,stockMin):
    i=0
    codProd=0
    stockProd=0
    tempMatrix=[]
    filas = len(matrix)
    for f in range(filas):
        if matrix[f][1]<stockMin:
            tempMatrix.append(matrix[f])
            i+=1
    if tempMatrix==[]:
        print("No hay productos con stock por debajo del mínimo.")
    else:
        tempMatrix.sort(key=lambda tempMatrix:tempMatrix[1])
        gen.imprimirMatriz(tempMatrix)

def StockProducto(matrix):
    i=0
    codProd='-2'
    stockProd=0
    tempMatrix=[]
    
    while int(codProd)!=-1:
        while codProd.isdigit() is False and int(codProd)!=-1:
            codProd=input("Ingrese el código del producto (Ingrese -1 para cancelar): ")
        if int(codProd)!=-1:
            if len(str(int(codProd)))==4:
                if gen.buscarCodigoDuplicadoMatrix(matrix,int(codProd))==True:
                    i=gen.buscarCodigoEnTabla(matrix,int(codProd))
                    tempMatrix.append(matrix[i])
                    gen.imprimirMatriz(tempMatrix)
                    tempMatrix=[]
                    codProd='-2'
                else:
                    print("El código ingresado no existe, re-ingrese el código.")
                    codProd='-2'
            else:
                print("El largo del código es inválido. Ingrese un código de 4 dígitos.")
                codProd='-2'

def main():
    print()

if __name__=="__main__":
    main()