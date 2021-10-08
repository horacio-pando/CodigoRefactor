import TPO_EJ2_LibraryGen as gen #Import para modulo de funciones genericas
import TPO_EJ2_LibraryInitialLoad as inLoad #Import para modulo de Carga inicial
import TPO_EJ2_LibraryUpdateRecord as updRec #Import para modulo actualización de tabla
import TPO_EJ2_LibraryReporting as reportData #Import para modulo de reportes
import subprocess as os #Import para comando clear

def main():
    menuFlag='-1'
    subMenuFlag='-1'
    matrix=[]
    
    mockTableLoaded=False
    temp='-1'
    
    stockMinimo=10
    stockMaximo=100
    
    '''Interfaz Menu: Muestra las distintas opciones de menu en base al input del usuario.
    1. Carga Inicial
        1.1 Realizar carga inicial de prueba
        1.2 Definir stock mínimo
        1.3 Definir stock máximo
    2. Actualizar Stock
        2.1 Nuevo Producto
        2.2 Actualizar stock por Venta
        2.3 Actualizar stock por Fabricación
    3. Consultas e Informes
        3.1 Ordenar por código y mostrar tabla
        3.2 Productos con stock debajo del mínimo
        3.3 Detalle de stock de un producto
    '''
    while int(menuFlag) !=0:
        os.call('clear')
        gen.menuPrincipal()
        while menuFlag.isdigit() is False:
            menuFlag=str(input())
        if int(menuFlag)==1: #Menu Carga Inicial
            while subMenuFlag !=0:
                os.call('clear')
                gen.subMenuCI()
                while subMenuFlag.isdigit() is False:
                    subMenuFlag=str(input())
                if int(subMenuFlag)==1:
                    if mockTableLoaded==True:
                        print("La carga de prueba ya se encuentra realizada.")
                    else:
                        os.call('clear')
                        matrix=inLoad.initializeMatrix(matrix,stockMinimo,stockMaximo)
                        mockTableLoaded=True
                    subMenuFlag='-1'
                elif int(subMenuFlag)==2:
                    while temp.isdigit() is False:
                        temp=input("Ingrese el stock mínimo que debe tener cada producto: ")
                    stockMinimo=int(temp)
                    print("Stock mínimo actualizado.")
                    input()
                    temp='-1'
                    subMenuFlag='-1'
                elif int(subMenuFlag)==3:
                    while temp.isdigit() is False:
                        temp=input("Ingrese el stock máximo que debe tener cada producto: ")
                    stockMaximo=int(temp)
                    print("Stock máximo actualizado.")
                    input()
                    temp='-1'
                    subMenuFlag='-1'
                elif int(subMenuFlag)==0:
                    subMenuFlag=0
                    menuFlag='-1'
                else:
                    print("Opción de menu invalida. Por favor seleccione una de las secciones listadas.")
                    subMenuFlag='-1'
            subMenuFlag='-1'
        elif int(menuFlag)==2: #Menu Actualizar Stock
            while subMenuFlag !=0:
                os.call('clear')
                gen.subMenuAS()
                while subMenuFlag.isdigit() is False:
                    subMenuFlag=str(input())
                if int(subMenuFlag)==1:
                    updRec.agregarNuevoProd(matrix, stockMinimo, stockMaximo)
                    subMenuFlag='-1'
                elif int(subMenuFlag)==2:
                    updRec.actualizarStockFab(matrix, stockMaximo)
                    subMenuFlag='-1'
                elif int(subMenuFlag)==3:
                    updRec.actualizarStockVenta(matrix, stockMinimo)
                    subMenuFlag='-1'
                elif int(subMenuFlag)==4:
                    updRec.eliminarProducto(matrix)
                    subMenuFlag='-1'
                elif int(subMenuFlag)==0:
                    subMenuFlag=0
                    menuFlag='-1'
                else:
                    print("Opción de menu invalida. Por favor seleccione una de las secciones listadas.")
                    subMenuFlag='-1'
            subMenuFlag='-1'
        elif int(menuFlag)==3: #Menu Consultas e Informes
            while subMenuFlag !=0:
                os.call('clear')
                gen.subMenuCoIn()
                while subMenuFlag.isdigit() is False:
                    subMenuFlag=str(input())
                if int(subMenuFlag)==1:
                    reportData.ordenarProductos(matrix)
                    subMenuFlag='-1'
                elif int(subMenuFlag)==2:
                    reportData.productosStockMenorMin(matrix,stockMinimo)
                    subMenuFlag='-1'
                elif int(subMenuFlag)==3:
                    reportData.StockProducto(matrix)
                    subMenuFlag='-1'
                elif int(subMenuFlag)==0:
                    subMenuFlag=0
                    menuFlag='-1'
                else:
                    print("Opción de menu invalida. Por favor seleccione una de las secciones listadas.")
                    subMenuFlag='-1'
            subMenuFlag='-1'
        elif int(menuFlag)==0: #Cerrar Programa
            print("Gracias, que tenga buen día.")
        else: #Error en opción incorrecta
            print("Opción de menu invalida. Por favor seleccione una de las secciones listadas.")
            subMenuFlag='-1'
        #menuFlag='-1'
    

if __name__=="__main__":
    main()
