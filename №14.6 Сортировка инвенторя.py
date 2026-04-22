prices_input = input('Введите цены предметов через пробел: ')

prices = list(map(int, prices_input.split()))

ascending = sorted(prices)
descending = sorted(prices, reverse=True)
original = prices.copy()
reverse = prices[::-1]

print(f'Сортировка по возрастанию: {ascending}')
print(f'Сортировка по убыванию: {descending}')
print(f'Оригинальный порядок(от старых к новым): {original}')
print(f'Обратный порядок(от новых к стары): {reverse}')
