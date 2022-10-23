import numpy as np

print('Нахождение обратной матрицы')

print('')
strA = input('Кол-во сторк в A матрице: ')
print('')

iA = 0
A = []

while int(strA) > iA:
    iA = iA + 1
    AS = list(map(int, input(f'A{iA}: ').split()))
    A.append(AS)


def minor(arr, i, j):
    return arr[np.array(list(range(i)) + list(range(i + 1, arr.shape[0])))[:, np.newaxis],
               np.array(list(range(j)) + list(range(j + 1, arr.shape[1])))]


a = np.array(A)
d = round(np.linalg.det(a), 1)

print('')

if d:
    print(f'Определитель матрицы равен {d}')
    if int(strA) <= 2:
        minor = [
            [a[1][1], a[1][0]],
            [a[0][1], a[0][0]],
        ]
        print(f'Минор: {minor}')
        alg = [
            [minor[0][0], - minor[0][1]],
            [- minor[1][0], minor[1][1]],
        ]
        print(f'Алгебраические дополнения: {alg}')
        trans = [
            [alg[0][0], alg[1][0]],
            [alg[0][1], alg[1][1]],
        ]
        print(f'Транспонированная матрица: {trans}')
        print(f'Ответ: A¯¹ = 1/{d} {trans}')
        answer = np.dot(1/d, trans)
        print(answer)
        check = np.dot(a, answer)
        print(f'Проверка: a * answer')
        print(f'{check}')
    elif int(strA) <= 3:
        index = -1
        matrix_minor = []
        for item in a:
            index = index + 1
            index_val = -1
            str_minor = []
            for val in item:
                index_val = index_val + 1
                minor_result = minor(a, index, index_val)
                str_minor.append(minor_result[0][0] * minor_result[1][1] - minor_result[0][1] * minor_result[1][0])
            matrix_minor.append(str_minor)
        print(f'Минор: {matrix_minor}')
        matrix_alg = [
            [matrix_minor[0][0], matrix_minor[0][1] * -1, matrix_minor[0][2]],
            [matrix_minor[1][0] * -1, matrix_minor[1][1], matrix_minor[1][2] * -1],
            [matrix_minor[2][0], matrix_minor[2][1] * -1, matrix_minor[2][2]],
        ]
        print(f'Алгебраические дополнения: {matrix_alg}')
        matrix_trans = [
            [matrix_minor[0][0], matrix_minor[1][0] * -1, matrix_minor[2][0]],
            [matrix_minor[0][1] * -1, matrix_minor[1][1], matrix_minor[2][1] * -1],
            [matrix_minor[0][2], matrix_minor[1][2] * -1, matrix_minor[2][2]],
        ]
        print(f'Транспонированная матрица: {matrix_trans}')
        print(f'Ответ: A¯¹ = 1/d * (matrix_trans)')
        answer = np.dot(matrix_trans, d)
        print(f'{answer}')
        check = np.dot(a, answer)
        print(f'Проверка: a * answer')
        print(f'{check}')

else:
    print(f'Определитель матрицы равен {d} - обратной матрицы не существует')
