def main():
    f = open("Archivos/text.txt", "a")
    info = input("Introduce los datos que quieres guardar en el fichero: ")
    f.write(info + '\n')
    f.close()

if __name__ == "__main__":
    main()