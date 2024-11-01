# Первое задание: даны три целых числа: A, B, C. Проверить истинность высказывания: «Ровно два из
# чисел A, B, C являются положительными»
def check_two_positive(A, B, C):
    # Проверяем, сколько из чисел положительные
    positive_count = (A > 0) + (B > 0) + (C > 0)
    return positive_count == 2

# Пример
A = 5
B = -1
C = 3
result = check_two_positive(A, B, C)
print("Ровно два числа положительные:", result)

# Второе задание: даны три целых числа, одно из которых отлично от двух других, равных между
# собой. Определить порядковый номер числа, отличного от остальных
def find_unique_number_index(a, b, c):
    if a == b:
        return 3  # C отличается
    elif a == c:
        return 2  # B отличается
    else:
        return 1  # A отличается

# Пример:
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
result = find_unique_number_index(a, b, c)
print(f"Порядковый номер числа, отличного от остальных: {result}")