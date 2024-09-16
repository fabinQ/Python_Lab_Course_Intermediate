def fibonacci(n):
    if n <= 0:
        raise ValueError("Podaj wartość n większą od zera.")

    if n == 1:
        return 0

    if n == 2:
        return 1

    prev_prev = 0
    prev = 1

    for _ in range(3, n + 1):
        current = prev_prev + prev
        prev_prev = prev
        prev = current

    return prev

# Testujemy funkcję
n = 2000000
result = fibonacci(n)
print(f"Liczba Fibonacciego o indeksie {n} wynosi: {result}")