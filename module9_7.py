def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 2 or result % 2 == 0:
            print("Составное")
        elif result >= 2:
            for i in range(3, int(result**0.5) + 1, 2):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(1, 2, 7)
print(result)



