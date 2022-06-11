# Напишите программу для проверки истинности утверждения
#          ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z                для всех значений предикат

X = int(input('Введи значение X -> '))
Y = int(input('Введи значение Y -> '))
Z = int(input('Введи значение Z -> '))

f = not (X or Y or Z) is not X and not Y and not Z
print(f)