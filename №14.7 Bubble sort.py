numbers = [64, 34, 25, 12, 22, 11, 90]

print(f'Исходный список: {numbers}')

sorted_numbers = numbers.copy()
num = len(sorted_numbers)
swapped = True

while swapped:
    swapped = False
    i = 0
    while i < num - 1:
        if sorted_numbers[i] > sorted_numbers[i + 1]:
            temp = sorted_numbers[i]
            sorted_numbers[i] = sorted_numbers[i + 1]
            sorted_numbers[i + 1] = temp
            swapped = True
        i += 1
    num -= 1

print(f'Отсортированный список: {sorted_numbers}')
