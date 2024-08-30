def get_matrix ():
    strings = input('Введите кол-во строк: ')
    n = int(strings)
    columns = input ('Введите кол-во столбцов: ')
    m = int(columns)
    value = input('Введите значение: ')
    matrix = []
    for strings in range(n):
        mat = []
        matrix.append(mat)
        for columns in range(m):
            mat.append(value)
    print(matrix)
get_matrix()




