# coding=utf-8
"""
Напишите функцию, которая перебирает натуральные числа от 1 до N включительно
и раскладывает каждое число на простые множители.
Результат можно выводить на экран либо копить в любой структуре данных.
"""


def prime_numbers(n):
    """Sieve of Eratosthenes"""
    a = range(n + 1)
    a[1] = 0
    lst = []

    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in xrange(i, n + 1, i):
                a[j] = 0
        i += 1
    return lst


def multipliers(item, primes):
    mul = []
    while item != 1:
        for prime in primes:
            if item % prime == 0:
                item = item / prime
                mul.append(prime)
                break
    return mul


def prime_multipliers(n):
    result = {}
    primes = prime_numbers(n)
    natural_numbers = [num for num in range(1, n + 1)]
    for item in natural_numbers:
        if item == 1:
            result[item] = [1]
            continue

        result[item] = multipliers(item, primes)

    print result


if __name__ == '__main__':
    # prime_multipliers(1000)
    prime_multipliers(int(input('N = ')))
