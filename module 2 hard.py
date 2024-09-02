num = int(input('Введите проверочное число: '))

def anc_code(num):
    code = ''
    for i in range(1, num):
        for j in range(i + 1, num):
            if num % (i + j) == 0:
                code += str(i) + str(j)
    return code

print(f'''Ваш пароль: {anc_code(num)}''')
