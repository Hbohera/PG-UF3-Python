def file():
    file_name = input("Introduce el nombre del fichero: ")
    file_name = "Archivos/" + file_name
    return file_name


def choose():
    num = 0
    print("*------------------------------------*\n"
          "*| Opciones:                        |*\n"
          "*| 1. Crear fichero                 |*\n"
          "*| 2. Mostrar contenido del fichero |*\n"
          "*| 3. Modificar el fichero          |*\n"
          "*| 4. Salir                         |*\n"
          "*------------------------------------*")
    while num < 1 or num > 4:
        num = int(input("¿Que opción quieres?: "))
    return num


def ifs(num):
    if num == 1:
        f_create(file())
    elif num == 2:
        f_print(file())
    elif num == 3:
        f_write(file())
    elif num == 4:
        exit(0)


def f_create(file_name):
    f = open(file_name, "w")
    f.close()


def f_print(file_name):
    f = open(file_name, "r")
    line = f.readline()
    while line:
        print(line)
        line = f.readline()
    f.close()


def f_write(file_name):
    f = open(file_name, "w")
    info = input("Introduce los datos que quieres guardar en el fichero: ")
    f.write(info)
    f.close()


def main():
    ifs(choose())


if __name__ == "__main__":
    main()