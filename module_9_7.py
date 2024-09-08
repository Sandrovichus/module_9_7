def is_prime(func):
    def wrapper(*args, **kwargs):
        func_result = func(*args, **kwargs)
        prime = True
        for i in range(2, func(*args, **kwargs)):
            if func(*args, **kwargs) % i == 0:
                prime = False
                break
        if prime:
            print('Простое')
        else:
            print('Составное')
        return func_result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)

result = sum_three(20, 30, 70)
print(result)
