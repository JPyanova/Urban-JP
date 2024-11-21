def is_prime(function):
    def wrapper(*args):
        function_result = function(*args)
        is_prime = True
        for divider in range(2, function_result):
            if function_result % divider == 0:
                is_prime = False
        if is_prime == True:
            return f'{function_result} является простым числом'
        else:
            return f'{function_result} является составным числом'
    return wrapper

@is_prime
def sum_three(a, b, c):
    sum_result = a + b + c
    return sum_result

result = sum_three(2, 3, 6)
print(result)