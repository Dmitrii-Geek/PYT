# https://drive.google.com/file/d/10d7xyKM2fcPiTs_vnKqJknsNAHsGvbuy/view?usp=sharing
# Найти сумму и произведение цифр введённого пользователем трехзначного числа

num = input('Введите натуральное трёхзначное число: ')

num = int(num)
a = num // 100
b = num % 100 // 10
c = num % 10
summary = a + b + c
# mult = a * b * c
print(f'Сумма = {summary}')
print(f'Произведение = {a * b * c}')
