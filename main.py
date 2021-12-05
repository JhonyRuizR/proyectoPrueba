import user
def run():
    usuario = input("Ingrese su Usuario:\n")
    clave = input("Ingrese su Clave:\n")

    datos = user.datos_usuario()
    if usuario == datos[0] and clave == datos[1]:
        print("Usuario logueado correctamente")
    else:
        print("Usuario o clave Incorrecta!!!")
    print("Agregando mensaje")

if __name__ == "__main__":
    run()