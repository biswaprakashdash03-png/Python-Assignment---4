num = int(input("Enter a number: "))

sum_even_factors = 0

for i in range(1, num + 1):
    if num % i == 0 and i % 2 == 0:
        sum_even_factors += i

print("Sum of even factors =", sum_even_factors)