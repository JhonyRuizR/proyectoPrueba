def run():
    usuario = input("Ingrese su Usuario:\n")
    clave = input("Ingrese su Clave:\n")

    if usuario == "jhony" and clave == "7981":
        print("Usuario logueado correctamente")
    else:
        print("Usuario o clave Incorrecta!!!")


if __name__ == "__main__":
    run()