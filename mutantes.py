def main():
    dna = []
    
    for i in range(6):
        row = input(f"Ingrese la fila {i + 1}: ")
        dna.append(row)

    result = is_mutant(dna)

    if result:
        print("Es un mutante.")
    else:
        print("No es un mutante.")


def is_mutant(dna):
    n = len(dna)
    count = 0

    for i in range(n):
        for j in range(n - 3):
            if dna[i][j] == dna[i][j + 1] == dna[i][j + 2] == dna[i][j + 3]:
                count += 1

    for i in range(n - 3):
        for j in range(n):
            if dna[i][j] == dna[i + 1][j] == dna[i + 2][j] == dna[i + 3][j]:
                count += 1

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
