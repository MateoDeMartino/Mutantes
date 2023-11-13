def main():
    letras = ("A","T","C","G")
    
    dna = []
    while(len(dna)<6):
        codigo = input("Ingrese el codigo: ")
        print("validando caracteres")
        if len(codigo) == 6:
            contiene = all(letra.upper() in letras for letra in codigo)
            if contiene:
                dna.append(codigo)
                print("Se guardo correctamente")
                print(dna)
            else:
                print(f"el codigo no contiene unicamente {letras}, ingreselo nuevamente")
        else:
            print("el codigo no tiene 6 caracteres,ingreselo nuevamente")
            
    # dna = ['atcgtc', 'agttat', 'tcatta', 'agactg', 'tatcct', 'ggacca']

    result = is_mutant(dna)

    if result:
        print("Es un mutante.")
    else:
        print("No es un mutante.")


def is_mutant(dna):
    n = len(dna)
    count = 0
    
    # Verifica filas horizontales
    for i in range(n):
        for j in range(n - 3):
            if dna[i][j] == dna[i][j + 1] == dna[i][j + 2] == dna[i][j + 3]:
                count += 1

    # Verifica columnas verticales
    for i in range(n - 3):
        for j in range(n):
            if dna[i][j] == dna[i + 1][j] == dna[i + 2][j] == dna[i + 3][j]:
                count += 1

    # Verifica diagonales
    for i in range(n - 3):
        for j in range(n - 3):
            if dna[i][j] == dna[i + 1][j + 1] == dna[i + 2][j + 2] == dna[i + 3][j + 3]:
                count += 1

    for i in range(n - 3):
        for j in range(n - 1, 2, -1):
            if dna[i][j] == dna[i + 1][j - 1] == dna[i + 2][j - 2] == dna[i + 3][j - 3]:
                count += 1

    return count > 1


if __name__ == "__main__":
    main()
