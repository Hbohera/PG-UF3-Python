def main():
    f = open("Archivos/text.txt", "w")
    info = input("Introduce los datos que quieres guardar en el fichero: ")
    f.write(info)
    f.close()

if __name__ == "__main__":
    main()