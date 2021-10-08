"""devuelve un numero entero ingresado por teclado y corrobora que sea positivo y natural"""
def teclado(texto = "Ingrese un numero: "):
    cad = input(texto)
    while cad.isdigit() is False:
        cad = input("Error. Ingrese un numero positivo y natural: ")
    return int(cad)


#funcion main
def main():
    x = teclado()
    print(x)
    
if __name__ == "__main__":
     main()
